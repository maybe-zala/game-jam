import pygame
import spritesheet

# LOAD SUNFLOWER ANIMATIONS
def load_sunflower_animations():
    sunflower = pygame.image.load("spritesheets/sunflower.png").convert_alpha()
    sprite_sheet = spritesheet.SpriteSheet(sunflower)
    
    # Base animations: talking (1-4), excited (5-11), idle (12-25)
    base_animations = []
    base_steps = [4, 7, 14]  # frames for each animation
    step_counter = 0
    # (talking 1-4, excited 5-11, idle 12-25, evolve 26-45, new idle 46-56, new excited 57-64, new talking 65-69) 
    for animation in base_steps:
        temp_img_list = []
        for _ in range(animation):
            temp_img_list.append(sprite_sheet.get_image(step_counter, 50, 100, 3, (0, 0, 0)))
            step_counter += 1
        base_animations.append(temp_img_list)
    
    # Evolve animation (26-45): 20 frames
    evolve_animation = []
    for _ in range(20):
        evolve_animation.append(sprite_sheet.get_image(step_counter, 50, 100, 3, (0, 0, 0)))
        step_counter += 1
    
    # Evolved animations: new talking (65-69), new excited (57-64), new idle (46-56)
    # Need to load in order: talking, excited, idle to match action indices 0, 1, 2
    evolved_animations = []
    
    # First load new idle (46-56): 11 frames
    new_idle = []
    for _ in range(11):
        new_idle.append(sprite_sheet.get_image(step_counter, 50, 100, 3, (0, 0, 0)))
        step_counter += 1
    
    # Then load new excited (57-64): 8 frames
    new_excited = []
    for _ in range(8):
        new_excited.append(sprite_sheet.get_image(step_counter, 50, 100, 3, (0, 0, 0)))
        step_counter += 1
    
    # Finally load new talking (65-69): 5 frames
    new_talking = []
    for _ in range(5):
        new_talking.append(sprite_sheet.get_image(step_counter, 50, 100, 3, (0, 0, 0)))
        step_counter += 1
    
    # Reorder to match action indices: [0: talking, 1: excited, 2: idle]
    evolved_animations = [new_talking, new_excited, new_idle]
    
    # Old animations: old talking (70-73), old excited (74-82), old idle (83-97)
    # Load old talking (70-73): 4 frames
    old_talking = []
    for _ in range(4):
        old_talking.append(sprite_sheet.get_image(step_counter, 50, 100, 3, (0, 0, 0)))
        step_counter += 1
    
    # Load old excited (74-82): 9 frames
    old_excited = []
    for _ in range(9):
        old_excited.append(sprite_sheet.get_image(step_counter, 50, 100, 3, (0, 0, 0)))
        step_counter += 1
    
    # Load old idle (83-103): 21 frames
    old_idle = []
    for _ in range(21):
        old_idle.append(sprite_sheet.get_image(step_counter, 50, 100, 3, (0, 0, 0)))
        step_counter += 1
    
    # Order: [0: talking, 1: excited, 2: idle]
    old_animations = [old_talking, old_excited, old_idle]
    
    # Death animation (104-116): 13 frames
    death_animation = []
    for _ in range(13):
        death_animation.append(sprite_sheet.get_image(step_counter, 50, 100, 3, (0, 0, 0)))
        step_counter += 1
    
    return base_animations, evolve_animation, evolved_animations, old_animations, death_animation

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