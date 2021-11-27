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


def buscar_medicos_cedula(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT medicos.idMedicos,nombreMedico,apellidoPMedico,apelLidoMMedico,Cedula,Telefono,turnos.nombreTurno 
            FROM medicos inner join turnos on medicos.idTurnos_F=turnos.idTurnos
             WHERE Cedula= {}""".format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchone()
        return result
    except:
        print('Something wrong happend buscar id 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_medicos_id(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT medicos.idMedicos,nombreMedico,apellidoPMedico,apelLidoMMedico,Cedula,Telefono,turnos.nombreTurno 
            FROM medicos inner join turnos on medicos.idTurnos_F=turnos.idTurnos
             WHERE idMedicos= {}""".format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchone()
        return result
    except:
        print('Something wrong happend buscar id 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_medicos_nombre(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT medicos.idMedicos,nombreMedico,apellidoPMedico,apelLidoMMedico,Cedula,Telefono,turnos.nombreTurno 
            FROM medicos inner join turnos on medicos.idTurnos_F=turnos.idTurnos
             WHERE nombreMedico= {}""".format(id)
        else:
            raise Exception('nombre is needed')
        mycursor.execute(consult)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend buscar nomb 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_medicos_apellido(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT medicos.idMedicos,nombreMedico,apellidoPMedico,apelLidoMMedico,Cedula,Telefono,turnos.nombreTurno 
            FROM medicos inner join turnos on medicos.idTurnos_F=turnos.idTurnos
             WHERE medicos.apellidoPMedico= {}""".format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend buscar apellido 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_medicos_turno(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
                    SELECT medicos.idMedicos,nombreMedico,apellidoPMedico,apelLidoMMedico,Cedula,Telefono,turnos.nombreTurno 
                    FROM medicos inner join turnos on medicos.idTurnos_F=turnos.idTurnos
             WHERE turnos.nombreTurno= {}""".format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend buscar turno 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def mostrar_medicos():
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        consult = "SELECT medicos.idMedicos,nombreMedico,apellidoPMedico,apelLidoMMedico,Cedula,Telefono,turnos.nombreTurno FROM medicos inner join turnos on medicos.idTurnos_F=turnos.idTurnos"
        mycursor.execute(consult)
        result2 = mycursor.fetchall()
        return result2
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()