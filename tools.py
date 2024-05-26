from PyQt5.QtGui import QTextCursor, QTextCharFormat, QFont
from PyQt5.QtWidgets import  QMessageBox
            
def show_error_message(descripcion_del_error):
    # Crear un cuadro de diálogo QMessageBox de tipo Error
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle("Error")
    msg.setText("¡Ha ocurrido un error!")
    msg.setInformativeText(descripcion_del_error)
    msg.exec_() 
    
def show_warning_message(descripcion_de_advertencia):
    # Crear un cuadro de diálogo QMessageBox de tipo Advertencia
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle("Advertencia")
    msg.setText("¡Advertencia!")
    msg.setInformativeText(descripcion_de_advertencia)
    msg.exec_()
    
def show_information_message(descripcion_de_informacion):
    # Crear un cuadro de diálogo QMessageBox de tipo Información
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Información")
    msg.setText("¡Información!")
    msg.setInformativeText(descripcion_de_informacion)
    msg.exec_()
    
def confirmar_mensaje(descripcion):
    # Crear un cuadro de diálogo QMessageBox de tipo Pregunta
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setWindowTitle("Confirmar")
    msg.setText("¿Está seguro de continuar?")
    msg.setInformativeText(descripcion)
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.setDefaultButton(QMessageBox.No)
    result = msg.exec_()
    return result == QMessageBox.Yes

    
def Patrones():
    return {
    # Condicionales
    r"si (.+?), entonces (.+?)": "if \\1:\n    \\2",
    r"si (.+?), entonces (.+?), sino (.+)": "if \\1:\n    \\2\nelse:\n    \\3",

    # Bucles
    r"repite (.+?) veces (.+)": "for _ in range(\\1):\n    \\2",
    r"mientras (.+?), haz (.+)": "while \\1:\n    \\2",
    r"para cada (.+) en (.+), haz (.+)": "for \\1 in \\2:\n    \\3",

    # Otras instrucciones
    r"guarda (.+?) en (\S+)": "\\2 = \\1",
    r"suma (.+?) con (.+?) en (\S+)": "\\3 = \\1 + \\2",
    r"resta (.+?) con (.+?) en (\S+)": "\\3 = \\1 - \\2",
    r"multiplica (.+?) con (.+?) en (\S+)": "\\3 = \\1 * \\2",
    r"divide (.+?) con (.+?) en (\S+)": "\\3 = \\1 / \\2",
    r"eleva (.+?) con (.+?) en (\S+)": "\\3 = \\1 ** \\2",
    r"radica (.+?) con (.+?) en (\S+)": "\\1 ** (1/\\2)",
    r"concatena (.+?) con (.+?) en (\S+)": '\\3 = \\1 + \\2',
    r"imprime variable (.+)": "print(\\1)",
    r"imprime (.+)": 'print("\\1")',
}
    
def Operadores():
    return {
    r" es igual a ": " == ",
    r" es diferente de ": " != ",
    r" es mayor que ": " > ",
    r" es menor que ": " < ",
    r" es mayor o igual que ": " >= ",
    r" es menor o igual que ": " <= ",
}
