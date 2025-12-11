import pygame
import spritesheet

# LOAD SUNFLOWER ANIMATIONS
def load_sunflower_animations():
    sunflower = pygame.image.load("spritesheets/sunflower.png").convert_alpha()
    sprite_sheet = spritesheet.SpriteSheet(sunflower)
    
    animation_list = []
    animation_steps = [4, 7, 14]
    step_counter = 0
    
    for animation in animation_steps:
        temp_img_list = []
        for _ in range(animation):
            temp_img_list.append(sprite_sheet.get_image(step_counter, 50, 100, 3, (0, 0, 0)))
            step_counter += 1
        animation_list.append(temp_img_list)
    
    return animation_list

def load_watering_can_animation():
    watering_can = pygame.image.load("spritesheets/watering can.png").convert_alpha()
    sprite_sheet = spritesheet.SpriteSheet(watering_can)
    
    animation_list = []
    animation_steps = 19
    
    for frame in range(animation_steps):
        animation_list.append(sprite_sheet.get_image(frame, 50, 100, 3, (0, 0, 0)))
    
    return animation_list

def load_plant_food_animation():
    plant_food = pygame.image.load("spritesheets/plant-food.png").convert_alpha()
    sprite_sheet = spritesheet.SpriteSheet(plant_food)
    
    animation_list = []
    animation_steps = 22
    
    for frame in range(animation_steps):
        animation_list.append(sprite_sheet.get_image(frame, 50, 100, 3, (0, 0, 0)))
    
    return animation_list