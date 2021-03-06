import bcrypt
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import cv2
import os
import Modulos.db_iniciosesion as comprobar
class Login(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Inicio_sesion.ui", self)
        self.setWindowTitle("J-Medic: Inicio de Sesion")
        self.stylesheet = self.estilos()
        self.setStyleSheet(self.stylesheet)
        self.pushButton.clicked.connect(self.validar_datos)
        self.pushButton_2.clicked.connect(self.login2)
        self.validar()

    def estilos(self):
        estilo = """
        *{
            font-family:century gothic;
            font-size:24px;
        }

        QWidget{
            background-image: url(Imagenes/pru.jpg);
            background-color: white;
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
            background:#88c7dc;
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

        #label{
            font-size:65px;
        }
        """
        return estilo


    def validar(self):
        self.inputUsuario.textChanged.connect(self.validar_usuario)
        pass


    def validar_contra(self):
        result = comprobar.comprobar_inicio_contra()
        contra = self.inputPassword.text()
        encontro = 0
        try:
            contador = 0
            for elements in result:
                if bcrypt.checkpw(contra.encode(), result[contador][0].encode()):
                    encontro += 1
                    break
                else:
                    pass
                contador += 1
            if encontro>=1:
                return True
            else:
                return False
        except:
            pass

    def validar_usuario(self):
        result = comprobar.comprobar_inicio_usuario()
        user = self.inputUsuario.text()
        encontro = 0
        try:
            contador = 0
            for elements in result:
                if user == result[contador][0]:
                    encontro += 1
                    break
                else:
                    pass
                contador += 1
            if encontro>=1:
                return True
            else:
                return False
        except:
            pass

    def login(self):
        self.switch_window.emit()

    def validar_datos(self):
        if self.validar_usuario() and self.validar_contra():
            QMessageBox.information(
                self, "Exito", "Ingreso correctamente", QMessageBox.Discard)
            self.login()
        else:
            QMessageBox.warning(
                self, "Error", "El usuario o la contrase??a estan incorrectos", QMessageBox.Discard)



    def login2(self):
        dataPath = "./Data"
        imagePaths = os.listdir(dataPath)

        face_recognizer = cv2.face.EigenFaceRecognizer_create()

        # Leyendo el modelo
        face_recognizer.read("modeloEigenFaces.xml")

        cap = cv2.VideoCapture(1)

        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
        salir = 0
        global salir2
        salir2 = 0
        while True:
            ret, frame = cap.read()
            if ret == False: break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = gray.copy()

            faces = faceClassif.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150), interpolation= cv2.INTER_CUBIC)
                result = face_recognizer.predict(rostro)

                cv2.putText(frame, "{}".format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.cv2.LINE_AA)
                if result[1] < 5700:
                    cv2.putText(frame,"{}".format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    salir=1
                else:
                    cv2.putText(frame,"Desconocido",(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

            cv2.imshow("frame",frame)
            k =cv2.waitKey(1)
            if k == 27:
                salir2 = 0
                break
            if salir == 1:
                salir2 = 1
                break
        cap.release()
        cv2.destroyAllWindows()
        if salir2 == 1:
            self.switch_window.emit()