from domain.Cifrado import Cifrado
from login import *
from pathlib import Path
import os


class Cliente(Login):
    iguales = 0
    def __init__(self, nombre, usuario, password, apellidos, correo):
        self._nombre = nombre
        self._apellidos = apellidos
        self._correo = correo
        super().__init__(usuario, password)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    def crear(self):
        try:
            arch = 'C:/Cursos/Python/Practicas/LoginConArchivos/Usuarios/' + self._usuario + '.txt'
            my_file = Path(arch)
            if my_file.is_file():
                print(f'El usuario: {self._usuario} ya existe, intente con otro.')
                arch.close()
            else:
                user = self._usuario + '.txt'
                si_exite = os.listdir('C:/Cursos/Python/Practicas/LoginConArchivos/Usuarios')
                for dentro in si_exite:
                    archivos = open('C:/Cursos/Python/Practicas/LoginConArchivos/Usuarios/'+dentro, 'r', encoding='utf8')
                    igual = archivos.readlines()[3]
                    archivos.close()
                    if igual == f'Correo: {self._correo}\n':
                        Cliente.iguales = Cliente.iguales + 1
                if Cliente.iguales > 0:
                    print(f'El correo {self._correo} ya existe')
                else:
                    cifrado = Cifrado(self._password,5)
                    archivo = open('C:/Cursos/Python/Practicas/LoginConArchivos/Usuarios/' + user, 'a', encoding='utf8')
                    archivo.write(f'Nombre: {self._nombre}\nApellido: {self._apellidos}\nUsuario: {self._usuario}\nCorreo: {self._correo}\nPassword: {cifrado.cifrar()}')
                    print(f'El usuario {self._usuario} fue creado con exito'.center(50, '-'))
                    archivo.close()
        except Exception as e:
            print(f'Tuviste un error: {e}, Tipo de error: {type(e)}')
        finally:
            # archivo.close()
            # arch.close()
            pass
    def entrar(self):
        pass


if __name__ == '__main__':
    cliente1 = Cliente('Carlosx', '7Carlos9', 'holismune34523', 'Antonio', 'carlos70@gmail.com')
    cliente1.crear()