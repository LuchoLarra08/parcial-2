import pygame
from Constantes import *
from Funciones import mostrar_texto, guardar_puntuacion, mostrar_puntuacion_alta, actualizar_estadisticas

pygame.init()
pygame.mixer.init()

# Cargar música de fondo
pygame.mixer.music.load("game_music.mp3")  # Ruta de la música
pygame.mixer.music.set_volume(0.5)  # Ajusta el volumen (0.0 - 1.0)
pygame.mixer.music.play(-1)  # Reproduce la música en bucle (-1 para que sea infinito)
pygame.mixer.music.stop()  # Detiene la música

# Configuración del cuadro de texto para el nombre
fuente = pygame.font.SysFont("Arial Narrow", 40)
cuadro = {}
cuadro["superficie"] = pygame.Surface(CUADRO_TEXTO)
cuadro["rectangulo"] = cuadro["superficie"].get_rect()
cuadro["superficie"].fill(COLOR_AZUL)  # Color de fondo del cuadro
nombre = ""

def mostrar_fin_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict, volumen: float, dificultad: str) -> str:
    """
    Muestra la ventana final del juego, donde el jugador ingresa su nombre para guardar la puntuación.
    
    :param pantalla: Superficie principal del juego.
    :param cola_eventos: Lista de eventos generados por el usuario.
    :param datos_juego: Diccionario con información del juego, incluyendo la puntuación.
    :param volumen: El volumen actual del juego.
    :param dificultad: La dificultad seleccionada.
    :return: String que indica la próxima ventana a mostrar.
    """
    global nombre
    retorno = "terminado"  
    
    # Ajusta el volumen de la música en base a la opción seleccionada
    pygame.mixer.music.set_volume(volumen)

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir" 
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Guardar puntuación y volver al menú
            if cuadro["rectangulo"].collidepoint(evento.pos) and nombre.strip():
                guardar_puntuacion(nombre, datos_juego["puntuacion"])  # Guarda la puntuación
                # Actualizar estadísticas de las preguntas después del juego
                actualizar_estadisticas(datos_juego["estadisticas"])
                retorno = "menu"  
        elif evento.type == pygame.KEYDOWN:
            letra_presionada = pygame.key.name(evento.key)
            
            if letra_presionada == "backspace" and len(nombre) > 0:
                nombre = nombre[:-1]  
                cuadro["superficie"].fill(COLOR_AZUL)  # Rellena el cuadro con el color
            elif len(letra_presionada) == 1 and len(nombre) < 15:
                nombre += letra_presionada.upper()  # Agrega la letra al nombre

    # Dibuja pantalla
    pantalla.fill(COLOR_BLANCO)  # Fondo blanco
    cuadro["rectangulo"] = pantalla.blit(cuadro["superficie"], (200, 200))  # Dibuja el cuadro de texto
    mostrar_texto(cuadro["superficie"], nombre, (10, 5), fuente, COLOR_BLANCO)  # Muestra el nombre
    mostrar_texto(pantalla, f"Usted obtuvo: {datos_juego['puntuacion']} puntos", (250, 100), fuente, COLOR_NEGRO)
    mostrar_texto(pantalla, "Ingrese su nombre y haga clic para guardar", (150, 350), fuente, COLOR_NEGRO)

    # Mostrar la puntuación más alta
    puntuacion_alta = guardar_puntuacion(nombre, datos_juego["puntuacion"])  # Guarda la puntuación más alta
    mostrar_puntuacion_alta(pantalla, puntuacion_alta)  # Muestra la puntuación más alta

    return retorno

