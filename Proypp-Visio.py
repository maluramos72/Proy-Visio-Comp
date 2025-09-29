import cv2
from cvzone.HandTrackingModule import HandDetector

# Inicializar la webcam
webcam = cv2.VideoCapture(0)
webcam.set(3, 740)  # Ancho
webcam.set(4, 580)  # Alto

# Verificar si la webcam 
if not webcam.isOpened():
    print("Error: No se pudo abrir la webcam.")
    exit()

# Inicializar el detector de manos
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Crear ventana ajustable
cv2.namedWindow('Vision x Compu - Webcam', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Vision x Compu - Webcam', 640, 480)

while True:
    # Leer frame de la webcam
    exito, frame = webcam.read()
    if not exito:
        print("Error al leer la imagen de la webcam.")
        break

    # Detectar las manos
    manos, img_con_manos = detector.findHands(frame, flipType=True)

    # Si hay manos detectadas
    if manos:
        for mano in manos:
            # Dibujar la caja alrededor de la mano
            x, y, w, h = mano['bbox']
            cv2.rectangle(img_con_manos, (x, y), (x + w, y + h), (255, 0, 255), 2)

            # Dibujar puntos de la mano
            for punto in mano['lmList']:
                cv2.circle(img_con_manos, (punto[0], punto[1]), 5, (0, 255, 0), cv2.FILLED)

    # Mostrar imagen
    cv2.imshow('Vision x Compu - Webcam', img_con_manos)

    # Salir con la cualquier tecla 
    if cv2.waitKey(1) != -1: 
        break

# Liberar recursos
webcam.release()
cv2.destroyAllWindows()

