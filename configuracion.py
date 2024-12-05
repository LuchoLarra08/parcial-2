import pygame
from Constantes import *
from Funciones import mostrar_texto

pygame.init()

# Fuentes y configuraciones iniciales
fuente = pygame.font.SysFont("Arial Narrow", 30)
fuente_boton = pygame.font.SysFont("Arial Narrow", 23)

# Botones para volver y ajustes
boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_AZUL)

def mostrar_configuracion(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict):
    """
    Ventana para modificar configuraciones del juego.
    
    :param pantalla: Superficie principal del juego.
    :param cola_eventos: Lista de eventos de pygame.
    :param datos_juego: Diccionario con datos del juego a modificar.
    :return: Estado de la ventana ("configuraciones", "menu" o "salir").
    """
    retorno = "configuraciones"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and datos_juego["volumen_musica"] < 100:
                datos_juego["volumen_musica"] += 5
            elif evento.key == pygame.K_DOWN and datos_juego["volumen_musica"] > 0:
                datos_juego["volumen_musica"] -= 5

    # Dibujar fondo y textos
    pantalla.fill(COLOR_BLANCO)
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"], (10, 10))
    mostrar_texto(boton_volver["superficie"], "VOLVER", (10, 10), fuente_boton, COLOR_BLANCO)
    
    # Mostrar opciones actuales
    mostrar_texto(pantalla, f"Volumen de la música: {datos_juego['volumen_musica']}%", (50, 200), fuente, COLOR_NEGRO)
    mostrar_texto(pantalla, "Presiona ↑ para aumentar y ↓ para disminuir", (50, 250), fuente_boton, COLOR_GRIS)

    return retorno
