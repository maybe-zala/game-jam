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

# INITIALIZE PYGAME AND SCREEN
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spritesheets")

# LOAD SPRITES
animation_list = load_sunflower_animations()

# GAME VARIABLES
action = 2  # 0: talking, 1:excited, 2:idle
last_update = pygame.time.get_ticks()
animation_cooldown = 220
frame = 0

# MAIN GAME LOOP
running = True
while running:
    
    # Update background
    screen.fill((20, 20, 20))      
    
    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
         frame += 1
         if frame >= len(animation_list[action]):
              frame = 0
         last_update = current_time

    # Show frame image
    screen.blit(animation_list[action][frame], (0, 0))

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list)-1:
                action += 1
                frame = 0
      
    pygame.display.flip()

pygame.quit()