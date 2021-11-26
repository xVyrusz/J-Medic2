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