from Datos import *
class Cifrado(Datos):
    d1 = Datos.abc
    def __init__(self, palabra, clave):
        self.palabra = palabra
        self.clave = clave
        super().__init__(clave, palabra)
        self.resultado = ""

    def cifrar(self):
        for i in self.palabra:
            for j in self.abc:
                if i.upper() in j:
                    self.resultado += self.abc[(self.abc.index(j)+self.clave)% len(self.abc)]
        return self.resultado

    def descifrar(self):
        for i in self.palabra:
            for j in self.abc:
                if i.upper() in j:
                    self.resultado += self.abc[(self.abc.index(j)-self.clave)% len(self.abc)]
        return self.resultado
if __name__ == '__main__':
    cifrado1 = Cifrado('hola66',5)
    print(cifrado1.cifrar())



