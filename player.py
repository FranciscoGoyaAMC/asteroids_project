import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) #Chama o construtor da classe pai
        self.rotation = 0 #Rotação inicial
        self.shoot_timer = 0 #Inicializa o timer do cooldown das balas em 0


    def triangle(self):
        """Calcula os três pontos do triângulo que representa a nave"""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def draw(self, screen):
        """Desenha a nave na tela"""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def rotate(self, dt, clockwise=True):
        """Rotaciona o jogador com base no delta time"""
        direction = 1 if clockwise else -1
        self.rotation += PLAYER_TURN_SPEED * dt * direction
    

    def update(self, dt):
        """Atualiza o jogador e o timer de cooldown."""

        #Atualiza o timer de cooldown, diminuindo com base no delta time
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        #Atualiza a rotação do jogador com base na entrada do teclado
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  #Girar para a esquerda
            self.rotate(dt, clockwise=False)
        if keys[pygame.K_d]:  #Girar para a direita
            self.rotate(dt, clockwise=True)
        if keys[pygame.K_w]: #Mover para frente
            self.move(dt, forward=True)
        if keys[pygame.K_s]: #Mover para trás
            self.move(dt, forward=False)


    def move(self, dt, forward=True):
        """Move o jogador na direção que ele está apontando"""
        direction = 1 if forward else -1 #Define a direção do movimento
        forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward_vector * PLAYER_SPEED * dt * direction


    def shoot(self):
        """Cria uma bala na posição do jogador, respeitando o cooldown"""
        if self.shoot_timer <= 0:  #Se o cooldown estiver 0 ou negativo, podemos disparar
            shot = Shot(self.position.x, self.position.y, self.rotation)
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN  #Reseta o timer para o cooldown
            return shot
        return None
