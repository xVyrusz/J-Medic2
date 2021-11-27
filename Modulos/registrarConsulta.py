import re
import datetime
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import Modulos.db_consultas as consultas

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/AddConsulta.ui", self)
        self.setWindowTitle("J-Medic: Registrar Consulta")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.guardarConsulta.clicked.connect(self.validar_datos_2)
        self.generarIdConsulta.clicked.connect(self.validar_datos)
        self.botonFecha.clicked.connect(self.seleccionar_fecha)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.inputIdMedico.textChanged.connect(self.validar_id_medico)
        self.inputIdPaciente.textChanged.connect(self.validar_id_paciente)
        #self.inputIdConsulta.textChanged.connect(self.validar_id_consulta)
        self.inputPruebasRealizadas.textChanged.connect(self.validar_pruebas)
        self.inputDiagnostico.textChanged.connect(self.validar_diagnostico)
        self.inputTratamiento.textChanged.connect(self.validar_tratamiento)
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
            motivo = 0
            if self.inputMotivoConsulta.currentText() == 'Consulta general':
                motivo = 1
            elif self.inputMotivoConsulta.currentText() == 'Examenes':
                motivo = 2
            elif self.inputMotivoConsulta.currentText() == 'Curaciones':
                motivo = 3
            else:
                motivo = 1
            fecha_2 = datetime.date.today()
            fecha_3 = str(fecha_2)
            self.FechaAuto.setText(str(fecha_3))
            result = consultas.insertar_datos_de_consulta(
                self.inputIdMedico.text(), self.inputIdPaciente.text(), fecha_2, motivo)
            if result == 1:
                result2 = consultas.mostrar_datos_consulta()
                print(result2)

                ayuda = result2
                try:
                    if ayuda:
                        contador = 0
                        for elements in ayuda:
                            self.tablaConsultas.setItem(
                                contador, 0, QTableWidgetItem(str(ayuda[contador][0])))
                            self.tablaConsultas.setItem(
                                contador, 1, QTableWidgetItem(ayuda[contador][1]))
                            self.tablaConsultas.setItem(
                                contador, 2, QTableWidgetItem(str(ayuda[contador][2])))
                            self.tablaConsultas.setItem(
                                contador, 3, QTableWidgetItem(ayuda[contador][3]))
                            self.tablaConsultas.setItem(
                                contador, 4, QTableWidgetItem(ayuda[contador][4]))
                            self.tablaConsultas.setItem(
                                contador, 5, QTableWidgetItem(str(ayuda[contador][5])))
                            self.tablaConsultas.setItem(
                                contador, 6, QTableWidgetItem(str(ayuda[contador][6])))
                            contador += 1
                    else :         
                        QMessageBox.information(
                            self, "Datos guardados", "Se genero su ID de consulta correctamente", QMessageBox.Discard)
                except : 
                    QMessageBox.information(
                        self, "Datos guardados", "Se genero su ID de consulta correctamente", QMessageBox.Discard)
            else:
                QMessageBox.warning(
                    self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def validar_id_consulta(self):
        id_consulta = self.inputIdConsulta.text()
        validar = re.match("^\d{1,}$", id_consulta, re.I)
        if id_consulta == "":
            self.inputIdConsulta.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputIdConsulta.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputIdConsulta.setStyleSheet("border: 2px solid green;")
            return True

    def validar_pruebas(self):
        pruebas = self.inputPruebasRealizadas.toPlainText()
        validar = re.match(
            "^[\w'\-,.][^_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", pruebas, re.I)
        if pruebas == "":
            self.inputPruebasRealizadas.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputPruebasRealizadas.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputPruebasRealizadas.setStyleSheet("border: 2px solid green;")
            return True

    def validar_diagnostico(self):
        diag = self.inputDiagnostico.toPlainText()
        validar = re.match(
            "^[\w'\-,.][^_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", diag, re.I)
        if diag == "":
            self.inputDiagnostico.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputDiagnostico.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputDiagnostico.setStyleSheet("border: 2px solid green;")
            return True

    def validar_tratamiento(self):
        trata = self.inputTratamiento.toPlainText()
        validar = re.match(
            "^[\w'\-,.][^_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", trata, re.I)
        if trata == "":
            self.inputTratamiento.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.inputTratamiento.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.inputTratamiento.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_2(self):
        cont = 0
        if self.validar_id_consulta() and self.validar_pruebas() and self.validar_diagnostico() and self.validar_tratamiento():
            result =consultas.insertar_consulta(self.inputIdConsulta.text(),self.inputPruebasRealizadas.toPlainText(),self.inputDiagnostico.toPlainText()
            ,self.inputTratamiento.toPlainText())
            print(result)
            if result == 1:
                QMessageBox.information(
                    self, "Datos guardados", "Se genero su consulta correctamente", QMessageBox.Discard)
            #self.switch()
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