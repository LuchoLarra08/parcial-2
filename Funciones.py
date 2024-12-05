import pygame
import csv
from Constantes import WIDTH, HEIGHT, COLOR_BLANCO, COLOR_AZUL



# Función para mostrar texto en la pantalla
def mostrar_texto(superficie: pygame.Surface, texto: str, posicion: tuple, fuente: pygame.font.Font, color: tuple, centrar=False):
    """
    Muestra texto en una superficie con la opción de centrarlo.
    """
    renderizado = fuente.render(texto, True, color)
    if centrar:
        posicion = (posicion[0] - renderizado.get_width() // 2, posicion[1] - renderizado.get_height() // 2)
    superficie.blit(renderizado, posicion)

# Función para guardar puntuación en un archivo CSV
def guardar_puntuacion(nombre_archivo: str, jugador: str, puntuacion: int):
    """
    Guarda la puntuación de un jugador en un archivo CSV.
    """
    try:
        with open(nombre_archivo, mode="a", newline="") as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerow([jugador, puntuacion])  # Escribe una nueva línea con el jugador y la puntuación
            print(f"Puntuación guardada: {jugador} - {puntuacion}")
    except Exception as e:
        print(f"Error al guardar la puntuación: {e}")

def mostrar_puntuacion_alta(pantalla, puntuacion_alta):
    """Muestra la puntuación más alta en la pantalla."""
    mostrar_texto(pantalla, f"Puntuación más alta: {puntuacion_alta}", (WIDTH // 2, 300), pygame.font.SysFont("Arial", 30), COLOR_BLANCO, centrar=True)





