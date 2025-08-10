from GameObject import GameObject

class Item(GameObject):
    COLORS = {
        "blue": (0, 0, 255),
        "red": (255, 0, 0),
        "white": (255, 255, 255)
    }
    def __init__(self, x, y, tipo):
        color = self.COLORS.get(tipo, (255, 255, 255))
        super().__init__(x, y, 20, 20, color)
        self.speed = 3
        self.tipo = tipo  #Só alterei o nome daqui para não me perder na alteração da main
    
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
