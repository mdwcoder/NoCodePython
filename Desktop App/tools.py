from PyQt5.QtGui import QTextCursor, QTextCharFormat, QFont
from PyQt5.QtWidgets import  QMessageBox

def show_error_message(descripcion_del_error, index):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("¡Ha ocurrido un error!" if index == 0 else "An error has occurred!" if index == 1 else "Une erreur s'est produite!")
        msg.setInformativeText(descripcion_del_error)
        msg.exec_()

def show_warning_message(descripcion_de_advertencia, index):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle("Advertencia")
    msg.setText("¡Advertencia!" if index == 0 else "Warning!" if index == 1 else "Avertissement!")
    msg.setInformativeText(descripcion_de_advertencia)
    msg.exec_()

def show_information_message(descripcion_de_informacion, index):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Información")
    msg.setText("¡Información!" if index == 0 else "Information!" if index == 1 else "Information!")
    msg.setInformativeText(descripcion_de_informacion)
    msg.exec_()

def confirmar_mensaje(descripcion, index):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setWindowTitle("Confirmar")
    msg.setText("¿Está seguro de continuar?" if index == 0 else "Are you sure you want to continue?" if index == 1 else "Êtes-vous sûr de vouloir continuer?")
    msg.setInformativeText(descripcion)
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.setDefaultButton(QMessageBox.No)
    result = msg.exec_()
    return result == QMessageBox.Yes


def words() -> tuple:
    save = ("Guardar", "Save", "Sauvegarder")
    run = ("Ejecutar", "Run", "Exécuter")
    help_ = ("Ayuda 🆘", "Help 🆘", "Aide 🆘")
    clear = ("Limpiar", "Clear", "Claire")
    open_ = ("Abir", "Open", "Ouvrir")
    exit_ = ("Salir", "Exit", "Sortir")
    return (
            save,
            run,
            help_,
            clear,
            open_,
            exit_
    )

def EndCodeLib() -> dict:
    return {
        "tk.Tk()":"\nventana.mainloop()"
    }

def Patrones() -> dict:
    Python_Base = {
        # Español - Condicionales
        r"si (.+?), entonces (.+?)": "if \\1:\n   \\2",
        r"si (.+?), entonces (.+?), sino (.+)": "if \\1:\n   \\2\nelse:\n   \\3",

        # Español - Bucles
        r"repite (.+?) veces (.+)": "for _ in range(\\1):\n   \\2",
        r"mientras (.+?), haz (.+)": "while \\1:\n   \\2",
        r"para cada (.+) en (.+), haz (.+)": "for \\1 in \\2:\n   \\3",

        # Español - Entradas del usuario
        r"pide entrada y guarda en (\S+)": "\\1 = input()",
        r"pide entrada con mensaje \"(.+?)\" y guarda en (\S+)": "\\2 = input('\\1')",

        # Español - Funciones
        r"definir función (\S+)\((.*?)\): (.+)": "def \\1(\\2):\n   \\3",
        r"definir función (\S+)\((.*?)\)": "def \\1(\\2):\n   pass",

        # Español - Otras instrucciones
        r"guarda (.+?) en (\S+)": "\\2 = \\1",
        r"guarda conjunto (.+?) en (\S+)": "\\2 = [\\1]",
        r"suma (.+?) con (.+?) en (\S+)": "\\3 = \\1 + \\2",
        r"sumale (.+?) a (\S+)": "\\2 += \\1",
        r"resta (.+?) con (.+?) en (\S+)": "\\3 = \\1 - \\2",
        r"multiplica (.+?) con (.+?) en (\S+)": "\\3 = \\1 * \\2",
        r"divide (.+?) con (.+?) en (\S+)": "\\3 = \\1 / \\2",
        r"eleva (.+?) con (.+?) en (\S+)": "\\3 = \\1 ** \\2",
        r"radica (.+?) con (.+?) en (\S+)": "\\1 ** (1/\\2)",
        r"concatena (.+?) con (.+?) en (\S+)": '\\3 = \\1 + \\2',
        r"imprime variable (.+)": "print(\\1)",
        r"imprime (.+)": 'print("\\1")',

        # Inglés - Condicionales
        r"if (.+?), then (.+?)": "if \\1:\n   \\2",
        r"if (.+?), then (.+?), else (.+)": "if \\1:\n   \\2\nelse:\n   \\3",

        # Inglés - Bucles
        r"repeat (.+?) times (.+)": "for _ in range(\\1):\n   \\2",
        r"while (.+?), do (.+)": "while \\1:\n   \\2",
        r"for each (.+) in (.+), do (.+)": "for \\1 in \\2:\n   \\3",

        # Inglés - Entradas del usuario
        r"ask for input and save in (\S+)": "\\1 = input()",
        r"ask for input with message \"(.+?)\" and save in (\S+)": "\\2 = input('\\1')",

        # Inglés - Funciones
        r"define function (\S+)\((.*?)\): (.+)": "def \\1(\\2):\n   \\3",
        r"define function (\S+)\((.*?)\)": "def \\1(\\2):\n   pass",

        # Inglés - Otras instrucciones
        r"save (.+?) in (\S+)": "\\2 = \\1",
        r"save set (.+?) in (\S+)": "\\2 = [\\1]",
        r"add (.+?) to (.+?) in (\S+)": "\\3 = \\1 + \\2",
        r"increment (.+?) by (\S+)": "\\2 += \\1",
        r"subtract (.+?) from (.+?) in (\S+)": "\\3 = \\1 - \\2",
        r"multiply (.+?) with (.+?) in (\S+)": "\\3 = \\1 * \\2",
        r"divide (.+?) by (.+?) in (\S+)": "\\3 = \\1 / \\2",
        r"power (.+?) to (.+?) in (\S+)": "\\3 = \\1 ** \\2",
        r"root (.+?) by (.+?) in (\S+)": "\\1 ** (1/\\2)",
        r"concatenate (.+?) with (.+?) in (\S+)": '\\3 = \\1 + \\2',
        r"print variable (.+)": "print(\\1)",
        r"print (.+)": 'print("\\1")',

        # Francés - Condicionales
        r"si (.+?), alors (.+?)": "if \\1:\n   \\2",
        r"si (.+?), alors (.+?), sinon (.+)": "if \\1:\n   \\2\nelse:\n   \\3",

        # Francés - Bucles
        r"répète (.+?) fois (.+)": "for _ in range(\\1):\n   \\2",
        r"tant que (.+?), fais (.+)": "while \\1:\n   \\2",
        r"pour chaque (.+) dans (.+), fais (.+)": "for \\1 in \\2:\n   \\3",

        # Francés - Entradas del usuario
        r"demande une entrée et sauvegarde dans (\S+)": "\\1 = input()",
        r"demande une entrée avec le message \"(.+?)\" et sauvegarde dans (\S+)": "\\2 = input('\\1')",

        # Francés - Funciones
        r"définir fonction (\S+)\((.*?)\): (.+)": "def \\1(\\2):\n   \\3",
        r"définir fonction (\S+)\((.*?)\)": "def \\1(\\2):\n   pass",

        # Francés - Otras instrucciones
        r"sauvegarde (.+?) dans (\S+)": "\\2 = \\1",
        r"sauvegarde ensemble (.+?) dans (\S+)": "\\2 = [\\1]",
        r"ajoute (.+?) à (.+?) dans (\S+)": "\\3 = \\1 + \\2",
        r"ajoute (.+?) à (\S+)": "\\2 += \\1",
        r"soustraire (.+?) de (.+?) dans (\S+)": "\\3 = \\1 - \\2",
        r"multiplie (.+?) avec (.+?) dans (\S+)": "\\3 = \\1 * \\2",
        r"divise (.+?) par (.+?) dans (\S+)": "\\3 = \\1 / \\2",
        r"puissance (.+?) à (.+?) dans (\S+)": "\\3 = \\1 ** \\2",
        r"racine (.+?) par (.+?) dans (\S+)": "\\1 ** (1/\\2)",
        r"concatène (.+?) avec (.+?) dans (\S+)": '\\3 = \\1 + \\2',
        r"imprime variable (.+)": "print(\\1)",
        r"imprime (.+)": 'print("\\1")',
    }
    Tkinter = {
        # Español
            # Creación de ventana
        r"inicia la ventana": """
        import tkinter as tk

        root = tk.Tk()
        """,
            # Configuración de ventana
        r"resolucion de (.+)x(.+)": 'root.geometry("\\1x\\2")',
            # Creación de widgets
        r"crea un boton llamado (\S+) con (.+) dentro conectado a la funcion (\S+)": '\\1 = tk.Button(root, text="\\2")',
        r"crea una etiqueta llamada (\S+) con (.+) dentro": '\\1 = tk.Label(root, text="\\2")',
        r"crea una entrada de texto llamada (\S+)": '\\1 = tk.Entry(root)',
            # Posicionamiento de Widgets
        r"coloca el widget llamado (\S+) la columna (\S+) de la fila (\S+)": '\\1.grid(column=\\2, row=\\3)',
        r"coloca el widget llamado (\S+) hay": '\\1.pack()',

        # English
            # Window creation
        r"initialize the window": """
        import tkinter as tk

        root = tk.Tk()
        """,
            # Window configuration
        r"resolution of (.+)x(.+)": 'root.geometry("\\1x\\2")',
            # Widget creation
        r"create a button named (\S+) with (.+) inside connected to the function (\S+)": '\\1 = tk.Button(root, text="\\2", command=\\3)',
        r"create a label called (\S+) with (.+) inside": '\\1 = tk.Label(root, text="\\2")',
        r"create a text entry called (\S+)": '\\1 = tk.Entry(root)',
            # Widget positioning
        r"place the widget called (\S+) at column (\S+) row (\S+)": '\\1.grid(column=\\2, row=\\3)',
        r"place the widget called (\S+) here": '\\1.pack()',

        # Français
            # Création de fenêtre
        r"initialiser la fenêtre": """
        import tkinter as tk

        root = tk.Tk()
        """,
            # Configuration de fenêtre
        r"résolution de (.+)x(.+)": 'root.geometry("\\1x\\2")',
            # Création de widgets
        r"crée un bouton nommé (\S+) avec (.+) à l'intérieur connecté à la fonction (\S+)": '\\1 = tk.Button(root, text="\\2", command=\\3)',
        r"crée une étiquette appelée (\S+) avec (.+) à l'intérieur": '\\1 = tk.Label(root, text="\\2")',
        r"crée une entrée de texte appelée (\S+)": '\\1 = tk.Entry(root)',
            # Positionnement de Widgets
        r"place le widget appelé (\S+) à la colonne (\S+) rangée (\S+)": '\\1.grid(column=\\2, row=\\3)',
        r"place le widget appelé (\S+) ici": '\\1.pack()'
    }

    return Python_Base | Tkinter


def Operadores() -> dict:
    Operadores_Generales = {
        # Español
        r" es igual a ": " == ",
        r" es diferente de ": " != ",
        r" es mayor que ": " > ",
        r" es menor que ": " < ",
        r" es mayor o igual que ": " >= ",
        r" es menor o igual que ": " <= ",

        # Inglés
        r" is equal to ": " == ",
        r" is not equal to ": " != ",
        r" is greater than ": " > ",
        r" is less than ": " < ",
        r" is greater or equal to ": " >= ",
        r" is less or equal to ": " <= ",

        # Francés
        r" est égal à ": " == ",
        r" est différent de ": " != ",
        r" est supérieur à ": " > ",
        r" est inférieur à ": " < ",
        r" est supérieur ou égal à ": " >= ",
        r" est inférieur ou égal à ": " <= ",
    }

    Listas = {
        # Español
        r"elemento numero (.+?) de la lista (.+)": "\\2[\\1]",

        # Inglés
        r"element number (.+?) in the list (.+)": "\\2[\\1]",

        # Francés
        r"élément numéro (.+?) dans la liste (.+)": "\\2[\\1]",
    }
    return Operadores_Generales | Listas
