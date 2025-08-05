class GameState:
    MENU = 0
    PLAYING = 1
    GAME_OVER = 2

class GameManager:
    def __init__(self):
        self.state = GameState.MENU
        self.score = 0
        self.high_score = 0
    
    def reset(self):
        self.score = 0
        self.state = GameState.PLAYING
    
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.state = GameState.GAME_OVER