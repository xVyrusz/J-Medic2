import Modulos.db_conexion as conexion
from PyQt5.QtWidgets import QMessageBox
import bcrypt

def insertar_medicos(nombre, apellidop, apellidom, cedula, telefono, id_turnos, contra):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO medicos(nombreMedico,apellidoPMedico,apellidoMMedico,Cedula,Telefono,idTurnos_F,contra) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        hashed = bcrypt.hashpw(contra.encode(), bcrypt.gensalt(10))
        if id_turnos == "Matutino":
            id_turnos = 1
        elif id_turnos == "Vespertino":
            id_turnos = 2
        else:
            pass
        #val = (nombre,apellidop,apellidom,cedula,telefono,id_turnos,usuario,password)
        val = (nombre, apellidop, apellidom, cedula,
               telefono, id_turnos, hashed.decode())

        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM medicos")
        result = mycursor.fetchall()

        result = 1
        return result
    except:
         print("Error al guardar los datos"),
                                #"Su informacion no se ha guardado", QMessageBox.Discard)
    finally:
        mydb.close()
        mycursor.close()
