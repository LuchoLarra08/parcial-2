import pygame
from Constantes import *
from Funciones import mostrar_texto

pygame.init()

fuente_opciones = pygame.font.SysFont("Arial Narrow", 28)
fuente_boton = pygame.font.SysFont("Arial Narrow", 23)

boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_AZUL)

botones_mas_menos = []
for _ in range(3):  # Tres pares de botones (+ y -)
    boton_mas = pygame.Surface(TAMAÑO_BOTON)
    boton_mas.fill(COLOR_VERDE)
    boton_menos = pygame.Surface(TAMAÑO_BOTON)
    boton_menos.fill(COLOR_ROJO)
    botones_mas_menos.append({"mas": boton_mas, "menos": boton_menos})

# Nueva configuración para dificultad y volumen
def mostrar_opciones(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict, dificultad_seleccionada: str, volumen: float) -> str:
    """
    Muestra la pantalla de opciones donde el jugador puede elegir la dificultad y el volumen.
    :param pantalla: Superficie principal.
    :param cola_eventos: Lista de eventos actuales.
    :param datos_juego: Datos actuales del juego.
    :param dificultad_seleccionada: Dificultad seleccionada (Normal, Difícil, Fácil).
    :param volumen: Nivel de volumen actual (de 0 a 1).
    :return: Nombre de la siguiente ventana o acción.
    """
    retorno = "opciones"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"

            # Ajustar valores según los botones
            for i, boton in enumerate(botones_mas_menos):
                if pantalla.blit(boton["mas"], (400, 100 + i * 60)).collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    if i == 0:  # Ajustar puntos por acierto
                        datos_juego["puntos_acierto"] += 1
                    elif i == 1:  # Ajustar puntos por error
                        datos_juego["puntos_error"] += 1
                    elif i == 2:  # Ajustar tiempo por pregunta
                        datos_juego["tiempo_por_pregunta"] += 5
                elif pantalla.blit(boton["menos"], (460, 100 + i * 60)).collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    if i == 0 and datos_juego["puntos_acierto"] > 0:
                        datos_juego["puntos_acierto"] -= 1
                    elif i == 1 and datos_juego["puntos_error"] > 0:
                        datos_juego["puntos_error"] -= 1
                    elif i == 2 and datos_juego["tiempo_por_pregunta"] > 5:
                        datos_juego["tiempo_por_pregunta"] -= 5

            # Ajustar volumen
            if pantalla.blit(boton_volver["superficie"], (400, 300)).collidepoint(evento.pos):
                if volumen == 0.5:
                    volumen = 1.0
                else:
                    volumen = 0.5
                pygame.mixer.music.set_volume(volumen)

            # Ajustar dificultad
            if pantalla.blit(boton_volver["superficie"], (400, 400)).collidepoint(evento.pos):
                if dificultad_seleccionada == "Normal":
                    dificultad_seleccionada = "Difícil"
                elif dificultad_seleccionada == "Difícil":
                    dificultad_seleccionada = "Fácil"
                else:
                    dificultad_seleccionada = "Normal"

    # Dibujar opciones
    pantalla.fill(COLOR_BLANCO)
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"], (10, 10))
    mostrar_texto(boton_volver["superficie"], "VOLVER", (10, 10), fuente_boton, COLOR_BLANCO)

    mostrar_texto(pantalla, "Opciones de juego", (250, 20), fuente_opciones, COLOR_NEGRO)
    mostrar_texto(pantalla, f"Puntos por acierto: {datos_juego['puntos_acierto']}", (100, 100), fuente_opciones, COLOR_NEGRO)
    mostrar_texto(pantalla, f"Puntos por error: {datos_juego['puntos_error']}", (100, 160), fuente_opciones, COLOR_NEGRO)
    mostrar_texto(pantalla, f"Tiempo por pregunta: {datos_juego['tiempo_por_pregunta']} seg", (100, 220), fuente_opciones, COLOR_NEGRO)

    # Mostrar volumen y dificultad
    mostrar_texto(pantalla, f"Volumen: {'Alto' if volumen == 1.0 else 'Bajo'}", (100, 280), fuente_opciones, COLOR_NEGRO)
    mostrar_texto(pantalla, f"Dificultad: {dificultad_seleccionada}", (100, 340), fuente_opciones, COLOR_NEGRO)

    # Dibujar botones (+ y -) para cada configuración
    for i, boton in enumerate(botones_mas_menos):
        pantalla.blit(boton["mas"], (400, 100 + i * 60))
        pantalla.blit(boton["menos"], (460, 100 + i * 60))

    return retorno
