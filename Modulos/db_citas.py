
import Modulos.db_conexion as conexion
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem


def insertar_cita(self, idpaciente, fecha):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO cita(idPaciente_F,fechaCita) VALUES(%s,%s)"
        val = (idpaciente, fecha)
        mycursor.execute(sql, val)
        mydb.commit()
        result = 1
        return result
    except:
        QMessageBox.warning(self, "Error", "Fecha de cita ya asignada", QMessageBox.Discard)
    finally:
        mydb.close()
        mycursor.close()

def mostrar_citas():
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT cita.idCita, pacientes.idPaciente, pacientes.nombrePaciente, pacientes.apellidoPPaciente, pacientes.apellidoMPaciente, cita.fechaCita FROM cita,  pacientes WHERE cita.idPaciente_F = pacientes.idPaciente order by idCita DESC"
        mycursor.execute(sql)
        result2 = mycursor.fetchall()
        return result2
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_cita_idcita(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT cita.idCita, pacientes.idPaciente, pacientes.nombrePaciente, pacientes.apellidoPPaciente, pacientes.apellidoMPaciente, cita.fechaCita 
            FROM cita,  pacientes
            WHERE cita.idPaciente_F = pacientes.idPaciente AND cita.idCita= {}""".format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchone()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_cita_idpaciente(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = """SELECT cita.idCita, pacientes.idPaciente, pacientes.nombrePaciente, pacientes.apellidoPPaciente, pacientes.apellidoMPaciente, cita.fechaCita 
            FROM cita,  pacientes
            WHERE cita.idPaciente_F = pacientes.idPaciente AND cita.idPaciente_F= '{}' """.format(id)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_cita_fecha(fecha):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = """select cita.idCita,cita.idPaciente_F,pacientes.nombrePaciente,pacientes.apellidoPPaciente,pacientes.apellidoMPaciente,cita.fechaCita 
                FROM cita inner join pacientes on pacientes.idPaciente=cita.idPaciente_F  WHERE fechaCita = '{}' """.format(fecha)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

