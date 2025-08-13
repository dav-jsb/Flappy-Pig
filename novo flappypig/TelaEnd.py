import pygame
from Consts import Cores
from TelaBase import TelaBase

class TelaEnd(TelaBase):
    def __init__(self, width, height, game_manager, assets=None):
        super().__init__(width, height)
        self.manager = game_manager

        if assets and "game_over_screen" in assets:
            end_image = assets["game_over_screen"]
        else:
            end_image = pygame.image.load("game_over.png").convert_alpha()
        self.end_image = pygame.transform.smoothscale(end_image, (self.width, self.height))

        # fonte dos números
        self.font_num = pygame.font.SysFont("Arial", 22)

        self.anchors = {
            "cenouras": (0.78, 0.650),
            "carne":    (0.78, 0.680),
            "magia":    (0.78, 0.711), 
            "fogo":     (0.78, 0.740),   
            "aranha":   (0.78, 0.771),   
        }

    def handle_events(self, events):
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
        # fundo
        self.screen.blit(self.end_image, (0, 0))

        values = {
            "cenouras": self.manager.score_yellow, #carrots
            "carne": self.manager.score_green, #Meals
            "magia":  self.manager.score_blue,   # wizard hat
            "fogo":   self.manager.score_red,    # fire
            "aranha": self.manager.score_white,  # spider
        }

        # desenha cada número na âncora correspondente
        for key, val in values.items():
            ax, ay = self.anchors[key]
            txt = self.font_num.render(str(val), True, (30, 20, 10)) #Se quiser mexer na cor dos números, alterar aqui!
            rect = txt.get_rect(midleft=(int(self.width*ax), int(self.height*ay)))
            self.screen.blit(txt, rect)
