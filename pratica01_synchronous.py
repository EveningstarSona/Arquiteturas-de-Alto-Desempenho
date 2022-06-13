'''
[1001537] Arquiteturas de Alto Desempenho

Atividade Prática 01 (Versão síncrona sem multithreading)

Sona Eveningstar Jorge Candeu, 769802
Carlos André Costa Santana, 773370

06/06/2022
'''
from math import sqrt, pi
import pygame as pg
from random import random
import time

dot = tuple[float, float]


def distance_from_center(point: dot) -> float:
    return sqrt((WIDTH/2 - point[0])**2 + (HEIGHT/2 - point[1])**2)


def generate_point() -> dot:
    return (random()*CIRCLE_RADIUS*2+CIRCLE_RADIUS/2, random()*CIRCLE_RADIUS*2+CIRCLE_RADIUS/2)


def pixel(WINDOW, color, pos):
    WINDOW.fill(color, (pos, (1, 1)))


WIDTH = HEIGHT = 600
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
CIRCLE_RADIUS = 200


def initial_draw(WINDOW: pg.Surface):
    WINDOW.fill(WHITE)
    pg.draw.circle(WINDOW, BLACK, (WIDTH/2, HEIGHT/2), CIRCLE_RADIUS, width=1)
    pg.draw.rect(WINDOW, BLACK, (WIDTH/2 - CIRCLE_RADIUS, HEIGHT/2 - CIRCLE_RADIUS,
                                 CIRCLE_RADIUS*2, CIRCLE_RADIUS*2), width=1)
    pg.draw.line(WINDOW, BLACK, (0, HEIGHT/2), (WIDTH, HEIGHT/2))
    pg.draw.line(WINDOW, BLACK, (WIDTH/2, 0), (WIDTH/2, HEIGHT))


def draw_point(WINDOW: pg.Surface, point: dot):
    pixel(WINDOW, RED, point)


def update(points: list[dot]) -> dot:
    new_point = generate_point()
    points.append(new_point)
    return new_point


def main(DOTS: int):
    pg.init()
    points = []
    WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Método de Monte Carlo para aproximar pi")
    initial_draw(WINDOW)

    # Loop principal
    start_time = time.time()
    for _ in range(DOTS):
        point = update(points)
        draw_point(WINDOW, point)
        pg.display.flip()
    end_time = time.time()
    print('O tempo decorrido total de forma síncrona foi:', end_time - start_time)
    inside = [p for p in points if distance_from_center(p) < CIRCLE_RADIUS]
    print(f'Pontos: {len(points)}\nPontos dentro do círculo: {len(inside)}\nValor aproximado de pi: {4*len(inside)/len(points)}\n')
    return end_time - start_time, abs(pi - 4*len(inside)/len(points))


# Boas práticas
if __name__ == '__main__':
    main(100000)
