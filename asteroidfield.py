import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    """
    Classe responsável por gerar e gerenciar os asteroides no jogo
    Os asteroides aparecem aleatoriamente nas bordas da tela e se movem em linha reta
    """

    #Definição das bordas da tela e das direções de onde os asteroides podem surgir
    edges = [
        [
            pygame.Vector2(1, 0),  #Movimento da esquerda para a direita
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),  #Movimento da direita para a esquerda
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),  #Movimento de cima para baixo
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),  #Movimento de baixo para cima
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        """Inicializa o campo de asteroides e define o temporizador de spawn"""
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0  #Temporizador para controlar o surgimento dos asteroides

    def spawn(self, radius, position, velocity):
        """Cria um novo asteroide na posição e velocidade especificadas"""
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity  #Define a velocidade do asteroide

    def update(self, dt):
        """Atualiza o campo de asteroides, criando novos asteroides em intervalos regulares"""
        self.spawn_timer += dt  #Atualiza o temporizador de spawn

        #Se o tempo de spawn exceder a taxa definida, cria um novo asteroide
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0  #Reseta o temporizador

            #Escolhe uma borda aleatória para gerar o asteroide
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)  #Define uma velocidade aleatória
            velocity = edge[0] * speed  #Define a direção e velocidade
            velocity = velocity.rotate(random.randint(-30, 30))  #Aplica uma leve rotação aleatória
            position = edge[1](random.uniform(0, 1))  #Calcula a posição inicial
            kind = random.randint(1, ASTEROID_KINDS)  #Define o tamanho do asteroide
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)  #Cria o asteroide
            