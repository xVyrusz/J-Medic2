import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import Modulos.db_pacientes as pacientes

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/AddPaciente.ui", self)
        self.setWindowTitle("J-Medic: Menu 1")
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
        self.inputAlergias.textChanged.connect(self.validar_alergia)
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

    def validar_sexo(self):
        sexo = self.inputSexo.currentText()
        if sexo == "":
            return False
        else:
            return True

    def validar_peso(self):
        pesok = self.inputKg.currentText()
        pesog = self.inputG.currentText()
        cont = 0
        if pesog == "":
            cont += 1

        if pesok == "":
            cont += 1

        peso = str(pesok+pesog)
        if cont > 0:
            peso = ""

        if peso == "":
            return False
        else:
            return True

    def validar_estatura(self):
        estaturam = self.inputM.currentText()
        estaturacm = self.inputCm.currentText()
        cont = 0
        if estaturacm == "":
            cont += 1

        if estaturam == "":
            cont += 1

        estatura = str(estaturam + estaturacm)
        if cont > 0:
            estatura = ""

        if estatura == "":
            return False
        else:
            return True

    def validar_anios(self):
        anios = self.inputEdad.currentText()
        if anios == "":
            return False
        else:
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

    def validar_sangre(self):
        sangre = self.inputTipoSangre.currentText()
        if sangre == "":
            return False
        else:
            return True

    def validar_alergia(self):
        alergias = self.inputAlergias.toPlainText()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", alergias, re.I)
        if alergias == "":
            self.inputAlergias.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputAlergias.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputAlergias.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos(self):
        if self.validar_nombre() and self.validar_sexo() and self.validar_apellidoP() and self.validar_peso() and self.validar_apellidoM() and self.validar_estatura() and self.validar_telefono() and self.validar_anios() and self.validar_alergia() and self.validar_sangre():
            sangre = 0
            if self.inputTipoSangre.currentText() == 'A+':
                sangre = 1
            elif self.inputTipoSangre.currentText() == 'A-':
                sangre = 2
            elif self.inputTipoSangre.currentText() == 'B+':
                sangre = 3
            elif self.inputTipoSangre.currentText() == 'B-':
                sangre = 4
            elif self.inputTipoSangre.currentText() == 'O+':
                sangre = 5
            elif self.inputTipoSangre.currentText() == 'O-':
                sangre = 6
            elif self.inputTipoSangre.currentText() == 'AB+':
                sangre = 7
            elif self.inputTipoSangre.currentText() == 'AB-':
                sangre = 8
            pesok = self.inputKg.currentText()
            pesog = self.inputG.currentText()
            peso = str(pesok+pesog)
            estaturam = self.inputM.currentText()
            estaturacm = self.inputCm.currentText()
            estatura = str(estaturam + estaturacm)

            result = pacientes.insertar_pacientes(self.inputNombre.text(), self.inputAp.text(), self.inputAm.text(), self.inputSexo.currentText()
            , peso, estatura, self.inputEdad.currentText(), self.inputTelefono.text(), self.inputAlergias.toPlainText(), sangre)
            if result == 1:
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
        #inputTelefono{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputAlergias{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }

        """
        return estilo

    def switch(self):
        self.switch_window.emit()