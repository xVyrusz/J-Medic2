import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import Modulos.db_citas as cita

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/BuscarCita.ui", self)
        self.setWindowTitle("J-Medic: Buscar Medico")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.BuscarIdCita.clicked.connect(self.validar_datos)
        self.BuscarIdPaciente.clicked.connect(self.validar_datos_2)
        self.BuscarFecha.clicked.connect(self.validar_datos_3)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.InputIdCita.textChanged.connect(self.validar_id_cita)
        self.InputIdPaciente.textChanged.connect(self.validar_id_paciente)
        pass

    def validar_id_cita(self):
        id_cita = self.InputIdCita.text()
        validar = re.match("^\d{1,}$", id_cita, re.I)
        if id_cita == "":
            self.InputIdCita.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.InputIdCita.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.InputIdCita.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos(self):
        if self.validar_id_cita():
            result= cita.buscar_cita_idcita(int(self.InputIdCita.text()))
            print (result)
            ayuda = result
            try:
                self.tablaCita.setItem(0 , 0, QTableWidgetItem(str(ayuda[0])))
                self.tablaCita.setItem(0 , 1, QTableWidgetItem(str(ayuda[1])))
                self.tablaCita.setItem(0 , 2, QTableWidgetItem(ayuda[2]))
                self.tablaCita.setItem(0 , 3, QTableWidgetItem(ayuda[3]))
                self.tablaCita.setItem(0 , 4, QTableWidgetItem(ayuda[4]))
                self.tablaCita.setItem(0 , 5, QTableWidgetItem(str(ayuda[5])))
                QMessageBox.information(
                self,"Correcto", "Busqueda exitosa", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
        else:
           QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def validar_id_paciente(self):
        id_paciente = self.InputIdPaciente.text()
        validar = re.match("^\d{1,}$", id_paciente, re.I)
        if id_paciente == "":
            self.InputIdPaciente.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.InputIdPaciente.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.InputIdPaciente.setStyleSheet("border: 2px solid green;")
            return True
    def validar_datos_2(self):
        if self.validar_id_paciente():
            ayuda2= cita.buscar_cita_idpaciente(int(self.InputIdPaciente.text()))
            print(ayuda2)
            try:
                if ayuda2:
                    contador = 0
                    for elements in ayuda2:
                        self.tablaCita.setItem(
                            contador, 0, QTableWidgetItem(str(ayuda2[contador][0])))
                        self.tablaCita.setItem(
                            contador, 1, QTableWidgetItem(str(ayuda2[contador][1])))
                        self.tablaCita.setItem(
                            contador, 2, QTableWidgetItem(ayuda2[contador][2]))
                        self.tablaCita.setItem(
                            contador, 3, QTableWidgetItem(ayuda2[contador][3]))
                        self.tablaCita.setItem(
                            contador, 4, QTableWidgetItem(ayuda2[contador][4]))
                        self.tablaCita.setItem(
                            contador, 5, QTableWidgetItem(str(ayuda2[contador][5])))
                        contador += 1
                        QMessageBox.information(
                        self,"Correcto", "Busqueda exitosa", QMessageBox.Discard)
                else:
                     QMessageBox.warning(
                        self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
        else:
           QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

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

    def validar_datos_3(self):
        if self.validar_fecha():
            anio = self.inputA.currentText()
            mes = self.inputM.currentText()
            dia = self.inputD.currentText()
            hora = self.inputH.currentText()
            minutos = self.inputMin.currentText()     
            fecha=str(anio+mes+dia+hora+minutos)     
            ayuda2= cita.buscar_cita_fecha(fecha)
            print(fecha)
            print(ayuda2)
            try:
                if ayuda2:
                    contador = 0
                    for elements in ayuda2:
                        self.tablaCita.setItem(
                            contador, 0, QTableWidgetItem(str(ayuda2[contador][0])))
                        self.tablaCita.setItem(
                            contador, 1, QTableWidgetItem(str(ayuda2[contador][1])))
                        self.tablaCita.setItem(
                            contador, 2, QTableWidgetItem(ayuda2[contador][2]))
                        self.tablaCita.setItem(
                            contador, 3, QTableWidgetItem(ayuda2[contador][3]))
                        self.tablaCita.setItem(
                            contador, 4, QTableWidgetItem(ayuda2[contador][4]))
                        self.tablaCita.setItem(
                            contador, 5, QTableWidgetItem(str(ayuda2[contador][5])))
                        contador += 1
                else:
                     QMessageBox.warning(
                        self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
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
        #InputIdCita{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #InputIdPaciente{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }

        """
        return estilo

    def switch(self):
        self.switch_window.emit()