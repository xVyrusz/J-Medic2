import sys
from PyQt5 import QtWidgets
import Modulos.inicioSesion as iniciosesion
import Modulos.menu as menu
import Modulos.menu2 as menu2
import Modulos.registrarMedicos as registrar_medicos
import Modulos.registrarPacientes as registrar_pacientes
import Modulos.registrarConsulta as registrar_consulta
import Modulos.registrarCita as registrar_cita
import Modulos.buscarMedico as buscar_medico
import Modulos.buscarPaciente as buscar_paciente
import Modulos.buscarConsulta as buscar_consulta
import Modulos.buscarCita as buscar_cita
import Modulos.editarPaciente as editar_paciente
import Modulos.editarMedico as editar_medico
import Modulos.editarConsulta as editar_consulta
import Modulos.editarCita as editar_cita
import Modulos.eliminarConsulta as eliminar_consulta
import Modulos.eliminarCita as eliminar_cita


class Controller:

    def __init__(self):
        pass

    def close(self):
        self.window_two.close()
        self.show_main()

    def close2(self):
        self.window_tree.close()
        self.show_main2()

    def close3(self):
        self.window.close()
        self.show_login()

    def close4(self):
        self.window_two.close()
        self.show_login()

    def show_login(self):
        self.login = iniciosesion.Login()
        self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.window = menu.MainWindow()
        self.window.switch_window.connect(self.show_registrar_medicos)
        self.window.switch_window2.connect(self.show_registrar_pacientes)
        self.window.switch_window3.connect(self.show_registrar_consulta)
        self.window.switch_window4.connect(self.show_registrar_cita)
        self.window.switch_window5.connect(self.show_buscar_medico)
        self.window.switch_window6.connect(self.show_buscar_paciente)
        self.window.switch_window7.connect(self.show_buscar_consulta)
        self.window.switch_window8.connect(self.show_buscar_cita)
        self.window.switch_window9.connect(self.show_main2)
        self.window.switch_window10.connect(self.close3)
        self.login.close()
        self.window.show()

    def show_registrar_medicos(self):
        self.window_two = registrar_medicos.WindowTwo()
        self.window_two.switch_window.connect(self.close)
        self.window.close()
        self.window_two.show()

    def show_registrar_pacientes(self):
        self.window_two = registrar_pacientes.WindowTwo()
        self.window_two.switch_window.connect(self.close)
        self.window.close()
        self.window_two.show()

    def show_registrar_consulta(self):
        self.window_two = registrar_consulta.WindowTwo()
        self.window_two.switch_window.connect(self.close)
        self.window.close()
        self.window_two.show()

    def show_registrar_cita(self):
        self.window_two = registrar_cita.WindowTwo()
        self.window_two.switch_window.connect(self.close)
        self.window.close()
        self.window_two.show()

    def show_buscar_medico(self):
        self.window_two = buscar_medico.WindowTwo()
        self.window_two.switch_window.connect(self.close)
        self.window.close()
        self.window_two.show()

    def show_buscar_paciente(self):
        self.window_two = buscar_paciente.WindowTwo()
        self.window_two.switch_window.connect(self.close)
        self.window.close()
        self.window_two.show()

    def show_buscar_consulta(self):
        self.window_two = buscar_consulta.WindowTwo()
        self.window_two.switch_window.connect(self.close)
        self.window.switch_window.connect(self.show_registrar_medicos)
        self.window.switch_window2.connect(self.show_registrar_pacientes)
        self.window.switch_window3.connect(self.show_registrar_consulta)
        self.window.switch_window4.connect(self.show_registrar_cita)
        self.window.switch_window5.connect(self.show_buscar_medico)
        self.window.switch_window6.connect(self.show_buscar_paciente)
        self.window.switch_window7.connect(self.show_buscar_consulta)
        self.window.close()
        self.window_two.show()

    def show_buscar_cita(self):
        self.window_two = buscar_cita.WindowTwo()
        self.window_two.switch_window.connect(self.close)
        self.window.close()
        self.window_two.show()

    def show_main2(self):
        self.window_two = menu2.WindowTwo()
        self.window_two.switch_window.connect(self.show_editar_paciente)
        self.window_two.switch_window2.connect(self.show_editar_medico)
        self.window_two.switch_window3.connect(self.show_editar_consulta)
        self.window_two.switch_window4.connect(self.show_editar_cita)
        self.window_two.switch_window5.connect(self.show_eliminar_consulta)
        self.window_two.switch_window6.connect(self.show_eliminar_cita)
        self.window_two.switch_window7.connect(self.close)
        self.window_two.switch_window8.connect(self.close4)
        self.window.close()
        self.window_two.show()

    def show_editar_paciente(self):
        self.window_tree = editar_paciente.WindowTree()
        self.window_tree.switch_window.connect(self.close2)
        self.window_two.close()
        self.window_tree.show()

    def show_editar_medico(self):
        self.window_tree = editar_medico.WindowTree()
        self.window_tree.switch_window.connect(self.close2)
        self.window_two.close()
        self.window_tree.show()

    def show_editar_consulta(self):
        self.window_tree = editar_consulta.WindowTree()
        self.window_tree.switch_window.connect(self.close2)
        self.window_two.close()
        self.window_tree.show()

    def show_editar_cita(self):
        self.window_tree = editar_cita.WindowTree()
        self.window_tree.switch_window.connect(self.close2)
        self.window_two.close()
        self.window_tree.show()

    def show_eliminar_consulta(self):
        self.window_tree = eliminar_consulta.WindowTree()
        self.window_tree.switch_window.connect(self.close2)
        self.window_two.close()
        self.window_tree.show()

    def show_eliminar_cita(self):
        self.window_tree = eliminar_cita.WindowTree()
        self.window_tree.switch_window.connect(self.close2)
        self.window_two.close()
        self.window_tree.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())