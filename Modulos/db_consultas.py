import Modulos.db_conexion as conexion


def insertar_datos_de_consulta(idmedicos, idpaciente, fecha, motivo):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO datos_de_consulta(idMedicos_F,idPaciente_F,fechaVisita,idMotivo_F) VALUES(%s,%s,%s,%s)"
        val = (idmedicos, idpaciente, fecha, motivo)
        mycursor.execute(sql, val)
        mydb.commit()
        result = 1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def mostrar_datos_consulta():
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        consult = " SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita, motivos_de_consulta.nombreMotivo FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F order by idConsulta DESC"
        mycursor.execute(consult)
        result2 = mycursor.fetchall()
        return result2
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def insertar_consulta(idc, pruebas, diagnostico, tratamiento):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO consulta(idConsulta_F,pruebasRealizadas,diagnostico,tratamiento) VALUES(%s,%s,%s,%s)"
        val = (idc, pruebas, diagnostico, tratamiento)
        mycursor.execute(sql, val)
        mydb.commit()
        result = 1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_consulta_id(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,
            motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F where datos_de_consulta.idConsulta = {}""".format(id)
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

def buscar_consulta_id_medico(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
           SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,
            motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F where medicos.idMedicos=  {}""".format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend  medico😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_consulta_id_paciente(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,
            motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F where pacientes.idPaciente = {}""".format(id)
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

def buscar_consulta_fecha(fecha):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE datos_de_consulta.fechaVisita = '{}'".format(
            fecha)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()