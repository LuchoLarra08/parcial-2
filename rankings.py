import pygame
from Constantes import *
from Funciones import mostrar_texto

pygame.init()

# Fuentes y botón
fuente = pygame.font.SysFont("Arial Narrow", 32)
fuente_boton = pygame.font.SysFont("Arial Narrow", 23)
boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_AZUL)

def mostrar_rankings(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]):
    """
    Muestra los rankings en pantalla y gestiona los eventos.
    
    :param pantalla: Superficie principal donde se dibujan los rankings.
    :param cola_eventos: Lista de eventos de pygame.
    :return: Estado de la ventana ("rankings", "menu" o "salir").
    """
    retorno = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
    
    # Dibujar fondo y botón volver
    pantalla.fill(COLOR_BLANCO)
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"], (10, 10))
    mostrar_texto(boton_volver["superficie"], "VOLVER", (10, 10), fuente_boton, COLOR_BLANCO)
    
    # Mostrar el Top 10 (puedes reemplazar este texto con datos reales si ya los tienes)
    mostrar_texto(pantalla, "ACA SE DEBE MOSTRAR EL TOP 10", (50, 200), fuente, COLOR_NEGRO)
    
    return retorno
