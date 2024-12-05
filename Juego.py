import pygame
import random
from Constantes import WIDTH, HEIGHT, COLOR_AZUL, COLOR_BLANCO, COLOR_NEGRO, FPS
from Funciones import mostrar_texto, guardar_puntuacion  # Asegúrate de tener estas funciones importadas desde Funciones.py
from Terminado import mostrar_fin_juego  # Importa la función para la pantalla final

# Inicializar pygame
pygame.init()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Preguntados Boom")
reloj = pygame.time.Clock()

# Cargar fondo
try:
    fondo = pygame.image.load("fondo.jpg")
    fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))
except pygame.error as e:
    print(f"Error cargando la imagen: {e}")
    pygame.quit()
    exit()

# Preguntas y respuestas
preguntas = [
    {"pregunta": "¿Cuál es la capital de Francia?", "opciones": ["París", "Londres", "Roma", "Berlín"], "respuesta": "París"},
    {"pregunta": "¿Cuánto es 5 * 3?", "opciones": ["8", "15", "10", "20"], "respuesta": "15"},
    {"pregunta": "¿Quién pintó la Mona Lisa?", "opciones": ["Leonardo da Vinci", "Van Gogh", "Picasso", "Miguel Ángel"], "respuesta": "Leonardo da Vinci"}
]

# Cargar sonidos
CLICK_SONIDO = pygame.mixer.Sound("click.mp3")
ERROR_SONIDO = pygame.mixer.Sound("error.mp3")  # Sonido para respuesta incorrecta

# Cargar música de fondo (por defecto con volumen bajo)
pygame.mixer.music.load("game_music.mp3")
pygame.mixer.music.set_volume(0.5)  # Volumen predeterminado
pygame.mixer.music.play(-1, 0.0)

# Funciones para manejar las pantallas
def pantalla_menu():
    """Pantalla inicial con las opciones de Jugar y Salir."""
    while True:
        pantalla.blit(fondo, (0, 0))
        
        # Título de la pantalla de menú
        mostrar_texto(pantalla, "Preguntados Boom", (WIDTH // 2, 100), pygame.font.SysFont("Arial", 50), COLOR_BLANCO, centrar=True)
        
        # Botones con el mismo estilo que las opciones en el juego
        jugar_rect = pygame.Rect(WIDTH // 2 - 100, 250, 200, 50)
        salir_rect = pygame.Rect(WIDTH // 2 - 100, 350, 200, 50)
        pygame.draw.rect(pantalla, (0, 0, 0, 0), jugar_rect)
        pygame.draw.rect(pantalla, COLOR_BLANCO, jugar_rect, 3)
        pygame.draw.rect(pantalla, (0, 0, 0, 0), salir_rect)
        pygame.draw.rect(pantalla, COLOR_BLANCO, salir_rect, 3)

        mostrar_texto(pantalla, "Jugar", jugar_rect.center, pygame.font.SysFont("Arial", 30), COLOR_BLANCO, centrar=True)
        mostrar_texto(pantalla, "Salir", salir_rect.center, pygame.font.SysFont("Arial", 30), COLOR_BLANCO, centrar=True)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if jugar_rect.collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    return
                elif salir_rect.collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    pygame.quit()
                    exit()

def pantalla_juego(dificultad_seleccionada, volumen):
    """Pantalla donde se desarrollará el juego."""
    puntuacion = 0
    vidas = 3
    indice_actual = random.randint(0, len(preguntas) - 1)
    pregunta_actual = preguntas[indice_actual]

    # Ajustar el tiempo límite según la dificultad
    if dificultad_seleccionada == "Fácil":
        tiempo_limite = 15  # Más tiempo
    elif dificultad_seleccionada == "Difícil":
        tiempo_limite = 5  # Menos tiempo
    else:
        tiempo_limite = 10  # Tiempo normal

    tiempo_inicio = pygame.time.get_ticks()  # Tiempo en milisegundos
    tiempo_restante = tiempo_limite * 1000  # Convertimos a milisegundos

    # Ajustar el volumen de la música
    pygame.mixer.music.set_volume(volumen)

    while vidas > 0:
        pantalla.blit(fondo, (0, 0))
        mostrar_texto(pantalla, f"Puntuación: {puntuacion}", (10, 10), pygame.font.SysFont("Arial", 24), COLOR_BLANCO)
        mostrar_texto(pantalla, f"Vidas: {vidas}", (WIDTH - 100, 10), pygame.font.SysFont("Arial", 24), COLOR_BLANCO)
        
        mostrar_texto(pantalla, pregunta_actual["pregunta"], (WIDTH // 2, 150), pygame.font.SysFont("Arial", 30), COLOR_BLANCO, centrar=True)
        
        opciones_rect = []
        for i, opcion in enumerate(pregunta_actual["opciones"]):
            rect = pygame.Rect(WIDTH // 2 - 100, 250 + i * 70, 200, 50)
            pygame.draw.rect(pantalla, (0, 0, 0, 0), rect)  # Fondo transparente
            pygame.draw.rect(pantalla, COLOR_BLANCO, rect, 3)  # Borde blanco
            mostrar_texto(pantalla, opcion, rect.center, pygame.font.SysFont("Arial", 24), COLOR_BLANCO, centrar=True)  # Color blanco
            opciones_rect.append(rect)

        # Mostrar el temporizador
        tiempo_restante = tiempo_limite * 1000 - (pygame.time.get_ticks() - tiempo_inicio)
        if tiempo_restante > 0:
            mostrar_texto(pantalla, f"Tiempo: {tiempo_restante // 1000}", (WIDTH // 2, HEIGHT - 50), pygame.font.SysFont("Arial", 30), COLOR_BLANCO, centrar=True)
        else:
            ERROR_SONIDO.play()
            vidas -= 1
            indice_actual = random.randint(0, len(preguntas) - 1)
            pregunta_actual = preguntas[indice_actual]  # Nueva pregunta

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(opciones_rect):
                    if rect.collidepoint(evento.pos):
                        if pregunta_actual["opciones"][i] == pregunta_actual["respuesta"]:
                            puntuacion += 10
                        else:
                            ERROR_SONIDO.play()
                            vidas -= 1
                        indice_actual = random.randint(0, len(preguntas) - 1)
                        pregunta_actual = preguntas[indice_actual]
                        tiempo_inicio = pygame.time.get_ticks()  # Reinicia el tiempo

    return puntuacion

def pantalla_game_over(puntuacion):
    """Pantalla que aparece al perder todas las vidas y redirige a la pantalla de fin de juego."""
    cola_eventos = pygame.event.get()
    # Mostrar la pantalla de fin de juego donde se ingresa el nombre
    while True:
        retorno = mostrar_fin_juego(pantalla, cola_eventos, {"puntuacion": puntuacion}, volumen=0.5, dificultad="Normal")
        if retorno == "menu":
            break
        elif retorno == "salir":
            pygame.quit()
            exit()

dificultad_seleccionada = "Normal"  
volumen = 0.5  

while True:
    pantalla_menu()
    puntuacion = pantalla_juego(dificultad_seleccionada, volumen)
    pantalla_game_over(puntuacion)
