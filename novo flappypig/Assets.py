import pygame

def load_assets():
    assets = {}

    # Itens
    assets["blue_item"] = pygame.image.load("assets/wizard powerup.png").convert_alpha() #Wizard Hat
    assets["red_item"] = pygame.image.load("assets/fire powerup.png").convert_alpha() #Fire
    assets["white_item"] = pygame.image.load("assets/spider powerup.png").convert_alpha() #Widow item
    assets['green_item'] = pygame.image.load("assets/carrot.png").convert_alpha() #carrot
    assets['yellow_item'] = pygame.image.load("assets/meal.png").convert_alpha() # meal 

    # Skins do porco
    assets["pig_default"] = pygame.image.load("assets/pig_default.png").convert_alpha()
    assets["pig_white"] = pygame.image.load("assets/spider_pig.png").convert_alpha()
    assets["pig_blue"] = pygame.image.load("assets/wizard_pig.png").convert_alpha()
    assets["pig_red"] = pygame.image.load("assets/blazed_pig.png").convert_alpha()

    #Imagem de End
    assets["game_over_screen"] = pygame.image.load("assets/game_over.png").convert_alpha()

    #Fundo do jogo
    assets["nuvens"] = pygame.image.load("assets/nuvens.png").convert_alpha()
    assets["terreno"] = pygame.image.load("assets/terreno.png").convert_alpha()

    return assets

