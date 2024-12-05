import pygame
from Constantes import *
from Funciones import mostrar_texto, cargar_preguntas_csv, guardar_preguntas_csv

pygame.init()

fuente_titulo = pygame.font.SysFont("Arial Narrow", 40)
fuente_boton = pygame.font.SysFont("Arial Narrow", 25)
fuente_texto = pygame.font.SysFont("Arial Narrow", 20)

# Botones
boton_volver = {"superficie": pygame.Surface(TAMAÑO_BOTON_VOLVER), "rectangulo": None}
boton_volver["superficie"].fill(COLOR_AZUL)

boton_agregar_manual = {"superficie": pygame.Surface(TAMAÑO_BOTON), "rectangulo": None}
boton_agregar_manual["superficie"].fill(COLOR_VERDE)

boton_cargar_csv = {"superficie": pygame.Surface(TAMAÑO_BOTON), "rectangulo": None}
boton_cargar_csv["superficie"].fill(COLOR_VERDE)

# Cuadros de texto para ingresar preguntas manuales
cuadros_texto = [
    {"superficie": pygame.Surface(CUADRO_TEXTO), "rectangulo": None, "texto": ""},
    {"superficie": pygame.Surface(CUADRO_TEXTO), "rectangulo": None, "texto": ""},
    {"superficie": pygame.Surface(CUADRO_TEXTO), "rectangulo": None, "texto": ""},
    {"superficie": pygame.Surface(CUADRO_TEXTO), "rectangulo": None, "texto": ""},
]
for cuadro in cuadros_texto:
    cuadro["superficie"].fill(COLOR_GRIS_CLARO)

campo_foco = None

# Ventana
def mostrar_agregar_preguntas(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    global campo_foco
    retorno = "agregarpreguntas"
    mensaje = ""  # Mensaje para mostrar al usuario

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
            elif boton_agregar_manual["rectangulo"].collidepoint(evento.pos):
                # Verificar si todos los campos están llenos
                if all(cuadro["texto"] for cuadro in cuadros_texto):
                    nueva_pregunta = {
                        "pregunta": cuadros_texto[0]["texto"],
                        "respuesta_1": cuadros_texto[1]["texto"],
                        "respuesta_2": cuadros_texto[2]["texto"],
                        "respuesta_3": cuadros_texto[3]["texto"],
                        "respuesta_correcta": 1,  # Por defecto (puedes añadir lógica para elegir)
                    }
                    guardar_preguntas_csv([nueva_pregunta])  # Guardar en el archivo CSV
                    mensaje = "Pregunta agregada exitosamente."
                    for cuadro in cuadros_texto:
                        cuadro["texto"] = ""
                        cuadro["superficie"].fill(COLOR_GRIS_CLARO)
                else:
                    mensaje = "Por favor, complete todos los campos."
            elif boton_cargar_csv["rectangulo"].collidepoint(evento.pos):
                # Pedir al usuario que ingrese un path al archivo CSV
                path = input("Ingrese el path del archivo CSV: ")
                if path:
                    try:
                        cargar_preguntas_csv(path)  # Cargar preguntas desde el archivo
                        mensaje = "Preguntas cargadas exitosamente."
                    except Exception as e:
                        mensaje = f"Error: {str(e)}"
            else:
                # Verificar si se hizo clic en algún cuadro de texto
                for i, cuadro in enumerate(cuadros_texto):
                    if cuadro["rectangulo"].collidepoint(evento.pos):
                        campo_foco = i
                        break
                else:
                    campo_foco = None
        elif evento.type == pygame.KEYDOWN and campo_foco is not None:
            if evento.key == pygame.K_BACKSPACE:
                cuadros_texto[campo_foco]["texto"] = cuadros_texto[campo_foco]["texto"][:-1]
            elif len(cuadros_texto[campo_foco]["texto"]) < 50:
                cuadros_texto[campo_foco]["texto"] += evento.unicode
            cuadros_texto[campo_foco]["superficie"].fill(COLOR_GRIS_CLARO)

    # Dibujar en pantalla
    pantalla.fill(COLOR_BLANCO)
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"], (10, 10))
    mostrar_texto(boton_volver["superficie"], "VOLVER", (10, 10), fuente_boton, COLOR_BLANCO)

    mostrar_texto(pantalla, "AGREGAR PREGUNTAS", (180, 10), fuente_titulo, COLOR_NEGRO)

    # Dibujar campos para preguntas manuales
    posiciones = [(50, 100), (50, 160), (50, 220), (50, 280)]
    etiquetas = ["Pregunta:", "Respuesta 1:", "Respuesta 2:", "Respuesta 3:"]
    for i, (cuadro, pos, etiqueta) in enumerate(zip(cuadros_texto, posiciones, etiquetas)):
        cuadro["rectangulo"] = pantalla.blit(cuadro["superficie"], pos)
        mostrar_texto(cuadro["superficie"], cuadro["texto"], (10, 10), fuente_texto, COLOR_NEGRO)
        mostrar_texto(pantalla, etiqueta, (pos[0], pos[1] - 20), fuente_texto, COLOR_NEGRO)

    # Botones para agregar preguntas
    boton_agregar_manual["rectangulo"] = pantalla.blit(boton_agregar_manual["superficie"], (400, 340))
    mostrar_texto(boton_agregar_manual["superficie"], "AGREGAR MANUAL", (10, 10), fuente_boton, COLOR_BLANCO)

    boton_cargar_csv["rectangulo"] = pantalla.blit(boton_cargar_csv["superficie"], (400, 400))
    mostrar_texto(boton_cargar_csv["superficie"], "CARGAR CSV", (10, 10), fuente_boton, COLOR_BLANCO)

    # Mensaje para el usuario
    if mensaje:
        mostrar_texto(pantalla, mensaje, (50, 450), fuente_texto, COLOR_ROJO)

    return retorno

