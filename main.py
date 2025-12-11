import pygame
import random
from sprites import load_sunflower_animations, load_watering_can_animation, load_plant_food_animation

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Sunflower")

# assets
title_image = pygame.image.load("backgrounds/title-screen.png").convert()
title_image = pygame.transform.scale(title_image, screen.get_size())

# background images
backgrounds = [
    pygame.transform.scale(pygame.image.load("backgrounds/day.png").convert(), screen.get_size()),
    pygame.transform.scale(pygame.image.load("backgrounds/sunset.png").convert(), screen.get_size()),
    pygame.transform.scale(pygame.image.load("backgrounds/night.png").convert(), screen.get_size())
]
current_bg = 0  # index of current background

# button images
talk_button = pygame.image.load("images/talk-button.png").convert_alpha()
water_button = pygame.image.load("images/water-button.png").convert_alpha()
feed_button = pygame.image.load("images/feed-button.png").convert_alpha()

# button positions - spacing them apart horizontally
talk_button_rect = talk_button.get_rect(topleft=(100, 420))
water_button_rect = water_button.get_rect(topleft=(270, 420))
feed_button_rect = feed_button.get_rect(topleft=(440, 420))

# title text styling
title_font = pygame.font.SysFont("monospace", 56)
title_color = (255, 255, 255)
title_offset = (0, -5)

# prompt styling
prompt_font = pygame.font.SysFont("monospace", 28) 
prompt_color = (255, 220, 80)
prompt_offset = (0,80)

# credit styling
credit_font = pygame.font.SysFont("monospace", 20)
credit_color = (255, 220, 80)
credit_offset = (-150, 220)

# phrase system
phrases = [
    "Hello there!",
    "I'm happy to see you!",
    "How are you today?",
    "Thanks for visiting!",
    "This is nice..."
]
current_phrase = ""
show_phrase = False
phrase_timer = 0
phrase_duration = 3000  # show for 3 seconds
phrase_font = pygame.font.SysFont("monospace", 14)
phrase_color = (217, 137, 0)
# typing effect
typing_speed = 50 
current_char_index = 0
last_char_time = 0
full_phrase = ""

# load sunflower sprite animations
sunflower_animations = load_sunflower_animations()
watering_can_animation = load_watering_can_animation()
plant_food_animation = load_plant_food_animation()

# game state
game_start = False
text_color = (255, 255, 255)

# animation state
action = 2  # 0: talking, 1: excited, 2: idle
frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 220

# one-time animation tracking
playing_one_time = False
one_time_action = None
one_time_frame = 0
one_time_last_update = pygame.time.get_ticks()
one_time_loop_count = 0  # how many times animation has looped
one_time_loops_needed = 2  # how many times to loop before returning to idle

# watering can animation
show_watering_can = False
watering_can_frame = 0
watering_can_last_update = pygame.time.get_ticks()
watering_can_cooldown = 120 
watering_can_finished = False 

# plant food animation
show_plant_food = False
plant_food_frame = 0
plant_food_last_update = pygame.time.get_ticks()
plant_food_cooldown = 120

# background cycling
click_count = 0
clicks_per_bg = 8

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = False
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_start = True
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_clicked = True

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
        
        # render my credit
        credit = credit_font.render("Created by: possibly_nai", True, credit_color)
        credit_x = (screen.get_width() - credit.get_width()) // 2 + credit_offset[0]
        credit_y = (screen.get_height() - credit.get_height()) // 2 + credit_offset[1]
        screen.blit(credit, (credit_x, credit_y))
    else:
        # game screen - display current background
        screen.blit(backgrounds[current_bg], (0, 0))
        
        # handle one-time animations
        if playing_one_time:
            current_time = pygame.time.get_ticks()
            if current_time - one_time_last_update >= animation_cooldown:
                one_time_frame += 1
                if one_time_frame >= len(sunflower_animations[one_time_action]):
                    # animation finished one loop
                    one_time_loop_count += 1
                    if one_time_loop_count >= one_time_loops_needed:
                        # done looping, return to idle
                        playing_one_time = False
                        action = 2  # idle
                        frame = 0
                        one_time_loop_count = 0
                    else:
                        # loop again
                        one_time_frame = 0
                one_time_last_update = current_time
        else:
            # update idle animation
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                frame += 1
                if frame >= len(sunflower_animations[action]):
                    frame = 0
                last_update = current_time
        
        if show_watering_can:
            current_time = pygame.time.get_ticks()
            if current_time - watering_can_last_update >= watering_can_cooldown:
                watering_can_frame += 1
                if watering_can_frame >= len(watering_can_animation):
                    show_watering_can = False
                watering_can_last_update = current_time
                frame += 1
                if frame >= len(sunflower_animations[action]):
                    frame = 0
                last_update = current_time
        
        if show_plant_food:
            current_time = pygame.time.get_ticks()
            if current_time - plant_food_last_update >= plant_food_cooldown:
                plant_food_frame += 1
                if plant_food_frame >= len(plant_food_animation):
                    show_plant_food = False
                plant_food_last_update = current_time
                frame += 1
                if frame >= len(sunflower_animations[action]):
                    frame = 0
                last_update = current_time
        
        # display sunflower sprite
        if playing_one_time:
            screen.blit(sunflower_animations[one_time_action][one_time_frame], (250, 270))
        else:
            screen.blit(sunflower_animations[action][frame], (250, 270))
        
        # display watering can if active
        if show_watering_can:
            screen.blit(watering_can_animation[watering_can_frame], (270, 190))
        
        # display plant food if active
        if show_plant_food:
            screen.blit(plant_food_animation[plant_food_frame], (330, 260))
        
        # display phrase if active
        if show_phrase:
            # typing effect
            if current_char_index < len(full_phrase):
                current_time = pygame.time.get_ticks()
                if current_time - last_char_time >= typing_speed:
                    current_char_index += 1
                    current_phrase = full_phrase[:current_char_index]
                    last_char_time = current_time
            
            # check if phrase should disappear
            if pygame.time.get_ticks() - phrase_timer > phrase_duration:
                show_phrase = False
            else:
                # create text box background
                text_box_width = 250
                text_box_height = 80
                text_box_x = 370
                text_box_y = 250
                
                # draw rounded rectangle for text box
                text_box_rect = pygame.Rect(text_box_x, text_box_y, text_box_width, text_box_height)
                pygame.draw.rect(screen, (255, 193, 87), text_box_rect, border_radius=15)
                pygame.draw.rect(screen, (217, 137, 0), text_box_rect, 3, border_radius=15)
                
                # render and display phrase text (centered in box)
                phrase_text = phrase_font.render(current_phrase, True, phrase_color)
                text_x = text_box_x + (text_box_width - phrase_text.get_width()) // 2
                text_y = text_box_y + (text_box_height - phrase_text.get_height()) // 2
                screen.blit(phrase_text, (text_x, text_y))
        
        # display and handle talk button (action 0)
        screen.blit(talk_button, talk_button_rect)
        if talk_button_rect.collidepoint(mouse_pos) and mouse_clicked:
            playing_one_time = True
            one_time_action = 0  # talking animation
            one_time_frame = 0
            one_time_loop_count = 0
            one_time_loops_needed = 2  # talk animation loops twice
            one_time_last_update = pygame.time.get_ticks()
            full_phrase = random.choice(phrases)
            current_phrase = ""
            current_char_index = 0
            last_char_time = pygame.time.get_ticks()
            show_phrase = True
            phrase_timer = pygame.time.get_ticks()
            click_count += 1
            if click_count >= clicks_per_bg:
                current_bg = (current_bg + 1) % len(backgrounds)
                click_count = 0
        
        # display and handle water button (action 1)
        screen.blit(water_button, water_button_rect)
        if water_button_rect.collidepoint(mouse_pos) and mouse_clicked:
            playing_one_time = True
            one_time_action = 1  # excited animation
            one_time_frame = 0
            one_time_loop_count = 0
            one_time_loops_needed = 1  # water animation loops once
            one_time_last_update = pygame.time.get_ticks()
            show_watering_can = True
            watering_can_frame = 0
            click_count += 1
            if click_count >= clicks_per_bg:
                current_bg = (current_bg + 1) % len(backgrounds)
                click_count = 0
        
        # display and handle feed button (action 2)
        screen.blit(feed_button, feed_button_rect)
        if feed_button_rect.collidepoint(mouse_pos) and mouse_clicked:
            playing_one_time = True
            one_time_action = 1  # excited animation
            one_time_frame = 0
            one_time_loop_count = 0
            one_time_loops_needed = 1  # feed animation loops once
            one_time_last_update = pygame.time.get_ticks()
            show_plant_food = True
            plant_food_frame = 0
            click_count += 1
            if click_count >= clicks_per_bg:
                current_bg = (current_bg + 1) % len(backgrounds)
                click_count = 0
        
    pygame.display.flip()

pygame.quit()