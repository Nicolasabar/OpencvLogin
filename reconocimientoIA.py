import cv2
import os
import time


def reconocimientoRostro(nombremodelo):
    # ruta de donde se toma la data para el desarrollo del modelo, cambiar ruta de acuerdo a tu equiupo
    dataPath = '/home/nicolas/Desktop/python whit open cv/data'
    imagePaths = os.listdir(dataPath)

    # Carga del metodo EigenFaceRecognizer_create propio de opencv
    reconocerCara = cv2.face.EigenFaceRecognizer_create()

    usuario = nombremodelo

    # capturando modelo a leer creado y entrenado para reconocimiento de la persona que se registre
    nombreModelo = usuario+'.xml'

    # Lectura de modelo
    reconocerCara.read(nombreModelo)

    cap = cv2.VideoCapture(0)

    # Asignacion del modelo de clasificacion de rostros a una variable CascadeClassifier
    # Modelo propio de la libreria opencv, este modelo ya se encuentra entrenado para reconocer rostros
    # Solo reconoce rosotros, no los clasifica por si solo, ejemplo: reconoce mi cara, pero no reconoce si estoy ligado o registrado en la app que se usa
    faceClassif = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    validar = False
    no_Existe = False

    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            # El modelo de reconocimiento entiende que el tamano de imagenes que se le entregan son todas del mismo tamano en este caso 150x150
            rostro = auxFrame[y:y+h, x:x+y]
            rostro = cv2.resize(rostro, (150, 150),
                                interpolation=cv2.INTER_CUBIC)
            result = reconocerCara.predict(rostro)

            cv2.putText(frame, '{}'.format(result), (x, y-5),
                        1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

            # Ajustar parametro de 7000 para el reconocimiento facial, puede tener variaciones en los resultados
            # dependiendo de la calidad de imagenes y la cantidad de data con la que se crea el modelo
            # a mas cerca del 0 mayor probabilidad de acertar
            if result[1] < 7000:
                # lectura de la imagen asignada a la variable frame escalada a grises para poder identificar
                # Asignacion de parametros de resultadi y creacion de rectangulo para reconocer rostro
                cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y-5),
                            1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                # El valor validar cambie  True en caso de que el rostro a reconocer sea verdadero
                validar = True
            else:
                cv2.putText(frame, 'Desconocido', (x, y - 20),
                            2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                # El valor no_Existe cambia a True en caso de que no sea capas de reconocer el rostro capturado en la webcam_
                no_Existe = True
        # con cv2.imshow se carga la imagen y con time.sleep se espera una catidad de segundos() en este caso 1
        # vajidar en True nos dice que el usuario se registro bien y nos permite ingresar
        # con no_Existe validamos que el usuario no existe para finalizar la aplicacion
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1)
        if k == 27 or validar == True:
            time.sleep(1)
            print('Usuario encontrado en el registro')
            print('')
            print('**************************************')
            print('************Bienvenido {}**********'.format(usuario))
            print('**************************************')
            return True
            break
        elif k == 27 or no_Existe == True:
            time.sleep(1)
            print('Usuario no identificado')
            print('Debe registrarse para ingresar')
            return False
            break

    cap.release()
    cv2.destroyAllWindows()
