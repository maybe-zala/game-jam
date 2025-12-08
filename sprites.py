import pygame
import spritesheet

pygame.init()




screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spritesheets")

idle = pygame.image.load("spritesheets/idle.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(idle)





animation_list = []
animation_steps = 4
last_update = pygame.time.get_ticks()
animation_cooldown = 300
frame = 0

for x in range(animation_steps):
        animation_list.append(sprite_sheet.get_image(x, 50, 100, 3, (0, 0, 0)))


running = True
while running:
    
    #update background
    screen.fill((20, 20, 20))      
    
    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
         frame += 1
         last_update = current_time
         if frame >= len(animation_list):
              frame = 0

    #show frame image
    screen.blit(animation_list[frame],(0, 0))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()