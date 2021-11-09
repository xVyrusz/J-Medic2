import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/BuscarConsulta.ui", self)
        self.setWindowTitle("J-Medic: Buscar Medico")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.botonBuscar.clicked.connect(self.switch)
        self.buscarIdConsulta.clicked.connect(self.switch)
        self.buscarIdMedico.clicked.connect(self.switch)
        self.buscarIdPaciente.clicked.connect(self.switch)
        self.botonBuscarFecha.clicked.connect(self.switch)
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
        #inputIdConsulta{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputIdPaciente{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputIdMedico{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }

        """
        return estilo

    def switch(self):
        self.switch_window.emit()