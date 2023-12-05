import os
import pygame

from game.game_helper import get_current_attack, set_standard_image, draw_health_bar

pygame.init()

# create the screen
screen_width = 650
screen_height = 450
pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Phdmon")
screen = pygame.display.set_mode((screen_width, screen_height))

# create a clock for refreshing the screen
clock = pygame.time.Clock()

# Load the background image
background_image = pygame.image.load(os.path.join('Resources/Background', 'back1.png'))
# Scale the image to fit the screen
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# load other UI elements
UI_cursor = pygame.image.load(os.path.join('Resources/UI', 'cursor.png')).convert_alpha()
UI_cursor = pygame.transform.scale(UI_cursor, (40, 40))

UI_dialogbox = pygame.image.load(os.path.join('Resources/UI', 'dialogbox.png')).convert_alpha()
UI_dialogbox = pygame.transform.scale(UI_dialogbox, (screen_width * 0.9, screen_height / 3))

UI_hp_boxes = pygame.image.load(os.path.join('Resources/UI', 'ui_boxes.png')).convert_alpha()
UI_hp_boxes = pygame.transform.scale(UI_hp_boxes, (screen_width, screen_height))

UI_health = pygame.image.load(os.path.join('Resources/UI', 'ui_health.png')).convert_alpha()
UI_health = pygame.transform.scale(UI_health, (screen_width, screen_height))

font = pygame.font.Font(os.path.join('Resources/Fonts', 'slkscr.ttf'), 30)
font2 = pygame.font.Font(os.path.join('Resources/Fonts', 'slkscr.ttf'), 19)

pokeImage = pygame.image.load(os.path.join('Resources/Philomons', 'astronaut.png')).convert_alpha()
pokeImage = pygame.transform.scale(pokeImage, (250, 250))

pokeImage2 = pygame.image.load(os.path.join('Resources/Philomons', 'torKant.png')).convert_alpha()
pokeImage2 = pygame.transform.scale(pokeImage2, (250, 250))


# load sounds
clingselection = pygame.mixer.Sound(os.path.join('Resources/sons', 'Selection_Click_Beep.wav'))
damagesound = pygame.mixer.Sound(os.path.join('Resources/sons', 'Hit_Damage.wav'))
boostsound = pygame.mixer.Sound(os.path.join('Resources/sons', 'Boost_sound.wav'))


text_positions = {
    "attack1": (100, 300),
    "attack2": (350, 300),
    "attack3": (100, 350),
    "attack4": (350, 350)
}

# Cursor setup
cursor_points = [(0, 0), (15, 5), (0, 10)]  # Triangle points
cursor_rect = pygame.Rect(text_positions["attack1"][0] - 25, text_positions["attack1"][1], 15, 10)


# TODO: current helpers
start_health_player_1 = 200  # TODO: get start health from player 1
start_health_player_2 = 100  # TODO: get start health from player 2
current_health_player_1 = start_health_player_1
current_health_player_2 = start_health_player_2
p1_name = 'JanOmon'
p2_name = 'PeiterTor'

game_active = True
show_hp = False
make_dialog = False
perform_attack = False
current_player = 0
set_standard_image(screen, background_image, pokeImage, pokeImage2)

while game_active:
    for event in pygame.event.get():

        # check actions
        if event.type == pygame.QUIT:
            game_active = False
            print("Game quit")

        elif make_dialog:
            if event.type == pygame.KEYDOWN:
                # Handle cursor movement
                if event.key == pygame.K_LEFT:
                    cursor_rect.x = text_positions["attack1"][0] - 25
                    clingselection.play()
                if event.key == pygame.K_RIGHT:
                    cursor_rect.x = text_positions["attack2"][0] - 25
                    clingselection.play()
                if event.key == pygame.K_UP:
                    cursor_rect.y = text_positions["attack1"][1]
                    clingselection.play()
                if event.key == pygame.K_DOWN:
                    cursor_rect.y = text_positions["attack3"][1]
                    clingselection.play()
                elif event.key == pygame.K_SPACE:
                    # close dialog, and use attack
                    make_dialog = False
                    perform_attack = True
                    clingselection.play()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_SPACE:
                # TODO: when should we show the dialog?
                make_dialog = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse action")

    # draw health bars
    if show_hp:
        screen.blit(UI_hp_boxes, (0, 50))
        draw_health_bar(current_health_player_1, pv_start=start_health_player_1,
                        screen=screen, x=130, y=140)
        draw_health_bar(current_health_player_2, pv_start=start_health_player_2,
                        screen=screen, x=513, y=321)
        screen.blit(font.render(p1_name, True, (0, 0, 0)), (10, 100))
        screen.blit(font.render(p2_name, True, (0, 0, 0)), (390, 290))

    if make_dialog:
        # make dialog box
        screen.blit(UI_dialogbox, (screen_width * 0.05, screen_height * 0.6))
        pygame.draw.polygon(screen, (0, 0, 0),
                            [(x + cursor_rect.x, y + cursor_rect.y) for x, y in cursor_points])
        for text, pos in text_positions.items():
            screen.blit(font2.render(text, True, (0, 0, 0)), pos)

    if perform_attack:
        # get current attack
        attack_nr = get_current_attack(text_positions, cursor_rect.x, cursor_rect.y)
        # TODO: perform attack
        if current_player == 0:
            current_health_player_2 -= 10
        else:
            current_health_player_1 -= 10
        damagesound.play()
        print('attacking with attack nr: ', attack_nr)
        perform_attack = False
        make_dialog = False
        show_hp = True

        # switch player
        if current_player == 0:
            current_player = 1
        else:
            current_player = 0

        # refresh the screen
        set_standard_image(screen, background_image, pokeImage, pokeImage2)

    # refresh the screen
    pygame.display.flip()
    clock.tick(60)

# quit pygame
pygame.quit()
