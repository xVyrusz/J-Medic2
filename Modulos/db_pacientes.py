import Modulos.db_conexion as conexion


def insertar_pacientes(nombre, apellidop, apellidom, sexo, peso, estatura, edad, telefono, alergias, sangre):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO pacientes (nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,alergiasPaciente,idTipo_Sangre_F) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (nombre, apellidop, apellidom, sexo, peso,
               estatura, edad, telefono, alergias, sangre)
        mycursor.execute(sql, val)
        mydb.commit()
        result = 1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_pacientes_id(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT pacientes.idPaciente,nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,tipo_sangre.nombreSangre,pacientes.alergiasPaciente 
                FROM pacientes inner join tipo_sangre on pacientes.idTipo_sangre_F=tipo_sangre.idTipo_sangre
                WHERE pacientes.idPaciente= {}""".format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchone()
        return result
    except:
        print('Something wrong happend  id 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_pacientes_nombre(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT pacientes.idPaciente,nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,tipo_sangre.nombreSangre,pacientes.alergiasPaciente 
            FROM pacientes inner join tipo_sangre on pacientes.idTipo_sangre_F=tipo_sangre.idTipo_sangre
            WHERE  pacientes.nombrePaciente= '{}' """.format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_pacientes_apellido(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT pacientes.idPaciente,nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,tipo_sangre.nombreSangre,pacientes.alergiasPaciente 
            FROM pacientes inner join tipo_sangre on pacientes.idTipo_sangre_F=tipo_sangre.idTipo_sangre
            WHERE  pacientes.apellidoPPaciente= '{}' """.format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def mostrar_pacientes():
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        consult = """SELECT pacientes.idPaciente,nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,tipo_sangre.nombreSangre,pacientes.alergiasPaciente
               FROM pacientes inner join tipo_sangre on pacientes.idTipo_sangre_F=tipo_sangre.idTipo_sangre"""
        mycursor.execute(consult)
        result2 = mycursor.fetchall()
        return result2
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()