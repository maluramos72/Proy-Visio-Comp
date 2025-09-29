# Proy-Visio-Comp
Este proyecto utiliza Python + OpenCV + cvzone para detectar manos en tiempo real con la webcam  (mano abierta, puño cerrado, señal de llamada, etc.).

📌 Características

📷 Detección en tiempo real usando la webcam.

✋ Identificación de la mano izquierda y derecha.

🤙 Reconocimiento de gestos como:

Mano abierta (5 dedos)

Puño cerrado (0 dedos)

Señal de llamada (pulgar y meñique arriba)

Dos dedos levantados ✌️

🟢 Visualización con bounding box y puntos clave en los dedos.

🛠️ Tecnologías

Python 3.x

OpenCV

cvzone
 (basado en Mediapipe)

 📥 Instalación

Clona el repositorio:

git clone https://github.com/maluramos72/Proy-Visio-Comp.git
cd visionxcompu


Crea un entorno virtual (opcional pero recomendado):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Instala dependencias:

pip install -r requirements.txt


Si no tienes requirements.txt, instala manualmente:

pip install opencv-python cvzone

▶️ Uso

Ejecuta el script principal:

python Proypp-Visio.py


Presiona q para salir de la aplicación.

📂 Estructura del Proyecto
visionxcompu/
│── Proypp-Visio.py     # Código principal de detección de manos y gestos
│── requirements.txt     # Dependencias del proyecto
│── README.md     
