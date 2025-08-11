##imports de bibliotecas
import pygame
import random
## imports de classes do jogo
from Consts import Cores
from Pig import Pig
from NewPipe import Pipe
from Item import Item
from GameState import GameState,GameManager
from TelaMenu import TelaMenu
from TelaEnd import TelaEnd

class FlappyPig:
    ##construtor da classe, os valores aqui são escolhidos ao criar um objeto nessa classe
    def __init__(self,gravity,pulo,color_pipe,map_speed,espaco_tubo):
        ##definindo os valores das variaveis da classe
        self.gravity = gravity
        self.pulo = pulo
        self.color_pipe = color_pipe
        self.map_speed = map_speed
        self.espaco_tubo = espaco_tubo
        pygame.init() #inicia o pygame
        self.width = 400 #largura da tela
        self.height = 600 # altura da tela
        self.screen = pygame.display.set_mode((self.width, self.height)) ##inicia a tela, (cria um objeto do tipo tela)
        pygame.display.set_caption("Flappy Pig") ##nome da janela
        
        self.manager = GameManager()  ##criando um objeto pra gerenciar as telas do tipo GameManager 
        self.clock = pygame.time.Clock() ## Inicia o relógio do jogo
        self.fps = 60 ##frames por segundo

        # Grupos de sprites
        self.all_sprites = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        
        # Jogador
        self.player = Pig(self.width//4, self.height//2,gravity,pulo) #objeto do tipo Pig, o porco do jogo
        self.all_sprites.add(self.player) 
        
        # Timers -> Separar a lógica de criação de canos e itens com tempo determinado
        self.pipe_timer = pygame.USEREVENT + 1
        self.item_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.pipe_timer, 1500)
        pygame.time.set_timer(self.item_timer, 1500)
        
        # Telas ##inicia as outras telas, com o gerenciador e o tamanho
        self.menu_screen = TelaMenu(self.width, self.height, self.manager) 
        self.game_over_screen = TelaEnd(self.width, self.height, self.manager)

    def create_pipe(self, gap_center):
        # Define onde vai ficar o centro do gap (com margens de segurança)
        color = self.color_pipe
        speed = 3 #Velocidade do pipe
        top_pipe = Pipe(self.width + 60, gap_center, True, speed, color, self.height)
        bottom_pipe = Pipe(self.width + 60, gap_center, False, speed, color, self.height)
        self.all_sprites.add(top_pipe, bottom_pipe)
        self.pipes.add(top_pipe, bottom_pipe)

    def create_item(self, center_item): #Modificar posteriormente para em vez de receber uma cor, receber uma imagem para trocar ao coletar
        y = center_item
        item_type = random.choice(["blue", "red", "white"])
        new_item = Item(self.width + 50, y, item_type)
        self.items.add(new_item)
        self.all_sprites.add(new_item)
    
    def run_game(self): ###loop principal do jogo
        running = True
        while running:
            events = pygame.event.get()  # conta todos os eventos (teclas e cliques) desde o ultimo loop
            gap_center_main = random.randint(self.height // 4, 3 * self.height // 4)
            # Controles
            for event in events:
                if event.type == pygame.QUIT: ###fechar o jogo caso aperte o fechar no superior direito
                    running = False
                
                if event.type == pygame.KEYDOWN: ##apertar uma tecla
                    if self.manager.state == GameState.PLAYING: 
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w: ##apertar espaço, seta pra cima ou W -> Pular
                            self.player.jump()
                 
                if event.type == self.item_timer and self.manager.state == GameState.PLAYING: ## mesma coisa com item
                    self.create_item(gap_center_main)
                
                if event.type == self.pipe_timer and self.manager.state == GameState.PLAYING: ##gerar um cano após o timer
                    self.create_pipe(gap_center_main)
                
            # Lógica do jogo
            if self.manager.state == GameState.MENU: ##o que fazer na tela de menu
                result = self.menu_screen.handle_events(events) ##resultado do menu
                if result == False:
                    running = False
                elif result == "game":
                    self.manager.state = GameState.PLAYING ##iniciar o jogo
                self.menu_screen.draw()
            
            elif self.manager.state == GameState.PLAYING: ##passar todos os objetos do jogo a cada execução do loop
                # Atualizações
                self.player.update(self.height)
                self.pipes.update()
                self.items.update()
                
                # Colisões
                if pygame.sprite.spritecollideany(self.player, self.pipes): ###colidir com um cano e perder
                    self.manager.game_over() ##mudar para o modo de endgame
                #ALTEREI AQUI PARA CONTABILIZAR OS PONTOS
                collected = pygame.sprite.spritecollide(self.player, self.items, True)
                for item in collected:
                    self.manager.add_item_score(item.tipo)
                
                # Renderização
                self.screen.fill(Cores.PRETO) ###fundo preto
                self.all_sprites.draw(self.screen) ## colocar todos os objetos da tela
                
                # Mostra pontuação SEPARADAMENTE
                font = pygame.font.SysFont('Arial', 30)
                score_blue_text = font.render(f"Blue: {self.manager.score_blue}", True, Cores.AZUL)
                score_red_text = font.render(f"Red: {self.manager.score_red}", True, Cores.VERMELHO)
                score_white_text = font.render(f"White: {self.manager.score_white}", True, Cores.BRANCO) 

                self.screen.blit(score_blue_text, (10, 10))
                self.screen.blit(score_red_text, (10, 40))
                self.screen.blit(score_white_text, (10, 70))
            
            elif self.manager.state == GameState.GAME_OVER: 
                result = self.game_over_screen.handle_events(events) ##obter ação
                if result == False: ##encerrar
                    running = False
                elif result == "game": ##reiniciar
                    # Reset do jogo
                    self.all_sprites.empty()
                    self.pipes.empty()
                    self.items.empty()
                    self.player = Pig(self.width//4, self.height//2,gravidade,altura_do_pulo)
                    self.all_sprites.add(self.player)
                    self.manager.state = GameState.PLAYING
                elif result == "menu": ###voltar ao menu
                    self.manager.state = GameState.MENU
                
                self.game_over_screen.draw() ###tela de endgame
             
            pygame.display.flip() ###tbm não sei
            self.clock.tick(self.fps) #somar o tempo
        
        pygame.quit()

gravidade = 0.5 #queda
altura_do_pulo = -7 ##negativo pq a tela conta pra cima como -
velocidade_mapa = 3
espaco_entre_tubo = 150
game = FlappyPig(gravidade,altura_do_pulo,Cores.VERDE,velocidade_mapa,espaco_entre_tubo) #cria um objeto do tipo FlappyPig
game.run_game() #inicia o jogo 
