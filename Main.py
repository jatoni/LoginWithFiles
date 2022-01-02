from Cifrado import *
op = 0
while op != 3:
    op = int(input('Que desea hacer? \n1.- Cifrar\n2.- Descifrar\n3.- Salir\nEscoger.- '))
    if op == 1:
        palabra = input("Agregar palabra a cifrar: ")
        clave = int(input('Agrega la clave: '))
        c1 = Cifrado(palabra, clave)
        print(f'Tu palabra cifrada es: {c1.cifrar()}')
    elif op == 2:
        palabra = input("Agregar palabra a cifrar: ")
        clave = int(input('Agrega la clave: '))
        c1 = Cifrado(palabra, clave)
        print(f'Tu palabra cifrada es: {c1.descifrar()}')
print('hasta aqui acaba el programa, adios')