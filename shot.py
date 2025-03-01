import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED


    def update(self, dt):
        """Atualiza a posição da bala com base na sua velocidade"""
        self.position += self.velocity * dt


    def draw(self, screen):
        """Desenha a bala na tela como um círculo"""
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
