def stylesheet():

    return """
/* Ventana principal */
QWidget {
    background-color: #2E2E2E; /* Gris oscuro */
    color: #00FF00; /* Verde neón */
    font-family: Arial, Helvetica, sans-serif;
    font-size: 14px;
}

/* Botones */
QPushButton {
    background-color: #3E3E3E; /* Gris medio */
    color: #00FF00;
    border: 2px solid #000000; /* Borde negro */
    border-radius: 10px;
    padding: 5px;
}

QPushButton:hover {
    background-color: #00FF00;
    color: #2E2E2E;
}

QPushButton:pressed {
    background-color: #005500;
}

/* Botones de radio */
QRadioButton {
    background-color: #2E2E2E;
    color: #00FF00;
}

QRadioButton::indicator {
    border: 2px solid #000000;
    border-radius: 10px;
    background-color: #3E3E3E;
}

QRadioButton::indicator:checked {
    background-color: #00FF00;
}

/* Cuadros de texto */
QLineEdit {
    background-color: #1E1E1E;
    color: #00FF00;
    border: 2px solid #000000;
    border-radius: 5px;
    padding: 5px;
}

/* Combobox */
QComboBox {
    background-color: #1E1E1E;
    color: #00FF00;
    border: 2px solid #000000;
    border-radius: 5px;
    padding: 5px;
}

QComboBox::drop-down {
    border: none;
}

QComboBox QAbstractItemView {
    background-color: #2E2E2E;
    color: #00FF00;
    selection-background-color: #00FF00;
    selection-color: #2E2E2E;
}

/* Sliders */
QSlider::groove:horizontal {
    border: 2px solid #000000;
    height: 8px;
    background: #3E3E3E;
    border-radius: 4px;
}

QSlider::handle:horizontal {
    background: #00FF00;
    border: 2px solid #000000;
    width: 18px;
    height: 18px;
    margin: -5px 0;
    border-radius: 9px;
}

QSlider::groove:vertical {
    border: 2px solid #000000;
    width: 8px;
    background: #3E3E3E;
    border-radius: 4px;
}

QSlider::handle:vertical {
    background: #00FF00;
    border: 2px solid #000000;
    width: 18px;
    height: 18px;
    margin: 0 -5px;
    border-radius: 9px;
}

/* Listas y tablas */
QListView, QTableView {
    background-color: #2E2E2E;
    color: #00FF00;
    border: 2px solid #000000;
    border-radius: 5px;
    gridline-color: #3E3E3E;
}

QHeaderView::section {
    background-color: #3E3E3E;
    color: #00FF00;
    border: 1px solid #000000;
    padding: 5px;
}
"""

def exitButton():
    return """
    font-size: 18pt;
    color: rgb(200,65,65);
    """
    
def titleLabel():
    return """
    color: #ffffff;
    font-size: 25px;
    font-weight: bold
    """
    
def sendButton():
    return """ 
        border: 4px solid #00FFFF; /* Azul neón */
        border-radius: 15px;       /* Bordes redondeados */
    """