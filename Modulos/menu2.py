from PyQt5 import uic, QtCore, QtWidgets


class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()
    switch_window6 = QtCore.pyqtSignal()
    switch_window7 = QtCore.pyqtSignal()
    switch_window8 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Menu2.ui", self)
        self.setWindowTitle("J-Medic: Menu 2")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.editarPaciente.clicked.connect(self.switch)
        self.editarMedico.clicked.connect(self.switch2)
        self.editarConsulta.clicked.connect(self.switch3)
        self.editarCita.clicked.connect(self.switch4)
        self.eliminarConsulta.clicked.connect(self.switch5)
        self.eliminarCita.clicked.connect(self.switch6)
        self.regresar.clicked.connect(self.switch7)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch8)

    def switch(self):
        self.switch_window.emit()

    def switch2(self):
        self.switch_window2.emit()

    def switch3(self):
        self.switch_window3.emit()

    def switch4(self):
        self.switch_window4.emit()

    def switch5(self):
        self.switch_window5.emit()

    def switch6(self):
        self.switch_window6.emit()

    def switch7(self):
        self.switch_window7.emit()

    def switch8(self):
        self.switch_window8.emit()

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
        #label_13{
        background-image: url(Imagenes/editDoctor.png);
        }
        #label_12{
        background-image: url(Imagenes/editPx.png);
        }
        #label_19
        {
        background-image: url(Imagenes/editConsulta.png);
        }
        #label_15{
        image: url(Imagenes/editCita.png);
        }
        #label_16{
        image: url(Imagenes/deleteConsulta.png);
        }
        #label_17{
        background-image: url(Imagenes/deleteCita.png);
        }
        #label_18{
        background-image: url(Imagenes/left.png);
        }
        """
        return estilo