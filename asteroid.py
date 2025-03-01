import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    """Inicializa um novo asteroide na posição (x, y) com um raio específico"""
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) #Chama o construtor da classe pai
    

    def draw(self, screen):
        """Desenha o asteroide na tela como um círculo"""
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)


    def update(self, dt):
        """Atualiza a posição do asteroide, movendo-o em linha reta com velocidade constante"""
        self.position += self.velocity * dt  #Move o asteroide de acordo com sua velocidade

    
    def split(self):
        """Divide o asteroide em dois novos asteroides."""
        self.kill()  #Remove o asteroide atual

        #Se o asteroide for pequeno o suficiente, não divida, apenas o destrua
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        #Calcula o novo raio dos asteroides
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #Gera um ângulo aleatório para a rotação dos asteroides divididos
        random_angle = random.uniform(20, 50)

        #Cria duas novas velocidades, uma com rotação positiva e outra com rotação negativa
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        #Cria dois novos asteroides com o novo raio e nova velocidade
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2
