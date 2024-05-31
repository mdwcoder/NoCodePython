# UI Library's
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import  QProcess, QObject, pyqtSignal
# System Library's
import os, sys, re, webbrowser
# Local imports
import stylesheet
import tools as wtools
import images as wimg
from Ui_main import Ui_main

class CodeExecutor(QObject):
    codeFinished = pyqtSignal()
    inputRequested = pyqtSignal()

    def __init__(self, code):
        super().__init__()
        self.code = code
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.on_ready_read_output)
        self.process.readyReadStandardError.connect(self.on_ready_read_error)
        self.process.finished.connect(self.on_process_finished)
        self.stdinBuffer = ""

    def execute_code(self):
        self.process.start("python", ["-c", self.code])

    def on_ready_read_output(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.output.append(output)
        if "input(" in output:
            self.inputRequested.emit()

    def on_ready_read_error(self):
        error = self.process.readAllStandardError().data().decode()
        self.output.append(f"Error: {error}")

    def on_process_finished(self):
        self.codeFinished.emit()

    def send_input(self, text):
        self.process.write(text.encode() + b"\n")

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
            self.ui_main.languajeComboBox.currentIndexChanged.connect(self.languajeChange)
            self.ui_main.sendButton.clicked.connect(self.send_user_input)  # Conectar el botón de enviar

            self.ui_main.codeSpace.setPlaceholderText("Pon tu código aquí...")
            self.index = self.ui_main.languajeComboBox.currentIndex()

        def stylesheetmod():
            self.ui_main.exitButton.setStyleSheet(stylesheet.exitButton())
            self.ui_main.titleLabel.setStyleSheet(stylesheet.titleLabel())
            self.ui_main.sendButton.setStyleSheet(stylesheet.sendButton())

        self.ui_main.setupUi(self)
        self.setWindowIcon(wimg.icon())
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

    def execute_code(self):
        code = self.translate().replace("No se encontró un patrón coincidente.", "")

        self.ui_main.textBrowser.clear()

        self.ui_main.textBrowser.append((
            "Ejecutando código :\n",
            "Running code :\n",
            "Code en cours d'exécution :\n"
            )[self.index])
        self.ui_main.textBrowser.append("-"*35)
        self.ui_main.textBrowser.append(code)
        self.ui_main.textBrowser.append("-"*35+"\n")
        self.ui_main.textBrowser.append((
            "Salida del código :\n",
            "Output :\n",
            "Sortie du code :\n"
        )[self.index])

        self.code_executor = CodeExecutor(code)
        self.code_executor.output = self.ui_main.textBrowser
        self.code_executor.codeFinished.connect(self.on_code_finished)
        self.code_executor.inputRequested.connect(self.on_input_requested)
        self.code_executor.execute_code()

    def on_code_finished(self):
        self.ui_main.textBrowser.append((
            "Ejecución terminada.",
            "Execution finished.",
            "Exécution terminée."
            )[self.index])

    def on_input_requested(self):
        self.ui_main.textBrowser.append((
            "Esperando entrada de usuario...",
            "Waiting for user input...",
            "En attente de l'entrée de l'utilisateur..."
            )[self.index])

    def send_user_input(self):
        user_input = self.ui_main.commandLine.text()
        self.code_executor.send_input(user_input)
        self.ui_main.commandLine.clear()

    def exit_(self):
        if wtools.confirmar_mensaje(
            ("Perderá todo lo no guardado.",
             "You will lose everything not saved.",
             "Vous perdrez tout ce qui n'est pas sauvegardé."
             )[self.index],
            self.index):
            exit()

    def open_github(self):
        url = "https://github.com/mdwcoder/NoCodePython"
        webbrowser.open(url)

    def languajeChange(self, index):
        self.index = index
        widgets = (
            self.ui_main.saveButton,
            self.ui_main.runButton,
            self.ui_main.helpButton,
            self.ui_main.clearButton,
            self.ui_main.openButton,
            self.ui_main.exitButton
        )
        placeholder = ("Pon tu código aquí...", "Put your code here...", "Mettez votre code ici")
        words_languajes = wtools.words()

        self.ui_main.codeSpace.setPlaceholderText(placeholder[index])
        for widget in widgets:
            widget.setText(words_languajes[widgets.index(widget)][index])

    def translate(self):
        def add_text_if_present(text, conditions):
            for a, b in conditions.items():
                if a in text:
                    text += f"\n{b}"
            return text
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
        traduccion_final = add_text_if_present("\n".join(OutputCompleto), wtools.EndCodeLib())
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
            wtools.show_error_message((
                "El modo changeOsave no esta claro.",
                "The changeOsave mode is not clear.",
                "Le mode changeOsave n'est pas clair."
                )[self.index],
                self.index)
            return "error"
        if self.ui_main.save_mdw_select.isChecked() and self.ui_main.save_py_select.isChecked():
            wtools.show_error_message((
                "No deberrias poder seleccionar ambos, intentalo de nuevo.",
                "You should not be able to select both, try again.",
                "Vous ne devriez pas pouvoir sélectionner les deux, réessayez"
                )[self.index],
                self.index)
        elif self.ui_main.save_mdw_select.isChecked():
            return "mdw"
        elif self.ui_main.save_py_select.isChecked():
            if wtools.confirmar_mensaje((
                "No podras cambiar a modo NoCode despues, se recomienda guardar antes como .mdw.",
                "You will not be able to change to NoCode mode afterwards, it is recommended to save as .mdw first",
                "Vous ne pourrez plus passer en mode NoCode par la suite, il est recommandé de sauvegarder d'abord au format .mdw"
                )[self.index],
                self.index):
                return "py"
        else:
            wtools.show_error_message((
                "Para poder guardar el archivo tiene que seleccionar .mdw o .py.",
                "To be able to save the file, you must select .mdw or .py.",
                "Pour enregistrer le fichier, vous devez sélectionner .mdw ou .py."
                )[self.index],
                self.index)
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
                wtools.show_error_message(
                    ("Error al guardar el archivo",
                     "Error saving file",
                     "Erreur lors de l'enregistrement du fichier"
                     )[self.index]+f": {e}",
                    self.index)
        else:
            wtools.show_error_message(
                ("No se ha seleccionado una ruta de archivo.",
                "A file path has not been selected.",
                "Aucun chemin de fichier n'a été sélectionné."
                )[self.index]
                , self.index)
        wtools.show_information_message((
            "Archivo guardado correctamente",
            "File saved successfully",
            "Fichier enregistré avec succès"
            )[self.index],
            self.index)

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
            wtools.show_error_message((
                "No se ha seleccionado un archivo.",
                "No file has been selected.",
                "Aucun fichier sélectionné."
                )[self.index],
                self.index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = gui_class()
    gui.show()
    sys.exit(app.exec_())
