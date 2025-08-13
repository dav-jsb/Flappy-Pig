##imports de bibliotecas
import pygame
import random
## imports de classes do jogo
from Consts import Cores
from Pig import Pig
from Pipe import Pipe
from Item import Item
from GameState import GameState,GameManager
from TelaMenu import TelaMenu
from TelaEnd import TelaEnd
from Assets import load_assets 
#adicionei esse dicionário para buscar os arquivos mais facilmente

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

        #Fonte da pontuação
        self.font = pygame.font.SysFont('Arial', 24)
        self.hud_icon_size = 26

        #Carregando os assets
        self.assets = load_assets()
        self.img_blue = self.assets["blue_item"]
        self.img_green = self.assets["green_item"]
        self.img_yellow = self.assets["yellow_item"]
        self.img_red = self.assets["red_item"]
        self.img_white = self.assets["white_item"]
        self.terreno = self.assets["terreno"]
        self.nuvens = self.assets["nuvens"]

        #Ajustando a dimensão das imagens
        self.hud_icons = {
            "blue":  pygame.transform.smoothscale(self.assets["blue_item"],  (self.hud_icon_size, self.hud_icon_size)),
            "red":   pygame.transform.smoothscale(self.assets["red_item"],   (self.hud_icon_size, self.hud_icon_size)),
            "white": pygame.transform.smoothscale(self.assets["white_item"], (self.hud_icon_size, self.hud_icon_size)),
            "yellow": pygame.transform.smoothscale(self.assets["yellow_item"], (self.hud_icon_size, self.hud_icon_size)),
            "green": pygame.transform.smoothscale(self.assets["green_item"],  (self.hud_icon_size, self.hud_icon_size))
        }

        # Grupos de sprites
        self.all_sprites = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        
        # Jogador ##Fiz alterações na imagem de carregamento, puxando de uma função criada em assets.py
        self.player = Pig(self.width//4, self.height//2, gravity, pulo,self.assets["pig_default"]) #objeto do tipo Pig, o porco do jogo
        self.all_sprites.add(self.player) 
        
        # Timers -> Separar a lógica de criação de canos e itens com tempo determinado
        self.pipe_timer = pygame.USEREVENT + 1
        self.item_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.pipe_timer, 1500)
        pygame.time.set_timer(self.item_timer, 1500)
        
        # Telas ##inicia as outras telas, com o gerenciador e o tamanho
        self.menu_screen = TelaMenu(self.width, self.height, self.manager) 
        self.game_over_screen = TelaEnd(self.width, self.height, self.manager)

    def create_pipe(self,gap_center):
        # Define onde vai ficar o centro do gap (com margens de segurança)
        top_pipe = Pipe(self.width + 60, gap_center+self.espaco_tubo//2, self.height, self.map_speed, self.color_pipe)
        bottom_pipe = Pipe(self.width + 60, 0,gap_center-self.espaco_tubo//2, self.map_speed, self.color_pipe)
        #Pipe(self.width + 60, gap_center+self.espaco_tubo//2, False, speed, color, self.height)
        self.all_sprites.add(top_pipe, bottom_pipe)
        self.pipes.add(top_pipe, bottom_pipe)

    #Função que incializa o item
    def create_item(self, center_item):
        y = center_item
        item_type = random.choice(["blue", "red", "white","yellow","green"]) #dependendo da cor o item muda
        image_key = f"{item_type}_item" #Faz toda a verificação buscando a chave no dic 
        new_item = Item(self.width + 60, y, item_type, self.assets[image_key],size=(30,30)) #alterei para buscar no dicionário a imagem
        self.items.add(new_item)
        self.all_sprites.add(new_item)

    #Função que contabiliza a pontuação
    def draw_scoreboard(self):
        x = 10
        y = 10
        gap = self.hud_icon_size + 8

        def draw_row(key, value):
            nonlocal y #A função interna vai modificar a variável y da função maior (não é muito bom de usar, mas quebra o galho)
            icon = self.hud_icons.get(key)
            # ícone
            self.screen.blit(icon, (x, y))
            # número alinhado verticalmente com o ícone
            txt = self.font.render(str(value), True, Cores.BRANCO)
            txt_y = y + (self.hud_icon_size - txt.get_height()) // 2
            self.screen.blit(txt, (x + self.hud_icon_size + 8, txt_y))
            y += gap

        draw_row("blue",  self.manager.score_blue)
        draw_row("red",   self.manager.score_red)
        draw_row("white", self.manager.score_white)
        draw_row("yellow", self.manager.score_yellow)
        draw_row("green", self.manager.score_green)

    #Função que roda o jogo
    def run_game(self): 
        running = True
        xterreno = 0
        xnuvem = 0
        while running:
            events = pygame.event.get()  # conta todos os eventos (teclas e cliques) desde o ultimo loop
            yaleatorio = random.randint(self.height // 4, 3 * self.height // 4)

            # Controles
            for event in events:
                if event.type == pygame.QUIT: ###fechar o jogo caso aperte o fechar no superior direito
                    running = False
                
                if event.type == pygame.KEYDOWN: ##apertar uma tecla
                    if self.manager.state == GameState.PLAYING: 
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w: ##apertar espaço, seta pra cima ou W -> Pular
                            self.player.jump()

                
                if event.type == self.pipe_timer and self.manager.state == GameState.PLAYING: ##gerar um cano após o timer 
                    self.create_pipe(yaleatorio)
                
                if event.type == self.item_timer and self.manager.state == GameState.PLAYING: ## mesma coisa com item
                    self.create_item(yaleatorio)
            
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
                    if f"pig_{item.tipo}" in self.assets:
                        self.player.change_skin(self.assets[f"pig_{item.tipo}"])# BUSCA A CHAVE DOS ASSETS -> CARREGA O VALOR DEFINIDO NA FUNÇÃO DOS ASSETS
                
                # Renderização
                terreno = self.assets["terreno"]
                nuvens = self.assets["nuvens"]
                self.screen.fill(Cores.AZUL_CLARO) #ceu azul
                for _ in range(3) :
                    self.screen.blit(terreno, (_ * terreno.get_width() + xterreno, (self.height//2) + 55)) #chao
                    self.screen.blit(nuvens ,(_ * nuvens.get_width() + xnuvem,0)) #nuvens no ceu
                    self.screen.blit(nuvens ,(_ * nuvens.get_width() + xnuvem,nuvens.get_height()+30 )) #nuvens no ceu
                self.all_sprites.draw(self.screen) ## colocar todos os objetos da tela
                xterreno -= 2
                xnuvem -= 1
                if (abs(xterreno) > terreno.get_width()) :
                    xterreno = 0
                if (abs(xnuvem) > nuvens.get_width()) :
                    xnuvem = 0
                #Desenhando todos os objetos e colocando na tela
                self.all_sprites.draw(self.screen)
                #Desenhando e atualizando o placar a cada loop
                self.draw_scoreboard()
            
            elif self.manager.state == GameState.GAME_OVER: 
                result = self.game_over_screen.handle_events(events) ##obter ação
                if result == False: ##encerrar
                    running = False
                elif result == "game": ##reiniciar
                    # Reset do jogo 
                    self.all_sprites.empty()
                    self.pipes.empty()
                    self.items.empty()
                    self.player = Pig(self.width//4, self.height//2,gravidade,altura_do_pulo,self.assets["pig_default"] )
                    self.all_sprites.add(self.player)
                    self.manager.state = GameState.PLAYING
                elif result == "menu": ###voltar ao menu
                    self.all_sprites.empty()
                    self.pipes.empty()
                    self.items.empty()
                    self.player = Pig(self.width//4, self.height//2,gravidade,altura_do_pulo,self.assets["pig_default"])
                    self.all_sprites.add(self.player)
                    self.manager.state = GameState.MENU
                self.game_over_screen.draw() ###tela de endgame
            pygame.display.flip() 
            self.clock.tick(self.fps) #somar o tempo
        pygame.quit()

gravidade = 0.5 #queda
altura_do_pulo = -7 ##negativo pq a tela conta pra cima como -
velocidade_mapa = 3
espaco_entre_tubo = 150
game = FlappyPig(gravidade,altura_do_pulo,Cores.VERMELHO_CANO,velocidade_mapa,espaco_entre_tubo) #cria um objeto do tipo FlappyPig
game.run_game() #inicia o jogo 
