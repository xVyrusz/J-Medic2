from PyQt5 import uic, QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()
    switch_window6 = QtCore.pyqtSignal()
    switch_window7 = QtCore.pyqtSignal()
    switch_window8 = QtCore.pyqtSignal()
    switch_window9 = QtCore.pyqtSignal()
    switch_window10 = QtCore.pyqtSignal()


    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Menu1.ui", self)
        self.setWindowTitle("J-Medic: Menu 1")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.addMedico.clicked.connect(self.switch)
        self.addPaciente.clicked.connect(self.switch2)
        self.addConsulta.clicked.connect(self.switch3)
        self.addCita.clicked.connect(self.switch4)
        self.buscarMedico.clicked.connect(self.switch5)
        self.buscarPaciente.clicked.connect(self.switch6)
        self.buscarConsulta.clicked.connect(self.switch7)
        self.buscarCita.clicked.connect(self.switch8)
        self.actionCerrar_Sesion.setShortcut("Ctrl+R")
        self.actionCerrar_Sesion.triggered.connect(self.switch10)

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
        
    def switch10(self):
        self.switch_window10.emit()

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
        background-image: url(Imagenes/addDoctor.png);
        }
        #label_12{
        background-image: url(Imagenes/addPx.png);
        }
        #label_14{
        background-image: url(Imagenes/addConsulta.png);
        }
        #label_15{
        background-image: url(Imagenes/addCita.png);
        }
        #label_16{
        image: url(Imagenes/searchDoctor.png);
        }
        #label_17{
        background-image: url(Imagenes/searchPx.png);
        }
        #label_18{
        background-image: url(Imagenes/searchCita.png);
        }
        #label_19{
        background-image: url(Imagenes/searchConsulta.png);
        }
        #label_20{
        background-image: url(Imagenes/right.png);
        }
        """
        return estilo