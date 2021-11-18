import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/AddDoctor.ui", self)
        self.setWindowTitle("J-Medic: Registrar Medicos")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.botonGuardar.clicked.connect(self.validar_datos)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.inputNombre.textChanged.connect(self.validar_nombre)
        self.inputAp.textChanged.connect(self.validar_apellidoP)
        self.inputAm.textChanged.connect(self.validar_apellidoM)
        self.inputTelefono.textChanged.connect(self.validar_telefono)
        self.inputCedula.textChanged.connect(self.validar_cedula)
        self.inputContra.textChanged.connect(self.validar_password)
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

    def validar_apellidoP(self):
        apellido = self.inputAp.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", apellido, re.I)
        if apellido == "":
            self.inputAp.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputAp.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputAp.setStyleSheet("border: 2px solid green;")
            return True

    def validar_apellidoM(self):
        apellido = self.inputAm.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", apellido, re.I)
        if apellido == "":
            self.inputAm.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputAm.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputAm.setStyleSheet("border: 2px solid green;")
            return True

    def validar_cedula(self):
        cedula = self.inputCedula.text()
        validar = re.match("^\d{10}$", cedula, re.I)
        if cedula == "":
            self.inputCedula.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputCedula.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputCedula.setStyleSheet("border: 2px solid green;")
            return True

    def validar_telefono(self):
        telefono = self.inputTelefono.text()
        validar = re.match("^\d{10}$", telefono, re.I)
        if telefono == "":
            self.inputTelefono.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputTelefono.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputTelefono.setStyleSheet("border: 2px solid green;")
            return True

    def validar_turno(self):
        turno = self.inputTurno.currentText()
        if turno == "":
            return False
        else:
            return True

    def validar_password(self):
        password = self.inputUsuario.text()
        password2 = self.inputContra.text()
        if password != password2:
            self.inputContra.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputContra.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos(self):
        if self.validar_nombre() and self.validar_cedula() and self.validar_apellidoP() and self.validar_turno() and self.validar_apellidoM() and self.validar_telefono() and self.validar_password():
            QMessageBox.information(
                    self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            self.switch()
        else:
           QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def estilos(self):
        estilo = """
        *{
            font-family:century gothic;
            font-size:24px;
        }

        QWidget{
            background-image: url(Imagenes/pru.jpg);
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
        #inputNombre{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputAp{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputAm{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputCedula{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputTelefono{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputUsuario{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputContra{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }

        """
        return estilo

    def switch(self):
        self.switch_window.emit()