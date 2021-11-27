import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import Modulos.db_consultas as consultas

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/BuscarConsulta.ui", self)
        self.setWindowTitle("J-Medic: Buscar Medico")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.botonBuscar.clicked.connect(self.switch)
        self.buscarIdConsulta.clicked.connect(self.validar_datos_idc)
        self.buscarIdMedico.clicked.connect(self.validar_datos_id)
        self.buscarIdPaciente.clicked.connect(self.validar_datos)
        self.botonBuscarFecha.clicked.connect(self.validar_datos_3)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.InputIdConsulta.textChanged.connect(self.validar_id_consulta)
        self.InputIdMedico.textChanged.connect(self.validar_id_medico)
        self.InputIdPaciente.textChanged.connect(self.validar_id_paciente)
        #self.inputAp.textChanged.connect(self.validar_apellidoP)
        pass


    def validar_id_consulta(self):
        id_consulta = self.InputIdConsulta.text()
        validar = re.match("^\d{1,}$", id_consulta, re.I)
        if id_consulta == "":
            self.InputIdConsulta.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.InputIdConsulta.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.InputIdConsulta.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_idc(self):
        if self.validar_id_consulta():
            result=consultas.buscar_consulta_id(int(self.InputIdConsulta.text()))
            print (result)

            ayuda = result

            try:
                self.TablaConsultas.setItem(0 , 0, QTableWidgetItem(str(ayuda[0])))
                self.TablaConsultas.setItem(0 , 1, QTableWidgetItem(ayuda[1]))
                self.TablaConsultas.setItem(0 , 2, QTableWidgetItem(str(ayuda[2])))
                self.TablaConsultas.setItem(0 , 3, QTableWidgetItem(ayuda[3]))
                self.TablaConsultas.setItem(0 , 4, QTableWidgetItem(ayuda[4]))
                self.TablaConsultas.setItem(0 , 5, QTableWidgetItem(str(ayuda[5])))
                self.TablaConsultas.setItem(0 , 6, QTableWidgetItem(str(ayuda[6])))
                self.TablaConsultas.setItem(0 , 7, QTableWidgetItem(str(ayuda[7])))
                self.TablaConsultas.setItem(0 , 8, QTableWidgetItem(ayuda[8]))
                self.TablaConsultas.setItem(0 , 9, QTableWidgetItem(ayuda[9]))
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            #QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            #s¿self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def validar_id_medico(self):
        id_medico = self.InputIdMedico.text()
        validar = re.match("^\d{1,}$", id_medico, re.I)
        if id_medico == "":
            self.InputIdMedico.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.InputIdMedico.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.InputIdMedico.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_id(self):
        if self.validar_id_medico():
            result= consultas.buscar_consulta_id_medico(int(self.InputIdMedico.text()))
            print (result)
            ayuda = result

            try:
                if ayuda:
                    contador = 0
                    for elements in ayuda:
                        self.TablaConsultas.setItem(contador , 0, QTableWidgetItem(str(ayuda[contador][0])))
                        self.TablaConsultas.setItem(contador , 1, QTableWidgetItem(ayuda[contador][1]))
                        self.TablaConsultas.setItem(contador , 2, QTableWidgetItem(str(ayuda[contador][2])))
                        self.TablaConsultas.setItem(contador , 3, QTableWidgetItem(ayuda[contador][3]))
                        self.TablaConsultas.setItem(contador , 4, QTableWidgetItem(ayuda[contador][4]))
                        self.TablaConsultas.setItem(contador , 5, QTableWidgetItem(str(ayuda[contador][5])))
                        self.TablaConsultas.setItem(contador , 6, QTableWidgetItem(str(ayuda[contador][6])))
                        self.TablaConsultas.setItem(contador , 7, QTableWidgetItem(str(ayuda[contador][7])))
                        self.TablaConsultas.setItem(contador , 8, QTableWidgetItem(ayuda[contador][8]))
                        self.TablaConsultas.setItem(contador , 9, QTableWidgetItem(ayuda[contador][9]))
                        contador+=1
                else:
                    QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

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

    def validar_datos(self):
        if self.validar_id_paciente():
            result= consultas.buscar_consulta_id_paciente(int(self.InputIdPaciente.text()))
            print (result)
            ayuda = result

            try:
                if ayuda:
                    contador = 0
                    for elements in ayuda:
                        self.TablaConsultas.setItem(contador , 0, QTableWidgetItem(str(ayuda[contador][0])))
                        self.TablaConsultas.setItem(contador , 1, QTableWidgetItem(ayuda[contador][1]))
                        self.TablaConsultas.setItem(contador , 2, QTableWidgetItem(str(ayuda[contador][2])))
                        self.TablaConsultas.setItem(contador , 3, QTableWidgetItem(ayuda[contador][3]))
                        self.TablaConsultas.setItem(contador , 4, QTableWidgetItem(ayuda[contador][4]))
                        self.TablaConsultas.setItem(contador , 5, QTableWidgetItem(str(ayuda[contador][5])))
                        self.TablaConsultas.setItem(contador , 6, QTableWidgetItem(str(ayuda[contador][6])))
                        self.TablaConsultas.setItem(contador , 7, QTableWidgetItem(str(ayuda[contador][7])))
                        self.TablaConsultas.setItem(contador , 8, QTableWidgetItem(ayuda[contador][8]))
                        self.TablaConsultas.setItem(contador , 9, QTableWidgetItem(ayuda[contador][9]))
                        contador+=1
                else:
                    QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)


    def validar_fecha(self):
        anio = self.inputA.currentText()
        mes = self.inputM.currentText()
        dia = self.inputD.currentText()
        cont = 0
        if anio == "":
            cont+=1

        if mes == "":
            cont+=1

        if dia == "":
            cont+=1

        fecha=str(anio+mes+dia)
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
            fecha=str(anio+mes+dia)     
            ayuda= consultas.buscar_consulta_fecha(fecha)
            print(ayuda)

            try:
                if ayuda:
                    contador = 0
                    for elements in ayuda:
                        self.TablaConsultas.setItem(contador , 0, QTableWidgetItem(str(ayuda[contador][0])))
                        self.TablaConsultas.setItem(contador , 1, QTableWidgetItem(ayuda[contador][1]))
                        self.TablaConsultas.setItem(contador , 2, QTableWidgetItem(str(ayuda[contador][2])))
                        self.TablaConsultas.setItem(contador , 3, QTableWidgetItem(ayuda[contador][3]))
                        self.TablaConsultas.setItem(contador , 4, QTableWidgetItem(ayuda[contador][4]))
                        self.TablaConsultas.setItem(contador , 5, QTableWidgetItem(str(ayuda[contador][5])))
                        self.TablaConsultas.setItem(contador , 6, QTableWidgetItem(str(ayuda[contador][6])))
                        self.TablaConsultas.setItem(contador , 7, QTableWidgetItem(str(ayuda[contador][7])))
                        self.TablaConsultas.setItem(contador , 8, QTableWidgetItem(ayuda[contador][8]))
                        self.TablaConsultas.setItem(contador , 9, QTableWidgetItem(ayuda[contador][9]))
                        contador+=1
                else:
                    QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
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
        #InputIdConsulta{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #InputIdPaciente{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #InputIdMedico{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }

        """
        return estilo

    def switch(self):
        self.switch_window.emit()