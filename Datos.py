class Datos:
    def __init__(self, clave, palabra):
        self._abc = abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                           'H', 'I', 'J', 'K', 'L', 'M', 'N',
                           'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                           'V', 'W', 'X', 'Y', 'Z', '1', '2',
                           '3', '4', '5', '6', '7', '8', '9' ]
        self._clave = clave
        self._palabra = palabra

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, clave):
        self._clave = clave
    @property
    def abc(self):
        return self._abc