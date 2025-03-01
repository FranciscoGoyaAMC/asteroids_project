#Dimensões da tela
SCREEN_WIDTH = 1280  #Largura da tela em pixels
SCREEN_HEIGHT = 720  #Altura da tela em pixels

#Configurações dos asteroides
ASTEROID_MIN_RADIUS = 20  #Raio mínimo dos asteroides
ASTEROID_KINDS = 3  #Quantidade de tipos diferentes de asteroides
ASTEROID_SPAWN_RATE = 0.8  #Taxa de spawn dos asteroides (em segundos)
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS  #Raio máximo de um asteroide

#Configurações do jogador
PLAYER_RADIUS = 20  #Raio da nave do jogador
PLAYER_TURN_SPEED = 300  #Velocidade de rotação do jogador (graus por segundo)
PLAYER_SPEED = 200  #Velocidade de movimento do jogador (pixels por segundo)

#Configurações do tiro
SHOT_RADIUS = 5  #Raio das balas
PLAYER_SHOOT_SPEED = 500  #Velocidade das balas
PLAYER_SHOOT_COOLDOWN = 0.3 #Tempo de cooldown entre os disparos (em segundos)
