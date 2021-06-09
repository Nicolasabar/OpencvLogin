import cv2
import numpy as np
import os


def entrenamientoDatos(nombreEdad):
    
    # Cambiar direccion del directorio segun equipo en el que se encuentre
    data = '/home/nicolas/Desktop/python whit open cv/data'

    lista = os.listdir(data)

    labels = []
    facesData = []
    label = 0

    for nameDir in lista:
        personPath = data + '/' + nameDir
        print('leyendo imagenes')

        for fileName in os.listdir(personPath):

            labels.append(label)
            facesData.append(cv2.imread(personPath + '/' + fileName, 0))
            image = cv2.imread(personPath + '/' + fileName, 0)
        label = label + 1

    reconocer = cv2.face.EigenFaceRecognizer_create()
    print("Registrando informacion para reconocimiento facial........")
    # Proceso de entrenamiento que posteriormente generara un archivo xml con el nombre del usuario que ingrese a traves del main o pantalla principal
    # lectura de imagenes (la IA considera que todas las imagenes son del mismo tamano, en caso de no serlo puede afectar o directamente generar un error)
    # considerar que entre mas data(imagenes a leer) mayor sera el tiempo de procesamiento para generar el nuevo modelo de reconocimiento facial
    # considerar que cada carpeta con nombre asignado esta dentro de un solo modelo, pero este modelo usara los nombres de cada carpeta para asociar
    # el reconocimiento facial segun lo que indique la prediccion
    reconocer.train(facesData, np.array(labels))

    nombreModelo = nombreEdad+'.xml'

    reconocer.write(nombreModelo)
    print('terminado')
