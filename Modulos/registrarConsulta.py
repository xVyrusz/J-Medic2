import re
import datetime
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem


class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/AddConsulta.ui", self)
        self.setWindowTitle("J-Medic: Registrar Consulta")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.guardarConsulta.clicked.connect(self.switch)
        self.generarIdConsulta.clicked.connect(self.validar_datos)
        self.botonFecha.clicked.connect(self.seleccionar_fecha)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.inputIdMedico.textChanged.connect(self.validar_id_medico)
        self.inputIdPaciente.textChanged.connect(self.validar_id_paciente)
        #self.inputIdConsulta.textChanged.connect(self.validar_id_consulta)
        pass

    def validar_id_medico(self):
        id_medico = self.inputIdMedico.text()
        validar = re.match("^\d{1,}$", id_medico, re.I)
        if id_medico == "":
            self.inputIdMedico.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputIdMedico.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputIdMedico.setStyleSheet("border: 2px solid green;")
            return True

    def validar_id_paciente(self):
        id_paciente = self.inputIdPaciente.text()
        validar = re.match("^\d{1,}$", id_paciente, re.I)
        if id_paciente == "":
            self.inputIdPaciente.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputIdPaciente.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputIdPaciente.setStyleSheet("border: 2px solid green;")
            return True

    def seleccionar_motivo(self):
        motivo = self.inputMotivoConsulta.currentText()
        if motivo == "":
            return False
        else:
            return True

    def seleccionar_fecha(self):
        fecha_2 = datetime.date.today()
        fecha_3 = str(fecha_2)
        self.FechaAuto.setText(str(fecha_3))
        if fecha_3 == "":
            return False
        else:
            return True

    def validar_datos(self):
        if self.validar_id_medico() and self.validar_id_paciente() and self.seleccionar_motivo() and self.seleccionar_fecha():
            QMessageBox.information(
                    self, "Datos guardados", "Se genero su ID de consulta correctamente", QMessageBox.Discard)
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
        #inputIdMedico{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputIdPaciente{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputIdConsulta{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputDiagnostico{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputPruebasRealizadas{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputTratamiento{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }

        """
        return estilo

    def switch(self):
        self.switch_window.emit()