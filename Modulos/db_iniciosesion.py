import Modulos.db_conexion as conexion


def comprobar_inicio_usuario():
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT medicos.Cedula FROM mydb.medicos;"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print('Cedula😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def comprobar_inicio_contra():
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT medicos.contra FROM mydb.medicos;"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print('Contraseña 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()