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


def Patrones():
    return {
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


def Operadores():
    return {
        # Español
        r" es igual a ": " == ",
        r" es diferente de ": " != ",
        r" es mayor que ": " > ",
        r" es menor que ": " < ",
        r" es mayor o igual que ": " >= ",
        r" es menor o igual que ": " <= ",
        r"elemento numero (.+?) de la lista (.+)": "\\2[\\1]",

        # Inglés
        r" is equal to ": " == ",
        r" is not equal to ": " != ",
        r" is greater than ": " > ",
        r" is less than ": " < ",
        r" is greater or equal to ": " >= ",
        r" is less or equal to ": " <= ",
        r"element number (.+?) in the list (.+)": "\\2[\\1]",

        # Francés
        r" est égal à ": " == ",
        r" est différent de ": " != ",
        r" est supérieur à ": " > ",
        r" est inférieur à ": " < ",
        r" est supérieur ou égal à ": " >= ",
        r" est inférieur ou égal à ": " <= ",
        r"élément numéro (.+?) dans la liste (.+)": "\\2[\\1]",
    }
