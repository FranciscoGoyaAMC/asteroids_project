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

    def reset_game():
        """Função para reiniciar o jogo"""
        nonlocal game_over, player, asteroid_field, score
        game_over = False
        score = 0

        #Reinicializa os grupos
        updatable.empty()
        drawable.empty()
        asteroids.empty()
        shots.empty()

        #Recria os objetos do jogo
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroid_field = AsteroidField()

    #Criação dos grupos de objetos
    updatable = pygame.sprite.Group() #Objetos que serão atualizados
    drawable = pygame.sprite.Group()  #Objetos que serão desenhados
    asteroids = pygame.sprite.Group() #Grupo específico para asteroides
    shots = pygame.sprite.Group()  #Grupo de balas

    #Configura os containers para os objetos do jogo
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    #Cria os objetos do jogo
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  #Cria o jogador no centro da tela
    asteroid_field = AsteroidField()  #Inicia o campo de asteroide

    #Inicializa os objetos do jogo
    player = None
    asteroid_field = None
    score = 0
    font = pygame.font.Font(None, 36)

    #Variável de controle do estado do jogo
    game_over = False
    reset_game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  #Sai do loop se o usuário fechar a janela
        
        if game_over:
            #Exibe tela de Game Over e espera input para reiniciar
            screen.fill((0, 0, 0))
            game_over_text = font.render(f"Game Over! Score: {score}", True, (255, 255, 255))
            retry_text = font.render("Pressione 'R' para reiniciar", True, (255, 255, 255))
            
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))
            screen.blit(retry_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20))
            
            pygame.display.flip()

            #Aguarda o jogador pressionar "R" para reiniciar
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                reset_game()
            
            clock.tick(30)  #Reduz a taxa de atualização enquanto aguarda input
            continue  #Pula o restante do loop e volta para a verificação de eventos
        
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
                player.lives -= 1  #Diminui uma vida
                if player.lives > 0:
                    player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  #Respawna o jogador
                else:
                    game_over = True  #Sinaliza o fim do jogo
        
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

        #Mostra a quantidade de vidas na tela
        lives_text = font.render(f"Lives: {player.lives}", True, (255, 255, 255))
        screen.blit(lives_text, (SCREEN_WIDTH - 100, 10))

        pygame.display.flip()  #Atualiza a tela
        dt = clock.tick(60) / 1000 # Controla o FPS e calcula o delta time


if __name__ == "__main__":
    main()
