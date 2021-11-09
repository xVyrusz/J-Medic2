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
        self.generarIdConsulta.clicked.connect(self.switch)
        self.botonFecha.clicked.connect(self.switch)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)

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