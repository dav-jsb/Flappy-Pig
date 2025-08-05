# Bibliotecas 
import pygame
import random

# Arquivos do jogo
import Pig
import Tubo
import Item

# Configurações Iniciais
pygame.init()
LARGURA, ALTURA = 400, 600
screen = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

# Cores Teste
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Variáveis Globais
gravidade = 0.5
velocidade_mapa = 3


# Função para criar os Tubos
def criar_tubos():
    y = random.randint(150, 450)
    tubo_cima = Tubo(LARGURA + 50, y, True,VERDE,velocidade_mapa)
    tubo_baixo = Tubo(LARGURA + 50, y, False,VERDE,velocidade_mapa)
    tubos.add(tubo_cima, tubo_baixo)
    todos_sprites.add(tubo_cima, tubo_baixo)

# Função para criar os Itens
def criar_item():
    y = random.randint(100, 500)
    cor = random.choice([AZUL, VERMELHO, BRANCO])
    item = Item(LARGURA + 50, y, cor)
    itens.add(item)
    todos_sprites.add(item)

# Função para o Fim do Jogo
def game_over(pontuacao):
    fonte_grande = pygame.font.SysFont('Arial', 40)
    fonte_pequena = pygame.font.SysFont('Arial', 20)

    perdeu_texto = fonte_grande.render('VOCÊ PERDEU!', True, BRANCO)
    pontuacao_texto = fonte_pequena.render(f'Pontuação Final: {pontuacao}', True, VERDE)
    restart_texto = fonte_pequena.render('Pressione Espaço para Jogar Novamente', True, VERMELHO)

    screen.blit(perdeu_texto, perdeu_texto.get_rect(center=(LARGURA//2, ALTURA//2 - 50)))
    screen.blit(pontuacao_texto, pontuacao_texto.get_rect(center=(LARGURA//2, ALTURA//2)))
    screen.blit(restart_texto, restart_texto.get_rect(center=(LARGURA//2, ALTURA//2 + 50)))
    pygame.display.update()

    esperando_restart = True
    while esperando_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                esperando_restart = False

# Loop Principal do jogo
def main():
    global todos_sprites, tubos, itens
    pontuacao = 0

    todos_sprites = pygame.sprite.Group()
    tubos = pygame.sprite.Group()
    itens = pygame.sprite.Group()

    porco = Pig(100, ALTURA // 2)
    todos_sprites.add(porco)

    TIMER_TUBOS = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER_TUBOS, 1500)
    TIMER_ITENS = pygame.USEREVENT + 2
    pygame.time.set_timer(TIMER_ITENS, 3000)

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == TIMER_TUBOS:
                criar_tubos()
            if event.type == TIMER_ITENS:
                criar_item()

        # Atualização das caracterísiticas gerais do jogo
        todos_sprites.update()

        # Verificação de colisão entre o porco e o tubo
        if pygame.sprite.spritecollideany(porco, tubos):
            game_over(pontuacao)
            main()

        itens_coletados = pygame.sprite.spritecollide(porco, itens, True)
        pontuacao += len(itens_coletados)

        # Desenho
        screen.fill((0, 0, 0))
        todos_sprites.draw(screen)

        # Final para mostrar a pontuação do jogador
        fonte = pygame.font.SysFont('Arial', 30)
        texto = fonte.render(f'Pontuação: {pontuacao}', True, BRANCO)
        screen.blit(texto, (10, 10))

        pygame.display.update()
main()
