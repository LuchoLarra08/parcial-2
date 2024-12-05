import pygame
from Constantes import *  # Asegúrate de que estas constantes estén correctamente definidas
from Funciones import mostrar_texto

pygame.init()

fuente_menu = pygame.font.SysFont("Arial Narrow", 30)

# Asegúrate de definir el número correcto de botones
lista_botones = []
# Ajustamos la cantidad de botones a 6 (incluyendo las nuevas opciones)
for i in range(6):  
    boton = {}
    boton["superficie"] = pygame.Surface(TAMAÑO_BOTON)  # Definir el tamaño del botón
    boton["superficie"].fill(COLOR_AZUL)  # Color de fondo de los botones
    boton["rectangulo"] = boton["superficie"].get_rect()  # Obtener el rectángulo para detectar clics
    lista_botones.append(boton)

# Fondo del menú
fondo = pygame.image.load("fondo.jpg")  # Cargar la imagen de fondo
fondo = pygame.transform.scale(fondo, VENTANA)  # Escalar la imagen al tamaño de la ventana

# Definimos las variables globales para volumen y dificultad
dificultad_seleccionada = "Normal"  # Dificultad predeterminada
volumen = 0.5  # Volumen predeterminado (valor entre 0 y 1)

# Nuevas funciones
def pantalla_opciones(pantalla: pygame.Surface, cola_eventos: list) -> str:
    """
    Muestra la pantalla de opciones donde el jugador puede elegir la dificultad y el volumen.
    :param pantalla: Superficie principal.
    :param cola_eventos: Lista de eventos actuales.
    :return: Nombre de la siguiente ventana o acción.
    """
    retorno = "opciones"
    fuente_opciones = pygame.font.SysFont("Arial Narrow", 30)

    fondo_opciones = pygame.image.load("fondo_opciones.jpg")
    fondo_opciones = pygame.transform.scale(fondo_opciones, VENTANA)

    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(2):  # Solo tenemos dos botones en opciones
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()  # Reproducir el sonido de clic

                    if i == 0:  # Volumen
                        volumen = 1.0 if volumen == 0.5 else 0.5
                        pygame.mixer.music.set_volume(volumen)
                    elif i == 1:  # Dificultad
                        if dificultad_seleccionada == "Normal":
                            dificultad_seleccionada = "Difícil"
                        elif dificultad_seleccionada == "Difícil":
                            dificultad_seleccionada = "Fácil"
                        else:
                            dificultad_seleccionada = "Normal"

        elif evento.type == pygame.QUIT:
            retorno = "salir"

    pantalla.blit(fondo_opciones, (0, 0))

    posiciones_opciones = [(125, 100), (125, 180)]  # Posiciones de los botones
    textos_opciones = [f"Volumen: {'Alto' if volumen == 1.0 else 'Bajo'}", f"Dificultad: {dificultad_seleccionada}"]

    for i in range(2):
        lista_botones[i]["rectangulo"] = pantalla.blit(lista_botones[i]["superficie"], posiciones_opciones[i])
        mostrar_texto(lista_botones[i]["superficie"], textos_opciones[i], (30, 10), fuente_opciones, COLOR_BLANCO)

    return retorno

def mostrar_menu(pantalla: pygame.Surface, cola_eventos: list) -> str:
    """
    Muestra el menú principal y gestiona la navegación.
    :param pantalla: Superficie principal.
    :param cola_eventos: Lista de eventos actuales.
    :return: Nombre de la siguiente ventana o acción.
    """
    retorno = "menu"

    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()  # Reproducir el sonido de clic

                    # Lógica para los botones en el menú
                    if i == BOTON_SALIR:
                        retorno = "salir"
                    elif i == BOTON_JUGAR:
                        retorno = "juego"
                    elif i == BOTON_PUNTUACIONES:
                        retorno = "rankings"
                    elif i == BOTON_CONFIG:
                        retorno = "configuraciones"
                    elif i == BOTON_AGREGAR:
                        retorno = "agregar_preguntas"
                    elif i == BOTON_OPCIONES:
                        retorno = "opciones"  # Accede a la pantalla de opciones

        elif evento.type == pygame.QUIT:
            retorno = "salir"

    # Dibuja el fondo y los botones
    pantalla.blit(fondo, (0, 0))  # Fondo del menú
    posiciones_botones = [(125, 100), (125, 180), (125, 260), (125, 340), (125, 420), (125, 500)]  # Posiciones de los botones
    textos_botones = ["JUGAR", "CONFIGURACIÓN", "PUNTUACIONES", "SALIR", "AGREGAR PREGUNTAS", "OPCIONES"]  # Textos de los botones

    for i in range(len(lista_botones)):
        lista_botones[i]["rectangulo"] = pantalla.blit(lista_botones[i]["superficie"], posiciones_botones[i])
        mostrar_texto(lista_botones[i]["superficie"], textos_botones[i], (30, 10), fuente_menu, COLOR_BLANCO)

    return retorno
