import pygame

def load_assets():
    assets = {}

    # Itens
    assets["blue_item"] = pygame.image.load("wizard powerup.png").convert_alpha()
    assets["red_item"] = pygame.image.load("fire powerup.png").convert_alpha()
    assets["white_item"] = pygame.image.load("spider powerup.png").convert_alpha()
    assets['green_item'] = pygame.image.load("carrot.png").convert_alpha() #carrot
    assets['yellow_item'] = pygame.image.load("meal.png").convert_alpha() # meal 

    # Skins do porco
    assets["pig_default"] = pygame.image.load("vanilla pig.png").convert_alpha()
    assets["pig_white"] = pygame.image.load("spider powerup.png").convert_alpha()
    assets["pig_blue"] = pygame.image.load("wizardpig.png").convert_alpha()
    assets["pig_red"] = pygame.image.load("blaze pig.png").convert_alpha()

    return assets
