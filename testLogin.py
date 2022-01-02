from ClienteLogin import Cliente
opcion = None
while opcion != 3:
    try:
        print('Que deseas hacer\n1.-Crear usuario.\n2-Ingresar\n3.- Salir.')
        opcion = int(input('\nEscribe tu opcion(1-3): '))
        if opcion == 1:
            nombre = input('Ingrese su nombre: ')
            Apellidos = input('Ingrese apellidos: ')
            usuario = input('Ingrese nombre de usuario: ')
            password = input('Ingrese contraseña: ')
            correo = input('Ingrese un correo electronico: ')
            cliente = Cliente(nombre,usuario,password,Apellidos,correo)
            cliente.crear()
    except Exception as e:
        print(f'Tu error es: {e}, tipo de error: {type(e)}')