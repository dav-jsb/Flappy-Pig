from GameObject import GameObject

class Item(GameObject):
    def __init__(self, x, y, item_type):
        self.types = {
            "blue": (0, 0, 255),
            "red": (255, 0, 0),
            "white": (255, 255, 255)
        }
        color = self.types.get(item_type, (255, 255, 255))
        super().__init__(x, y, 20, 20, color)
        self.speed = 3
        self.type = item_type
    
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()