import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    
    #Cria a janela do jogo
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Clone, by Francisco Goya")
    
    clock = pygame.time.Clock()
    dt = 0 #Delta time (tempo entre frames)

    #Criação dos grupos de objetos
    updatable = pygame.sprite.Group() #Objetos que serão atualizados
    drawable = pygame.sprite.Group()  #Objetos que serão desenhados
    asteroids = pygame.sprite.Group() #Grupo específico para asteroides
    shots = pygame.sprite.Group()  # Grupo de balas

    #Configura os containers para os objetos do jogo
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    #Cria os objetos do jogo
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  #Cria o jogador no centro da tela
    asteroid_field = AsteroidField()  #Inicia o campo de asteroide

    #Inicializa o score do jogo
    score = 0
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  #Sai do loop se o usuário fechar a janela
        
        #Cria o disparo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:  #Se a tecla espaço for pressionada
            shot = player.shoot()  #Cria uma nova bala
            if shot:
                shots.add(shot)  #Adiciona a bala ao grupo
        
        updatable.update(dt)  #Atualiza todos os objetos do grupo "updatable"

        #Verifica colisão entre o player e os asteroides
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over! Final Score:", score)
                return  #Sai do jogo
        
        #Verifica colisão entre asteroides e balas
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):  #Se colidir
                    score += asteroid.get_score()  #Atualiza o score
                    asteroid.split()  #Divide o asteroide
                    shot.kill()  #Destrói a bala

        screen.fill((0, 0, 0))  #Preenche a tela com preto
        
        for obj in drawable:  #Desenha todos os objetos do grupo "drawable"
            obj.draw(screen)

        #Desenha o score na tela
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()  #Atualiza a tela
        dt = clock.tick(60) / 1000 # Controla o FPS e calcula o delta time


if __name__ == "__main__":
    main()
