from GameObject import GameObject

class Item(GameObject):
    COLORS = {
        "blue": (0, 0, 255),
        "red": (255, 0, 0),
        "white": (255, 255, 255)
    }
    def __init__(self, x, y, tipo,image_item):
        color = None
        super().__init__(x, y, 20, 20, color,image_item)
        self.speed = 3
        self.tipo = tipo  #Só alterei o nome daqui para não me perder na alteração da main
    
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
