import pygame

from configuracoes import WIDTH, HEIGHT, INIT, GAME, QUIT, FIM
from telas import init_screen
from telas import game_screen
from telas import end_game


# InicializaÃ§Ã£o do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Pitfall")

# Comando para evitar travamentos.
try:
    STATE = INIT
    while STATE != QUIT:
        if STATE == INIT:
            STATE = init_screen(screen)
        elif STATE == GAME:
            STATE, tesouro = game_screen(screen)
        elif STATE == FIM:
            STATE = end_game(screen,tesouro)
        else:
            STATE = QUIT
finally:
    pygame.quit()
