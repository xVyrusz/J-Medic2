import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import Modulos.db_medicos as medicos

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/BuscarMedico.ui", self)
        self.setWindowTitle("J-Medic: Buscar Medico")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.botonBuscar.clicked.connect(self.mostrar_medicos_all)
        self.buscarCedula.clicked.connect(self.validar_datos_cedula)
        self.buscarId.clicked.connect(self.validar_datos_id)
        self.buscarNombre.clicked.connect(self.validar_datos_2)
        self.buscarApellido.clicked.connect(self.validar_datos_3)
        self.buscarTurno.clicked.connect(self.validar_datos_4)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.inputCedula.textChanged.connect(self.validar_cedula)
        self.inputIdMedico.textChanged.connect(self.validar_id_medico)
        self.inputNombre.textChanged.connect(self.validar_nombre)
        self.inputAp.textChanged.connect(self.validar_apellidoP)
        self.inputTurno.textChanged.connect(self.validar_turno)
        pass

    def validar_cedula(self):
        cedula = self.inputCedula.text()
        validar = re.match("^\d{7,8}$", cedula, re.I)
        if cedula == "":
            self.inputCedula.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputCedula.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputCedula.setStyleSheet("border: 2px solid green;")
            return True
    def validar_datos_cedula(self):
        if self.validar_cedula():
            result= medicos.buscar_medicos_cedula(int(self.inputCedula.text()))
            print (result)
            ayuda = result
            try:
                self.tablaMedicos.setItem(0 , 0, QTableWidgetItem(str(ayuda[0])))
                self.tablaMedicos.setItem(0 , 1, QTableWidgetItem(ayuda[1]))
                self.tablaMedicos.setItem(0 , 2, QTableWidgetItem(ayuda[2]))
                self.tablaMedicos.setItem(0 , 3, QTableWidgetItem(ayuda[3]))
                self.tablaMedicos.setItem(0 , 4, QTableWidgetItem(ayuda[4]))
                self.tablaMedicos.setItem(0 , 5, QTableWidgetItem(ayuda[5]))
                self.tablaMedicos.setItem(0 , 6, QTableWidgetItem(ayuda[6]))
                QMessageBox.information(
                    self,"Correcto", "Busqueda exitosa", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)          
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

    def validar_datos_id(self):
        if self.validar_id_medico():
            result= medicos.buscar_medicos_id(int(self.inputIdMedico.text()))
            print (result)
            ayuda = result
            try:
                self.tablaMedicos.setItem(0 , 0, QTableWidgetItem(str(ayuda[0])))
                self.tablaMedicos.setItem(0 , 1, QTableWidgetItem(ayuda[1]))
                self.tablaMedicos.setItem(0 , 2, QTableWidgetItem(ayuda[2]))
                self.tablaMedicos.setItem(0 , 3, QTableWidgetItem(ayuda[3]))
                self.tablaMedicos.setItem(0 , 4, QTableWidgetItem(ayuda[4]))
                self.tablaMedicos.setItem(0 , 5, QTableWidgetItem(ayuda[5]))
                self.tablaMedicos.setItem(0 , 6, QTableWidgetItem(ayuda[6]))
                QMessageBox.information(
                    self,"Correcto", "Busqueda exitosa", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

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

    def validar_datos_2(self):
        if self.validar_nombre():
            result= medicos.buscar_medicos_nombre(self.inputNombre.text())
            print (result)
            ayuda2 = result
            try:
                if ayuda2:
                    contador = 0
                    for elements in ayuda2:
                        self.tablaMedicos.setItem(
                            contador, 0, QTableWidgetItem(str(ayuda2[contador][0])))
                        self.tablaMedicos.setItem(
                            contador, 1, QTableWidgetItem(ayuda2[contador][1]))
                        self.tablaMedicos.setItem(
                            contador, 2, QTableWidgetItem(str(ayuda2[contador][2])))
                        self.tablaMedicos.setItem(
                            contador, 3, QTableWidgetItem(ayuda2[contador][3]))
                        self.tablaMedicos.setItem(
                            contador, 4, QTableWidgetItem(ayuda2[contador][4]))
                        self.tablaMedicos.setItem(
                            contador, 5, QTableWidgetItem(str(ayuda2[contador][5])))
                        self.tablaMedicos.setItem(
                            contador, 6, QTableWidgetItem(str(ayuda2[contador][6])))
                        contador += 1 
                        QMessageBox.information(
                            self,"Correcto", "Busqueda exitosa", QMessageBox.Discard) 
                else:
                        QMessageBox.warning(
                            self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                    QMessageBox.warning(
                        self, "Error", "No se ha encontrado nada", QMessageBox.Discard)  


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

    def validar_datos_3(self):
        if self.validar_apellidoP():
            result= medicos.buscar_medicos_apellido(self.inputAp.text())
            print(self.inputAp.text())
            print (result)
            ayuda2 = result
            try:
                if ayuda2:
                    contador = 0
                    for elements in ayuda2:
                        self.tablaMedicos.setItem(
                            contador, 0, QTableWidgetItem(str(ayuda2[contador][0])))
                        self.tablaMedicos.setItem(
                            contador, 1, QTableWidgetItem(ayuda2[contador][1]))
                        self.tablaMedicos.setItem(
                            contador, 2, QTableWidgetItem(str(ayuda2[contador][2])))
                        self.tablaMedicos.setItem(
                            contador, 3, QTableWidgetItem(ayuda2[contador][3]))
                        self.tablaMedicos.setItem(
                            contador, 4, QTableWidgetItem(ayuda2[contador][4]))
                        self.tablaMedicos.setItem(
                            contador, 5, QTableWidgetItem(str(ayuda2[contador][5])))
                        self.tablaMedicos.setItem(
                            contador, 6, QTableWidgetItem(str(ayuda2[contador][6])))
                        contador += 1  
                        QMessageBox.information(
                            self,"Correcto", "Busqueda exitosa", QMessageBox.Discard)
                else:
                        QMessageBox.warning(
                            self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                    QMessageBox.warning(
                        self, "Error", "No se ha encontrado nada", QMessageBox.Discard)  

    def validar_turno(self):
        turno = self.inputTurno.text()
        if turno == "":
            return False
        else:
            return True

    def validar_datos_4(self):
        if self.validar_turno():
            result= medicos.buscar_medicos_turno(self.inputTurno.text())
            print(self.inputTurno.text())
            print (result)
            ayuda2 = result
            try:
                if ayuda2:
                    contador = 0
                    for elements in ayuda2:
                        self.tablaMedicos.setItem(
                            contador, 0, QTableWidgetItem(str(ayuda2[contador][0])))
                        self.tablaMedicos.setItem(
                            contador, 1, QTableWidgetItem(ayuda2[contador][1]))
                        self.tablaMedicos.setItem(
                            contador, 2, QTableWidgetItem(str(ayuda2[contador][2])))
                        self.tablaMedicos.setItem(
                            contador, 3, QTableWidgetItem(ayuda2[contador][3]))
                        self.tablaMedicos.setItem(
                            contador, 4, QTableWidgetItem(ayuda2[contador][4]))
                        self.tablaMedicos.setItem(
                            contador, 5, QTableWidgetItem(str(ayuda2[contador][5])))
                        self.tablaMedicos.setItem(
                            contador, 6, QTableWidgetItem(str(ayuda2[contador][6])))
                        contador += 1
                        QMessageBox.information(
                            self,"Correcto", "Busqueda exitosa", QMessageBox.Discard)  
                else:
                        QMessageBox.warning(
                            self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                    QMessageBox.warning(
                        self, "Error", "No se ha encontrado nada", QMessageBox.Discard)                

    def mostrar_medicos_all(self):
            result2 = medicos.mostrar_medicos()
            print (result2)
            ayuda2 = result2
            try:
                    if ayuda2:
                        contador = 0
                        for elements in ayuda2:
                            self.tablaMedicos.setItem(
                                contador, 0, QTableWidgetItem(str(ayuda2[contador][0])))
                            self.tablaMedicos.setItem(
                                contador, 1, QTableWidgetItem(ayuda2[contador][1]))
                            self.tablaMedicos.setItem(
                                contador, 2, QTableWidgetItem(str(ayuda2[contador][2])))
                            self.tablaMedicos.setItem(
                                contador, 3, QTableWidgetItem(ayuda2[contador][3]))
                            self.tablaMedicos.setItem(
                                contador, 4, QTableWidgetItem(ayuda2[contador][4]))
                            self.tablaMedicos.setItem(
                                contador, 5, QTableWidgetItem(str(ayuda2[contador][5])))
                            self.tablaMedicos.setItem(
                                contador, 6, QTableWidgetItem(str(ayuda2[contador][6])))
                            contador += 1
                    else:
                        QMessageBox.warning(
                            self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                    QMessageBox.warning(
                        self, "Error", "No se ha encontrado nada", QMessageBox.Discard)

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
       #inputCedula{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputIdMedico{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputNombre{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputAp{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputTurno{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }

        """
        return estilo

    def switch(self):
        self.switch_window.emit()