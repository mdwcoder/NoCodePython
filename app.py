from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import os, sys, re
import stylesheet
import tools as wtools
from Ui_main import Ui_main
from PyQt5.QtCore import  QProcess, QObject, pyqtSignal
import webbrowser

class CodeExecutor(QObject):
    codeFinished = pyqtSignal()

    def __init__(self, code):
        super().__init__()
        self.code = code
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.on_ready_read_output)
        self.process.finished.connect(self.on_process_finished)

    def execute_code(self):
        self.process.start("python", ["-c", self.code])

    def on_ready_read_output(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.output.append(output)

    def on_process_finished(self):
        self.codeFinished.emit()

class gui_class(QMainWindow):
    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)
        self.init_config()
        self.load_mainUI()
                
    def load_mainUI(self):
        def conect_widgets():
            self.ui_main.saveButton.clicked.connect(self.save)
            self.ui_main.exitButton.clicked.connect(self.exit_)
            self.ui_main.runButton.clicked.connect(self.execute_code)
            self.ui_main.clearButton.clicked.connect(self.clear_console)
            self.ui_main.openButton.clicked.connect(self.load_file)
            self.ui_main.helpButton.clicked.connect(self.open_github)
            
            self.ui_main.codeSpace.setPlaceholderText("Pon tu código aquí")
        def stylesheetmod():
            self.ui_main.exitButton.setStyleSheet(stylesheet.exitButton())
            self.ui_main.titleLabel.setStyleSheet(stylesheet.titleLabel())
            self.ui_main.sendButton.setStyleSheet(stylesheet.sendButton())
        self.ui_main.setupUi(self)
        conect_widgets()
        stylesheetmod()
        
    def init_config(self):
        def loadSomeThings():
            self.patrones = wtools.Patrones()
            self.operadores = wtools.Operadores()
            self.code_executor = None
        self.ui_main = Ui_main()
        self.setStyleSheet(stylesheet.stylesheet())    
        self.setWindowTitle("NoCodePython")
        loadSomeThings()
    
    def exit_(self):
        if wtools.confirmar_mensaje("Perderá todo lo no guardado."):
            exit()
            
    def open_github(self):
        url = "https://github.com/mdwcoder/NoCodePython"
        webbrowser.open(url)

    
    def translate(self):
        InputCompleto = self.ui_main.codeSpace.toPlainText().split("\n")
        OutputCompleto = []
        for entrada in InputCompleto:
            # Reemplazar operadores
            for patron, reemplazo in self.operadores.items():
                entrada = re.sub(patron, reemplazo, entrada)
            
            # Verificar si la entrada es un bloque de código (condicional o bucle)
            bloque_traducido = False
            for patron, reemplazo in self.patrones.items():
                match = re.match(patron, entrada)
                if match:
                    traduccion = re.sub(patron, reemplazo, entrada)
                    # Si es un condicional o un bucle, traducir el bloque de código dentro
                    if ":\n" in traduccion:
                        linea_principal, resto = traduccion.split(":\n", 1)
                        lineas = resto.split(", ")
                        lineas_traducidas = [linea_principal + ":"]
                        for linea in lineas:
                            linea_traducida = self.translate_line(linea.strip())
                            lineas_traducidas.append("    " + linea_traducida)
                        OutputCompleto.append("\n".join(lineas_traducidas))
                    else:
                        OutputCompleto.append(traduccion)
                    bloque_traducido = True
                    break
            
            if not bloque_traducido:
                # Si no es un bloque de código, intentar traducir la línea
                for patron, reemplazo in self.patrones.items():
                    match = re.match(patron, entrada)
                    if match:
                        OutputCompleto.append(re.sub(patron, reemplazo, entrada))
                        bloque_traducido = True
                        break
            
            if not bloque_traducido:
                OutputCompleto.append("No se encontró un patrón coincidente.")
        
        # Unir todas las traducciones en un solo string con saltos de línea
        traduccion_final = "\n".join(OutputCompleto)
        return traduccion_final

    def translate_line(self, entrada):
        # Reemplazar operadores
        for patron, reemplazo in self.operadores.items():
            entrada = re.sub(patron, reemplazo, entrada)
        
        # Verificar si la entrada es un bloque de código (condicional o bucle)
        for patron, reemplazo in self.patrones.items():
            match = re.match(patron, entrada)
            if match:
                traduccion = re.sub(patron, reemplazo, entrada)
                # Si es un condicional o un bucle, traducir el bloque de código dentro
                if ":\n" in traduccion:
                    linea_principal, resto = traduccion.split(":\n", 1)
                    lineas = resto.split(", ")
                    lineas_traducidas = [linea_principal + ":"]
                    for linea in lineas:
                        linea_traducida = self.translate_line(linea.strip())
                        lineas_traducidas.append("    " + linea_traducida)
                    return "\n".join(lineas_traducidas)
                return traduccion
        
        # Si no es un bloque de código, intentar traducir la línea
        for patron, reemplazo in self.patrones.items():
            match = re.match(patron, entrada)
            if match:
                return re.sub(patron, reemplazo, entrada)
        
        return "No se encontró un patrón coincidente."
        
    def changeOsave(self, mode):
        if mode != "s" and mode !=  "c":
            wtools.show_error_message("El modo changeOsave no esta claro.")
            return "error"
        if self.ui_main.save_mdw_select.isChecked() and self.ui_main.save_py_select.isChecked():
            wtools.show_error_message("No deberrias poder seleccionar ambos, intentalo de nuevo.")
        elif self.ui_main.save_mdw_select.isChecked():
            return "mdw"
        elif self.ui_main.save_py_select.isChecked():
            if wtools.confirmar_mensaje(
                "No podras cambiar a modo NoCode despues, se recomienda guardar antes como .mdw."
                ):
                return "py"  
        else:
            if  mode == "s":
                accion = "guardar el archivo"
            else:
                accion = "cambiar el modo"
            wtools.show_error_message(f"Para poder {accion} tiene que seleccionar .mdw o .py.")      
            return "error" 
    
    def clear_console(self):
        self.ui_main.textBrowser.clear()
        
    def seleccionar_ruta_guardar_archivo(self, mode):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # Para evitar el uso de diálogos nativos en macOS
        if mode == "mdw":
            ruta, _ = QFileDialog.getSaveFileName(None, "Guardar archivo", "", "MDW files (*.mdw);;Todos los archivos (*)", options=options)
        else:
            ruta, _ = QFileDialog.getSaveFileName(None, "Guardar archivo", "", "Python files (*.py);;Todos los archivos (*)", options=options)
        return f"{ruta}.{mode}"

        
    def save(self):
        mode = self.changeOsave("s")
        if mode == "error":
            return

        code = self.ui_main.codeSpace.toPlainText()
        if mode == "py":
            code = self.translate().replace("No se encontró un patrón coincidente.", "")

        ruta_ = self.seleccionar_ruta_guardar_archivo(mode)
        if ruta_:
            try:
                with open(ruta_, "w", encoding="utf-8") as archivo:
                    archivo.write(code)
            except Exception as e:
                wtools.show_error_message(f"Error al guardar el archivo: {e}")
        else:
            wtools.show_error_message("No se ha seleccionado una ruta de archivo.")
        wtools.show_information_message("Archivo guardado correctamente")
    
    def seleccionar_ruta_cargar_archivo(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog  # Para evitar el uso de diálogos nativos en macOS
            ruta, _ = QFileDialog.getOpenFileName(None, "Cargar archivo", "", "MDW files (*.mdw);;Todos los archivos (*)", options=options)
            return ruta
                
    def load_file(self):
        try:
            with open(self.seleccionar_ruta_cargar_archivo(), "r", encoding="utf-8") as archivo:
                newCode = archivo.read().replace("No se encontró un patrón coincidente.", "")
            self.ui_main.codeSpace.clear()
            self.ui_main.codeSpace.setPlainText(newCode)
        except:
            wtools.show_error_message("No se ha seleccionado un archivo.")

    def execute_code(self):
        code = self.translate().replace("No se encontró un patrón coincidente.", "")
        
        self.ui_main.textBrowser.clear()
        
        self.ui_main.textBrowser.append(f"Ejecutando código:")
        self.ui_main.textBrowser.append(code)

        self.code_executor = CodeExecutor(code)
        self.code_executor.output = self.ui_main.textBrowser
        self.code_executor.codeFinished.connect(self.on_code_finished)
        self.code_executor.execute_code()
    
    def on_code_finished(self):
        self.ui_main.textBrowser.append("Ejecución terminada.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = gui_class()
    gui.show()
    sys.exit(app.exec_())