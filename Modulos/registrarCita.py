import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import Modulos.db_citas  as cita

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/AddCita.ui", self)
        self.setWindowTitle("J-Medic: Registrar Cita")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.agendarCita.clicked.connect(self.validar_datos)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.inputIdPaciente.textChanged.connect(self.validar_id_paciente)
        #self.input_fecha.textChanged.connect(self.validar_fecha)
        pass

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

    def validar_fecha(self):
        anio = self.inputA.currentText()
        mes = self.inputM.currentText()
        dia = self.inputD.currentText()
        hora = self.inputH.currentText()
        minutos = self.inputMin.currentText()
        cont = 0
        if anio == "":
            cont+=1

        if mes == "":
            cont+=1

        if dia == "":
            cont+=1

        if hora == "":
            cont+=1

        if minutos == "":
            cont+=1

        fecha=str(anio+mes+dia+hora+minutos)
        if cont>0:
            fecha=""
        
        if fecha == "":
            return False
        else:
            return True

    def validar_datos(self):
        if self.validar_id_paciente() and self.validar_fecha():
            anio = self.inputA.currentText()
            mes = self.inputM.currentText()
            dia = self.inputD.currentText()
            hora = self.inputH.currentText()
            minutos = self.inputMin.currentText()     
            fecha=str(anio+mes+dia+hora+minutos)     
            result=cita.insertar_cita(self.inputIdPaciente.text(),fecha)
            if result == 1:
                result2=cita.mostrar_citas()
                ayuda = result2
                try:
                    if ayuda:
                        contador = 0
                        for elements in ayuda:
                            self.tablaCitas.setItem(contador , 0, QTableWidgetItem(str(ayuda[contador][0])))
                            self.tablaCitas.setItem(contador , 1, QTableWidgetItem(str(ayuda[contador][1])))
                            self.tablaCitas.setItem(contador , 2, QTableWidgetItem(str(ayuda[contador][2])))
                            self.tablaCitas.setItem(contador , 3, QTableWidgetItem(ayuda[contador][3]))
                            self.tablaCitas.setItem(contador , 4, QTableWidgetItem(ayuda[contador][4]))
                            self.tablaCitas.setItem(contador , 5, QTableWidgetItem(str(ayuda[contador][5])))
                            contador+=1            
                    else:
                        QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)
                except:
                    QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

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
        #inputIdPaciente{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }

        """
        return estilo

    def switch(self):
        self.switch_window.emit()