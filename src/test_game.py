import unittest
import pygame
from configuracoes import WIDTH, HEIGHT, INIT, GAME, QUIT, FIM
from telas import init_screen, game_screen, end_game

class TestGameIntegration(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def test_init_screen(self):
        state = init_screen(self.screen)
        self.assertEqual(state, GAME)  # Supondo que GAME é o próximo estado esperado após INIT

    def test_game_screen(self):
        state, tesouro = game_screen(self.screen)
        self.assertIn(state, [QUIT, FIM])  # Supondo que o jogo pode terminar em QUIT ou FIM
        self.assertIsInstance(tesouro, int)  # Supondo que tesouro é um inteiro

    def test_end_game(self):
        tesouro = 10  # Um valor de exemplo para tesouro
        state = end_game(self.screen, tesouro)
        self.assertEqual(state, QUIT)  # Supondo que o estado seguinte de FIM é QUIT

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
