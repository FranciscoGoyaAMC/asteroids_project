import pygame

#Classe base para os objetos do jogo que possuem formato circular
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        """Inicializa um objeto circular na posição (x, y) com um determinado raio"""
        #Se a classe tiver um atributo 'containers', adiciona automaticamente a instância aos grupos de sprites
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        #Define a posição do objeto como um vetor bidimensional
        self.position = pygame.Vector2(x, y)
        #Inicializa a velocidade do objeto como um vetor (0, 0) por padrão
        self.velocity = pygame.Vector2(0, 0)
        #Define o raio do círculo
        self.radius = radius


    def draw(self, screen):
        """Método para desenhar o objeto na tela"""
        pass  # Será implementado nas subclasses


    def update(self, dt):
        """Método para atualizar a lógica do objeto"""
        pass  # Será implementado nas subclasses

    def check_collision(self, other):
        """Verifica se há colisão entre objetos"""
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
