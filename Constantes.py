import pygame
from pygame import mixer


# Inicializar pygame y el mezclador de sonido
pygame.init()
pygame.mixer.init()  # Esto asegura que el mezclador de sonido se inicialice correctamente

# Dimensiones de la ventana
VENTANA = (800, 600)
WIDTH = 800  # Ancho de la ventana
HEIGHT = 600  # Alto de la ventana

# Colores
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)
COLOR_AZUL = (0, 102, 204)
COLOR_VERDE = (0, 204, 102)
COLOR_ROJO = (204, 0, 0)
COLOR_GRIS_CLARO = (200, 200, 200)
COLOR_GRIS = (200, 200, 200)

# Dimensiones de botones
TAMAÑO_BOTON = (200, 50)
TAMAÑO_BOTON_VOLVER = (100, 40)
CUADRO_TEXTO = (400, 50)

# Constantes de botones en el menú
BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_PUNTUACIONES = 2
BOTON_SALIR = 3
BOTON_AGREGAR = 4
BOTON_OPCIONES = 5

# Juego
FPS = 60
CANTIDAD_VIDAS = 3
PUNTOS_ACIERTO = 10
PUNTOS_ERROR = -5
TIEMPO_RESPUESTA = 30

# Sonidos
CLICK_SONIDO = pygame.mixer.Sound("click.mp3")
ERROR_SONIDO = pygame.mixer.Sound("error.mp3")

# Archivos
PREGUNTAS_CSV = "preguntas.csv"

