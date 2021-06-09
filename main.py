import registroIA
import entrenoIA
import reconocimientoIA
import os
import reconocimientoLogin


def procesoRegistro():

    namePerson = input('Ingrese nombre de usuario: ')

    registroIA.registrar(namePerson)
    entrenoIA.entrenamientoDatos(namePerson)
    if reconocimientoIA.reconocimientoRostro(namePerson) == True:
        print('       *')
        print('     *****')
        print('   ********')
        print('  ***********')
        print('****************')
        print('    !      !')
        print('    !      !')
    elif reconocimientoIA.reconocimientoRostro(namePerson) == False:
        pass


if __name__ == '__main__':

    print('********************************************************')
    print('')
    print('**********Bienvenido************')
    print('')
    print('********************************************************')

    pregunta = int(input('1- para registrarse\n 2- Para logearse \n '))

    if pregunta == 1:

        procesoRegistro()
    elif pregunta == 2:

        nombre_archivo = input('ingrese su nombre de usuario: ')

        reconocimientoLogin.reconocimientoRostro(nombre_archivo)
