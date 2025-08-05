import pygame
import random
from Pig import Pig
from Pipe import Pipe
from Item import Item
from GameState import GameState,GameManager
from TelaMenu import TelaMenu
from TelaEnd import TelaEnd

class FlappyPig:

    def __init__(self,gravity,pulo,color_pipe):
        self.gravity = gravity
        self.pulo = pulo
        self.color_pipe = color_pipe
        pygame.init()
        self.width = 400
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flappy Pig")
        
        self.manager = GameManager()
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        # Grupos de sprites
        self.all_sprites = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        
        # Jogador
        self.player = Pig(self.width//4, self.height//2,gravity,pulo)
        self.all_sprites.add(self.player)
        
        # Timers
        self.pipe_timer = pygame.USEREVENT + 1
        self.item_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.pipe_timer, 1500)
        pygame.time.set_timer(self.item_timer, 3000)
        
        # Telas
        self.menu_screen = TelaMenu(self.width, self.height, self.manager)
        self.game_over_screen = TelaEnd(self.width, self.height, self.manager)
    
    def create_pipe(self):
        y = random.randint(150, 450)
        top_pipe = Pipe(self.width + 50, y, True, 3, self.color_pipe)
        bottom_pipe = Pipe(self.width + 50, y, False, 3, self.color_pipe)
        self.pipes.add(top_pipe, bottom_pipe)
        self.all_sprites.add(top_pipe, bottom_pipe)
    
    def create_item(self):
        y = random.randint(100, 500)
        item_type = random.choice(["blue", "red", "white"])
        new_item = Item(self.width + 50, y, item_type)
        self.items.add(new_item)
        self.all_sprites.add(new_item)
    
    def run_game(self):
        running = True
        while running:
            events = pygame.event.get()  # <- captura os eventos UMA vez


            # Controles
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.manager.state == GameState.PLAYING:
                        self.player.jump()
                
                if event.type == self.pipe_timer and self.manager.state == GameState.PLAYING:
                    self.create_pipe()
                
                if event.type == self.item_timer and self.manager.state == GameState.PLAYING:
                    self.create_item()
            
            # Lógica do jogo
            if self.manager.state == GameState.MENU:
                result = self.menu_screen.handle_events(events)
                if result == False:
                    running = False
                elif result == "game":
                    self.manager.state = GameState.PLAYING
                self.menu_screen.draw()
            
            elif self.manager.state == GameState.PLAYING:
                # Atualizações
                self.player.update(self.height)
                self.pipes.update()
                self.items.update()
                
                # Colisões
                if pygame.sprite.spritecollideany(self.player, self.pipes):
                    self.manager.game_over()
                
                collected = pygame.sprite.spritecollide(self.player, self.items, True)
                self.manager.score += len(collected)
                
                # Renderização
                self.screen.fill((0, 0, 0))
                self.all_sprites.draw(self.screen)
                
                # Mostra pontuação
                font = pygame.font.SysFont('Arial', 30)
                score_text = font.render(f"Score: {self.manager.score}", True, (255, 255, 255))
                self.screen.blit(score_text, (10, 10))
            
            elif self.manager.state == GameState.GAME_OVER:
                result = self.game_over_screen.handle_events(events)
                if result == False:
                    running = False
                elif result == "game":
                    # Reset do jogo
                    self.all_sprites.empty()
                    self.pipes.empty()
                    self.items.empty()
                    self.player = Pig(self.width//4, self.height//2)
                    self.all_sprites.add(self.player)
                    self.manager.state = GameState.PLAYING
                elif result == "menu":
                    self.manager.state = GameState.MENU
                
                self.game_over_screen.draw()
            
            pygame.display.flip()
            self.clock.tick(self.fps)
        
        pygame.quit()

if __name__ == "__main__":
    verde = (0,255,0)
    gravidade = 0.5
    altura_do_pulo = -7 ##negativo pq a tela conta pra cima como -
    game = FlappyPig(gravidade,altura_do_pulo,verde)
    game.run_game()