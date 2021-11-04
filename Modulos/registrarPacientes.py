import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/AddPaciente.ui", self)
        self.setWindowTitle("J-Medic: Menu 1")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.botonGuardar.clicked.connect(self.switch)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.inputNombre.textChanged.connect(self.validar_nombre)
        pass

    def validar_nombre(self):
        nombre = self.inputNombre.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", nombre, re.I)
        if nombre == "":
            self.inputNombre.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputNombre.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputNombre.setStyleSheet("border: 2px solid green;")
            return True

    def estilos(self):
        estilo = """
        *{
            font-family:century gothic;
            font-size:24px;
        }

        QWidget{
            background-image: url(Imagenes/paisaje-cultura-sostenibilidad.jpg);
        }

        QFrame{
            background:rgba(0/0/0/0.8);
            border-radius:15px;
        }

        QPushButton{
            background:#88c7dc;
            color:white;
            border-radius:15px;
        }

        QPushButton:hover{
            color:#333;
            border-radius:15px;
            background:#49ebff;
        }

        QToolButton{
            background:red;
            border-radius:60px;

        }

        QLabel{
            color:white;
            background:transparent;
        }

        QLineEdit{
            background:transparent;
            border:none;
            color:#717072;
            border-bottom:1px solid #717072;
        }
        """
        return estilo

    def switch(self):
        self.switch_window.emit()