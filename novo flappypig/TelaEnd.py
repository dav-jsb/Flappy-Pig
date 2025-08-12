import pygame
from TelaBase import TelaBase
from Consts import Cores

class TelaEnd(TelaBase):
    def __init__(self, width, height, game_manager):
        super().__init__(width, height)
        self.manager = game_manager
        self.big_font = pygame.font.SysFont('Arial', 40)
        self.small_font = pygame.font.SysFont('Arial', 20)
    
    def handle_events(self,events):
        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.manager.reset()
                    return "game"
                if event.key == pygame.K_ESCAPE:
                    return "menu"
        return True
    def draw(self):
        self.screen.fill(Cores.PRETO)
        # Textos Finais escritos separadamente
        game_over = self.big_font.render("GAME OVER", True, Cores.VERMELHO)
        red_score = self.small_font.render(f"Fire coletados: {self.manager.score_red}", True, Cores.VERMELHO)
        white_score = self.small_font.render(f"Spider coletados: {self.manager.score_white}", True, Cores.BRANCO)
        blue_score = self.small_font.render(f"Wizard Hats coletados: {self.manager.score_blue}", True, Cores.AZUL)
        restart = self.small_font.render("Press SPACE to restart", True, Cores.VERDE)
        menu = self.small_font.render("Press ESC for menu", True, (200, 200, 200))

        # Posição inicial (verticalmente centralizado no topo) -> Para ter uma base e alterar a partir dela
        center_x = self.width // 2
        y = self.height // 4

        # Desenha cada elemento um abaixo do outro
        #GAME OVER
        self.screen.blit(game_over, (center_x - game_over.get_width() // 2, y))
        y += game_over.get_height() + 20
        #Red_score
        self.screen.blit(blue_score, (center_x - blue_score.get_width() // 2, y))
        y += blue_score.get_height() + 10
        #White_score
        self.screen.blit(red_score, (center_x - red_score.get_width() // 2, y))
        y += red_score.get_height() + 10
        #Blue_score
        self.screen.blit(white_score, (center_x - white_score.get_width() // 2, y))
        y += white_score.get_height() + 40
        #Restart
        self.screen.blit(restart, (center_x - restart.get_width() // 2, y))
        y += restart.get_height() + 10

        self.screen.blit(menu, (center_x - menu.get_width() // 2, y))
