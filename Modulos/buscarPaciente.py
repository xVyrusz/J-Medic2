import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import Modulos.db_pacientes as pacientes

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/BuscarPaciente.ui", self)
        self.setWindowTitle("J-Medic: Buscar Medico")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.botonBuscar.clicked.connect(self.mostrar_pacientes_all)
        self.buscarId.clicked.connect(self.validar_datos)
        self.buscarNombre.clicked.connect(self.validar_datos_2)
        self.buscarApellidoP.clicked.connect(self.validar_datos_3)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.inputIdPaciente.textChanged.connect(self.validar_id_paciente)
        self.inputNombre.textChanged.connect(self.validar_nombre)
        self.inputAp.textChanged.connect(self.validar_apellidoP)
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

    def validar_datos(self):
        if self.validar_id_paciente():
            result= pacientes.buscar_pacientes_id(int(self.inputIdPaciente.text()))
            print (result)
            ayuda = result
            try:
                self.tablaPacientes.setItem(0 , 0, QTableWidgetItem(str(ayuda[0])))
                self.tablaPacientes.setItem(0 , 1, QTableWidgetItem(ayuda[1]))
                self.tablaPacientes.setItem(0 , 2, QTableWidgetItem(ayuda[2]))
                self.tablaPacientes.setItem(0 , 3, QTableWidgetItem(ayuda[3]))
                self.tablaPacientes.setItem(0 , 4, QTableWidgetItem(ayuda[4]))
                self.tablaPacientes.setItem(0 , 5, QTableWidgetItem(str(ayuda[5])))
                self.tablaPacientes.setItem(0 , 6, QTableWidgetItem(str(ayuda[6])))
                self.tablaPacientes.setItem(0 , 7, QTableWidgetItem(str(ayuda[7])))
                self.tablaPacientes.setItem(0 , 8, QTableWidgetItem(ayuda[8]))
                self.tablaPacientes.setItem(0 , 9, QTableWidgetItem(ayuda[9]))
                self.tablaPacientes.setItem(0 , 10, QTableWidgetItem(ayuda[10]))
                QMessageBox.information(
                self,"Correcto", "Busqueda exitosa", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
        else:
           QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

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
            result= pacientes.buscar_pacientes_nombre(self.inputNombre.text())
            print (result)
            ayuda2 = result
            try:
                    if ayuda2:
                        contador = 0
                        for elements in ayuda2:
                            self.tablaPacientes.setItem(
                                contador, 0, QTableWidgetItem(str(ayuda2[contador][0])))
                            self.tablaPacientes.setItem(
                                contador, 1, QTableWidgetItem(ayuda2[contador][1]))
                            self.tablaPacientes.setItem(
                                contador, 2, QTableWidgetItem(str(ayuda2[contador][2])))
                            self.tablaPacientes.setItem(
                                contador, 3, QTableWidgetItem(ayuda2[contador][3]))
                            self.tablaPacientes.setItem(
                                contador, 4, QTableWidgetItem(ayuda2[contador][4]))
                            self.tablaPacientes.setItem(
                                contador, 5, QTableWidgetItem(str(ayuda2[contador][5])))
                            self.tablaPacientes.setItem(
                                contador, 6, QTableWidgetItem(str(ayuda2[contador][6])))
                            self.tablaPacientes.setItem(
                                contador, 7, QTableWidgetItem(str(ayuda2[contador][7])))
                            self.tablaPacientes.setItem(
                                contador, 8, QTableWidgetItem(str(ayuda2[contador][8])))
                            self.tablaPacientes.setItem(
                                contador, 9, QTableWidgetItem(str(ayuda2[contador][9])))
                            self.tablaPacientes.setItem(
                                contador, 10, QTableWidgetItem(str(ayuda2[contador][10])))
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
            result= pacientes.buscar_pacientes_apellido(self.inputAp.text())
            print (result)
            ayuda2 = result
            try:
                    if ayuda2:
                        contador = 0
                        for elements in ayuda2:
                            self.tablaPacientes.setItem(
                                contador, 0, QTableWidgetItem(str(ayuda2[contador][0])))
                            self.tablaPacientes.setItem(
                                contador, 1, QTableWidgetItem(ayuda2[contador][1]))
                            self.tablaPacientes.setItem(
                                contador, 2, QTableWidgetItem(str(ayuda2[contador][2])))
                            self.tablaPacientes.setItem(
                                contador, 3, QTableWidgetItem(ayuda2[contador][3]))
                            self.tablaPacientes.setItem(
                                contador, 4, QTableWidgetItem(ayuda2[contador][4]))
                            self.tablaPacientes.setItem(
                                contador, 5, QTableWidgetItem(str(ayuda2[contador][5])))
                            self.tablaPacientes.setItem(
                                contador, 6, QTableWidgetItem(str(ayuda2[contador][6])))
                            self.tablaPacientes.setItem(
                                contador, 7, QTableWidgetItem(str(ayuda2[contador][7])))
                            self.tablaPacientes.setItem(
                                contador, 8, QTableWidgetItem(str(ayuda2[contador][8])))
                            self.tablaPacientes.setItem(
                                contador, 9, QTableWidgetItem(str(ayuda2[contador][9])))
                            self.tablaPacientes.setItem(
                                contador, 10, QTableWidgetItem(str(ayuda2[contador][10])))
                            contador += 1
                        QMessageBox.information(
                                    self,"Correcto", "Busqueda exitosa", QMessageBox.Discard)
                    else:
                        QMessageBox.warning(
                            self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                    QMessageBox.warning(
                        self, "Error", "No se ha encontrado nada", QMessageBox.Discard)

    def mostrar_pacientes_all(self):
            result2 = pacientes.mostrar_pacientes()
            print (result2)
            ayuda2 = result2
            try:
                    if ayuda2:
                        contador = 0
                        for elements in ayuda2:
                            self.tablaPacientes.setItem(
                                contador, 0, QTableWidgetItem(str(ayuda2[contador][0])))
                            self.tablaPacientes.setItem(
                                contador, 1, QTableWidgetItem(ayuda2[contador][1]))
                            self.tablaPacientes.setItem(
                                contador, 2, QTableWidgetItem(str(ayuda2[contador][2])))
                            self.tablaPacientes.setItem(
                                contador, 3, QTableWidgetItem(ayuda2[contador][3]))
                            self.tablaPacientes.setItem(
                                contador, 4, QTableWidgetItem(ayuda2[contador][4]))
                            self.tablaPacientes.setItem(
                                contador, 5, QTableWidgetItem(str(ayuda2[contador][5])))
                            self.tablaPacientes.setItem(
                                contador, 6, QTableWidgetItem(str(ayuda2[contador][6])))
                            self.tablaPacientes.setItem(
                                contador, 7, QTableWidgetItem(str(ayuda2[contador][7])))
                            self.tablaPacientes.setItem(
                                contador, 8, QTableWidgetItem(str(ayuda2[contador][8])))
                            self.tablaPacientes.setItem(
                                contador, 9, QTableWidgetItem(str(ayuda2[contador][9])))
                            self.tablaPacientes.setItem(
                                contador, 10, QTableWidgetItem(str(ayuda2[contador][10])))
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
        #inputIdPaciente{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputAp{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }
        #inputNombre{
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
        }

        """
        return estilo

    def switch(self):
        self.switch_window.emit()