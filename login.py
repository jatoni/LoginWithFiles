from abc import ABC, abstractmethod

class Login(ABC):
    def __init__(self, usuario, password):
        self._usuario = usuario
        self._password = password

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @abstractmethod
    def entrar(self):
        pass

    @abstractmethod
    def crear(self):
        pass