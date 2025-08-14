class GameState:
    MENU = 0
    PLAYING = 1
    GAME_OVER = 2

class GameManager:
    def __init__(self):
        self.state = GameState.MENU
        # Pontuação por tipo de item
        self.score_blue = 0
        self.score_red = 0
        self.score_white = 0
        self.score_yellow = 0
        self.score_green = 0
    #Função para resetar a pontuação após o término do jogo
    def reset(self):
        self.score_blue = 0
        self.score_red = 0
        self.score_white = 0
        self.score_yellow = 0
        self.score_green = 0
        self.state = GameState.PLAYING
    
    def game_over(self):
        self.state = GameState.GAME_OVER
    # adiciona os itens à pontuação com base no tipo de item
    def add_item_score(self, item_type):
        if item_type == "blue":
            self.score_blue += 1
        elif item_type == "red":
            self.score_red += 1
        elif item_type == "white":
            self.score_white += 1
        elif item_type == 'yellow':
            self.score_yellow += 1
        elif item_type == 'green':
            self.score_green += 1