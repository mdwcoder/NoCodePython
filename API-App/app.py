from flask import Flask, request, jsonify
from flask_cors import CORS
import os, re
from dotenv import load_dotenv

import references

load_dotenv()

LocalIp = os.getenv('IP')
Frontend_Port = os.getenv('FrontEndPort')
Frontend_IP = os.getenv('FrontEndIp')
Backend_Port = os.getenv('BackEndPort')

operadores = references.Operadores()
patrones = references.Patrones()

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True,
    methods=["GET", "POST", "DELETE", "OPTIONS"],
    headers=["Content-Type", "X-Requested-With",
             "X-CSRFToken", "Authorization"],
    origins=[f"http://localhost:{Frontend_Port}",
             f"{LocalIp}{Frontend_Port}",
             f"{LocalIp}",
             ]
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Funciones sin metodo para el programa

def translate_line(entrada):
    # Traducir una línea de código
    for patron, reemplazo in operadores.items():
        entrada = re.sub(patron, reemplazo, entrada)

    for patron, reemplazo in patrones.items():
        match = re.match(patron, entrada)
        if match:
            traduccion = re.sub(patron, reemplazo, entrada)
            if ":\n" in traduccion:
                linea_principal, resto = traduccion.split(":\n", 1)
                lineas = resto.split(", ")
                lineas_traducidas = [linea_principal + ":"]
                for linea in lineas:
                    linea_traducida = translate_line(linea.strip())
                    lineas_traducidas.append("    " + linea_traducida)
                return "\n".join(lineas_traducidas)
            return traduccion

    return "No se encontró un patrón coincidente."

def translate(InputBase):
    # Traducir el código de entrada
    def add_text_if_present(text, conditions):
        for a, b in conditions.items():
            if a in text:
                text += f"\n{b}"
        return text
    InputCompleto = InputBase.split("\n")
    OutputCompleto = []
    for entrada in InputCompleto:
        # Reemplazar operadores
        for patron, reemplazo in operadores.items():
            entrada = re.sub(patron, reemplazo, entrada)

        # Verificar si la entrada es un bloque de código (condicional o bucle)
        bloque_traducido = False
        for patron, reemplazo in patrones.items():
            match = re.match(patron, entrada)
            if match:
                traduccion = re.sub(patron, reemplazo, entrada)
                # Si es un condicional o un bucle, traducir el bloque de código dentro
                if ":\n" in traduccion:
                    linea_principal, resto = traduccion.split(":\n", 1)
                    lineas = resto.split(", ")
                    lineas_traducidas = [linea_principal + ":"]
                    for linea in lineas:
                        linea_traducida = translate_line(linea.strip())
                        lineas_traducidas.append("    " + linea_traducida)
                    OutputCompleto.append("\n".join(lineas_traducidas))
                else:
                    OutputCompleto.append(traduccion)
                bloque_traducido = True
                break

        if not bloque_traducido:
            # Si no es un bloque de código, intentar traducir la línea
            for patron, reemplazo in patrones.items():
                match = re.match(patron, entrada)
                if match:
                    OutputCompleto.append(re.sub(patron, reemplazo, entrada))
                    bloque_traducido = True
                    break

        if not bloque_traducido:
            OutputCompleto.append("No se encontró un patrón coincidente.")

    # Unir todas las traducciones en un solo string con saltos de línea
    traduccion_final = add_text_if_present("\n".join(OutputCompleto), references.EndCodeLib())
    return traduccion_final

@app.route('/API/translate', methods=["GET"])
def translate_fn():
    data = request.json
    Natulal_Lenguaje_Code = data.get('NaturalLenguajeCode')
    PythonCode = translate(Natulal_Lenguaje_Code)

    return jsonify({'traduccion':PythonCode})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(Backend_Port))
