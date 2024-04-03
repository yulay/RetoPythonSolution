#IMPORTS
import sys
import os
from subprocess import call

#VARIABLES
option = ''
list_users = []

#CONSTANTES
MIN_LEN = 4
MAX_LEN = 51
EXACTLY_LEN = 10

#FUNCIONES
def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

def new_user():
    dict_user = {
        "id":"",
        "nombres":"",
        "apellidos":"",
        "telefono":"",
        "correo_electronico":""
    }
    local_list_users = []
    len_nombres = 0
    len_apellidos = 0
    len_telefono = 0
    len_correo_electronico = 0
    cant_registros = 0
    user = 1
    
    clear()
    
    while cant_registros <= 0:
        cant_registros = int(input('Ingresa la cantidad de usuarios que dese registrar: '))

    print()
    
    while cant_registros >= 1:
        #Recopilacion de datos de usuario
        while len_nombres < MIN_LEN or len_nombres >= MAX_LEN:
            dict_user['nombres'] = input('Ingresa los nombres para el usuario ' + str(user) + ': ')
            len_nombres = len(dict_user['nombres'])
            if len_nombres < MIN_LEN or len_nombres >= MAX_LEN:
                print("Error, vuelve a ingresar los nombres (min:"+ str(MIN_LEN) +", max:" + str(MAX_LEN) + ")")
        
        while len_apellidos < MIN_LEN or len_apellidos >= MAX_LEN:
            dict_user['apellidos'] = input('Ingresa los apellidos para el usuario ' + str(user) +': ')
            len_apellidos = len(dict_user['apellidos'])
            if len_apellidos < MIN_LEN or len_apellidos >= MAX_LEN:
                print("Error, vuelve a ingresar los apellidos (min:"+ str(MIN_LEN) +", max:" + str(MAX_LEN) + ")")
        
        while len_telefono != EXACTLY_LEN:
            dict_user['telefono'] = input('Ingresa el número de teléfono para el usuario ' + str(user) + ': ')
            len_telefono = len(dict_user['telefono'])
            if len_telefono != EXACTLY_LEN:
                print("Error, el teléfono debe ser de exactamente " + str(EXACTLY_LEN) + " caracteres")
        
        while len_correo_electronico < MIN_LEN or len_correo_electronico >= MAX_LEN:
            dict_user['correo_electronico'] = input('Ingresa el correo electrónico para el usuario ' + str(user) + ': ')
            len_correo_electronico = len(dict_user['correo_electronico'])
            if len_correo_electronico < MIN_LEN or len_correo_electronico >= MAX_LEN:
                print("Error, vuelve a ingresar el correo electrónico (min:"+ str(MIN_LEN) +", max:" + str(MAX_LEN) + ")")
            
        #Mensaje de bienvenida
        print('Hola ' + dict_user['nombres'] + ' ' + dict_user['apellidos'] + ', en breve recibirás un correo a ' + dict_user['correo_electronico'])
        print()
        
        cant_registros -= 1
        dict_user['id'] = user
        new_dict = dict(dict_user)
        local_list_users.append(new_dict)
        user += 1
        len_nombres = 0
        len_apellidos = 0
        len_telefono = 0
        len_correo_electronico = 0
    
    input('Intro para continuar')
    
    return local_list_users

def flist_users():
    clear()
    
    if len(list_users) == 0:
        print('No hay usuarios registrados')
        input('Intro para continuar')
        return

    for user in list_users:
        print('USUARIO #' + str(user['id']))
        for key, value in tuple(user.items()):
            print(str(key) + ': ' + str(value))
        print('----------')
    
    input('Intro para continuar')

def show_user():
    ingreso = False
    
    clear()
    
    if len(list_users) == 0:
        print('No hay usuarios registrados')
        input('Intro para continuar')
        return
    
    id = input('Ingrese el ID que quiere consultar: ')
    print()
    
    for user in list_users:
        if int(user['id']) == int(id):
            for key, value in tuple(user.items()):
                print(str(key) + ': ' + str(value))
                ingreso = True
    
    if not ingreso:
        print('No se encontró información con el ID proporcionado')
    
    input('Intro para continuar')

def edit_user():
    ingreso = False
    len_nombres = 0
    len_apellidos = 0
    len_telefono = 0
    len_correo_electronico = 0
    
    clear()
    
    if len(list_users) == 0:
        print('No hay usuarios registrados')
        input('Intro para continuar')
        return
    
    id = input('Ingrese el ID que quiere consultar: ')
    print()
    
    for user in list_users:
        if int(user['id']) == int(id):
            while len_nombres < MIN_LEN or len_nombres >= MAX_LEN:
                user['nombres'] = input('Ingresa el nuevo nombre: ')
                len_nombres = len(user['nombres'])
                if len_nombres < MIN_LEN or len_nombres >= MAX_LEN:
                    print("Error, vuelve a ingresar los nombres (min:"+ str(MIN_LEN) +", max:" + str(MAX_LEN) + ")")
            
            while len_apellidos < MIN_LEN or len_apellidos >= MAX_LEN:
                user['apellidos'] = input('Ingresa el nuevo apellido: ')
                len_apellidos = len(user['apellidos'])
                if len_apellidos < MIN_LEN or len_apellidos >= MAX_LEN:
                    print("Error, vuelve a ingresar los apellidos (min:"+ str(MIN_LEN) +", max:" + str(MAX_LEN) + ")")
            
            while len_telefono != EXACTLY_LEN:
                user['telefono'] = input('Ingresa el nuevo teléfono: ')
                len_telefono = len(user['telefono'])
                if len_telefono != EXACTLY_LEN:
                    print("Error, el teléfono debe ser de exactamente " + str(EXACTLY_LEN) + " caracteres")
            
            while len_correo_electronico < MIN_LEN or len_correo_electronico >= MAX_LEN:
                user['correo_electronico'] = input('Ingresa el nuevo correo electrónico: ')
                len_correo_electronico = len(user['correo_electronico'])
                if len_correo_electronico < MIN_LEN or len_correo_electronico >= MAX_LEN:
                    print("Error, vuelve a ingresar el correo electrónico (min:"+ str(MIN_LEN) +", max:" + str(MAX_LEN) + ")")
            
            ingreso = True
    
    if not ingreso:
        print('No se encontró información con el ID proporcionado')
    
    input('Intro para continuar')

def delete_user():
    ingreso = False
    
    clear()
    
    if len(list_users) == 0:
        print('No hay usuarios registrados')
        input('Intro para continuar')
        return
    
    id = input('Ingrese el ID que quiere consultar: ')
    print()
    
    for user in list_users:
        if int(user['id']) == int(id):
            list_users.remove(user)
            ingreso = True
    
    if not ingreso:
        print('No se encontró información con el ID proporcionado')
    
    input('Intro para continuar')

def salir():
    sys.exit(0)

#PROGRAMA PRINCIPAL
while True:
    while option != 'a' and option != 'b' and option != 'c' and option != 'd' and option != 'e' and option != 'f':
        clear()
        print('***  MENÚ ***')
        print('a. Registrar nuevos usuarios')
        print('b. Listar usuarios y IDs')
        print('c. Consultar usuarios')
        print('d. Editar usuarios')
        print('e. Eliminar')
        print('f. Salir')
        option = input('Ingresa tu opción: ')
    
    if option == 'a':
        list_users.extend(new_user())
    elif option == 'b':
        flist_users()
    elif option == 'c':
        show_user()
    elif option == 'd':
        edit_user()
    elif option == 'e':
        delete_user()
    elif option == 'f':
        salir()
    else:
        print('Error, opción no identificada')
    
    option=''