import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Sunflower")

# assets
title_image = pygame.image.load("backgrounds/title-screen.png").convert()
title_image = pygame.transform.scale(title_image, screen.get_size())

# title text styling
title_font = pygame.font.SysFont("monospace", 56)
title_color = (255, 255, 255)
title_offset = (0, -5)  # x, y offset from center

# prompt styling
prompt_font = pygame.font.SysFont("monospace", 28) 
prompt_color = (255, 220, 80)
prompt_offset = (0,80)

# credit styling
credit_font = pygame.font.SysFont("monospace", 28)
credit_color = (255, 220, 80)
credit_offset = (-105, 220)

# game state
game_start = False
text_color = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_start = True
        if event.type == pygame.QUIT:
            running = False

    if not game_start:
        screen.blit(title_image, (0, 0))
        
        # render title
        title = title_font.render("Sunflower", True, title_color)
        title_x = (screen.get_width() - title.get_width()) // 2 + title_offset[0]
        title_y = (screen.get_height() - title.get_height()) // 2 + title_offset[1]
        screen.blit(title, (title_x, title_y))
        
        # render prompt
        prompt = prompt_font.render("Press SPACE to start", True, prompt_color)
        prompt_x = (screen.get_width() - prompt.get_width()) // 2 + prompt_offset[0]
        prompt_y = (screen.get_height() - prompt.get_height()) // 2 + prompt_offset[1]
        screen.blit(prompt, (prompt_x, prompt_y))
        
        # render credit
        credit = credit_font.render("Created by: possibly_nai", True, credit_color)
        credit_x = (screen.get_width() - credit.get_width()) // 2 + credit_offset[0]
        credit_y = (screen.get_height() - credit.get_height()) // 2 + credit_offset[1]
        screen.blit(credit, (credit_x, credit_y))
    else:
        screen.fill((0, 0, 0))  # placeholder for actual game screen

    pygame.display.flip()

pygame.quit()