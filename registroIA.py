import cv2
import os
import imutils


def registrar(nameFolder):

    # apollo de variables del sistema operativo para creacion de carpeta con nombre de usuario que sera ingresado a traves del main

    os.mkdir('/home/nicolas/Desktop/python whit open cv/data/' + nameFolder)

    sinMascarilla = nameFolder

    datapath = '/home/nicolas/Desktop/python whit open cv/data'
    datosMascarilla = datapath + '/' + sinMascarilla

    cap = cv2.VideoCapture(0)

    faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # contador para agregar fotos se inicia en 0 y se puede terminar con la cantidad de fotos que usted considere necesaria para armar su data
    count = 0

    while True:
        # captura y lectura de datos desde la webcam, opencv captura imagenes de forma interna en escala de grises
        # para esto se usa cv2.color_rgb2gray
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        auxFrame = frame.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)
        # parametros para generar rectangulo en cara, valores muy altos o muy pequenos pueden provocar falsos positivos en captura
        # o tambien puede ser que directamente no capture el rostro
        # valor 150 indica el tamano de las imagenes que se guardaran
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            rostro = auxFrame[y:y+h, x:x+w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC
                                )
            cv2.imwrite(datosMascarilla +
                        '/rostro_{}.jpg'.format(count), rostro)
            count = count + 1
        cv2.imshow('frame', frame)
        # cuando el numero de imagenes sea igual a 500 la etapa de registro habra terminado
        # se guardara la informacion en la carpeta data con una nueva carpeta con nombre de usuario y sus fotos capturadas para el entrenamiento
        k = cv2.waitKey(1)
        if k == 27 or count >= 500:
            break

    cap.release()
    cv2.destroyAllWindows()
