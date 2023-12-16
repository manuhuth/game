import os
import random
import numpy as np
import pygame

from game.characters.character_class import Character
from game.status_functions import status_recovery
from game.attacks._base_attack_functions import conduct_status_based_action
from game.game_helper import get_current_attack, set_standard_image, draw_health_bar, switch_player, load_image
from game.attacks.attacks import mattermost_message_concerning_everybody, \
    restricted_travel_funds, group_presentation, proposal_help, \
    telling_different_phd_duration_times, delay_of_publication, \
    cancels_meeting, declares_as_expert, travel_money_use

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

defeated_image = pygame.image.load(os.path.join('Resources/Background', 'back3.png'))
defeated_image = pygame.transform.scale(defeated_image, (screen_width, screen_height))

# load other UI elements
UI_cursor = pygame.image.load(os.path.join('Resources/UI', 'cursor.png')).convert_alpha()
UI_cursor = pygame.transform.scale(UI_cursor, (40, 40))

UI_dialogbox = pygame.image.load(os.path.join('Resources/UI', 'dialogbox.png')).convert_alpha()
UI_dialogbox = pygame.transform.scale(UI_dialogbox, (screen_width * 0.53, screen_height / 3))

UI_hp_boxes = pygame.image.load(os.path.join('Resources/UI', 'ui_boxes.png')).convert_alpha()
UI_hp_boxes = pygame.transform.scale(UI_hp_boxes, (screen_width, screen_height))

UI_health = pygame.image.load(os.path.join('Resources/UI', 'ui_health.png')).convert_alpha()
UI_health = pygame.transform.scale(UI_health, (screen_width, screen_height))

font = pygame.font.Font(os.path.join('Resources/Fonts', 'slkscr.ttf'), 30)
font2 = pygame.font.Font(os.path.join('Resources/Fonts', 'slkscr.ttf'), 19)

sleeping_status = pygame.image.load(os.path.join('Resources/Status', 'sleeping.png')).convert_alpha()
sleeping_status = pygame.transform.scale(sleeping_status, (65, 45))

occupied_status = pygame.image.load(os.path.join('Resources/Status', 'occupied.png')).convert_alpha()
occupied_status = pygame.transform.scale(occupied_status, (65, 45))

puzzled_status = pygame.image.load(os.path.join('Resources/Status', 'puzzled.png')).convert_alpha()
puzzled_status = pygame.transform.scale(puzzled_status, (65, 45))

sad_status = pygame.image.load(os.path.join('Resources/Status', 'sad.png')).convert_alpha()
sad_status = pygame.transform.scale(sad_status, (65, 45))

status = {
    "sleeping": sleeping_status,
    "occupied": occupied_status,
    "puzzled": puzzled_status,
    "sad": sad_status
}

# load sounds
clingselection = pygame.mixer.Sound(os.path.join('Resources/sons', 'Selection_Click_Beep.wav'))
damagesound = pygame.mixer.Sound(os.path.join('Resources/sons', 'Hit_Damage.wav'))
boostsound = pygame.mixer.Sound(os.path.join('Resources/sons', 'Boost_sound.wav'))

text_positions = {
    "attack1": (85, 300),
    "attack2": (250, 300),
    "attack3": (85, 350),
    "attack4": (250, 350)
}

# Cursor setup
cursor_points = [(0, 0), (15, 5), (0, 10)]  # Triangle points
cursor_rect = pygame.Rect(text_positions["attack1"][0] - 25, text_positions["attack1"][1], 15, 10)


def single_battle(character1, character2):
    """
    Simulates a battle between two characters.

    At the start of each round, a random variable is drawn from a normal distribution for each character,
    with the mean and variance equal to the character's speed. The character with the higher value attacks first.

    Parameters
    ----------
    character1 : Character
        The first character in the battle.
    character2 : Character
        The second character in the battle.

    Returns
    -------
    str
        The name of the winning character.
    """
    make_dialog = False
    perform_attack = False
    current_round = 0
    switched_player = False
    show_attacker_name = True

    # Determine turn order based on speed  # todo: display something
    speed = random.normalvariate(character1.speed - character2.speed,
                                 (character1.speed + character2.speed) ** 0.5)

    attacker, defender = (character1, character2) if speed >= 0 else (character2, character1)
    possible_attacks = list(attacker.attacks.keys())
    possible_attacks = np.random.choice(possible_attacks, min(len(possible_attacks), 4), replace=False)

    set_standard_image(screen, background_image,
                       load_image(character1.image_path),
                       load_image(character2.image_path))

    while not character1.is_defeated() and not character2.is_defeated():
        for event in pygame.event.get():
            # check actions
            if event.type == pygame.QUIT:
                print("Game quit")
                pygame.quit()  # Use pygame.quit() to close the Pygame window properly
                quit()  # Use quit() to stop the script

            elif event.type == pygame.KEYDOWN:
                # If we are showing the attacker's name and SPACE is pressed, we want to move to attack selection
                if show_attacker_name and event.key == pygame.K_SPACE:
                    show_attacker_name = False
                    make_dialog = True
                    clingselection.play()

                # Handle cursor movement and attack selection only if make_dialog is True
                elif make_dialog:
                    if event.key == pygame.K_LEFT:
                        cursor_rect.x = text_positions["attack1"][0] - 25
                        clingselection.play()
                    elif event.key == pygame.K_RIGHT:
                        cursor_rect.x = text_positions["attack2"][0] - 25
                        clingselection.play()
                    elif event.key == pygame.K_UP:
                        cursor_rect.y = text_positions["attack1"][1]
                        clingselection.play()
                    elif event.key == pygame.K_DOWN:
                        cursor_rect.y = text_positions["attack3"][1]
                        clingselection.play()
                    elif event.key == pygame.K_SPACE:
                        # close dialog, and use attack
                        perform_attack = True
                        clingselection.play()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse button events if necessary
                pass

        # draw health bars
        screen.blit(UI_hp_boxes, (0, 50))
        draw_health_bar(character1.health, pv_start=character1.max_health,
                        screen=screen, x=130, y=140)
        draw_health_bar(character2.health, pv_start=character2.max_health,
                        screen=screen, x=513, y=321)
        screen.blit(font.render(character1.name, True, (0, 0, 0)), (10, 100))
        screen.blit(font.render(character2.name, True, (0, 0, 0)), (390, 290))

        # show status
        if character1.status is not None:
            screen.blit(status[character1.status], (575, 15))
        if character2.status is not None:
            screen.blit(status[character2.status], (150, 150))

        if show_attacker_name:
            # Display attacker's name only
            screen.blit(UI_dialogbox, (screen_width * 0.05, screen_height * 0.6))
            attacker_name_text = font2.render(f"{attacker.name}'s Turn", True, (0, 0, 0))
            screen.blit(attacker_name_text, text_positions["attack1"])

        elif make_dialog:
            if attacker.can_attack:
                # Display attacks only after attacker's name has been shown and space bar pressed
                screen.blit(UI_dialogbox, (screen_width * 0.05, screen_height * 0.6))
                pygame.draw.polygon(screen, (0, 0, 0),
                                    [(x + cursor_rect.x, y + cursor_rect.y) for x, y in cursor_points])
                for text, pos in zip(possible_attacks, text_positions.values()):
                    screen.blit(font2.render(text, True, (0, 0, 0)), pos)

            else:
                print('current attacker cannot attack')
                # include it here
                dummy_text = font2.render("dummy", True, (0, 0, 0))
                screen.blit(dummy_text, text_positions["attack1"])

                attacker.change_attack_status(True)  # TODO: maybe display something

                # switch player
                attacker, defender, switched_player, current_round = switch_player(attacker=attacker,
                                                                                   character1=character1,
                                                                                   character2=character2,
                                                                                   switched_player=switched_player,
                                                                                   current_round=current_round)
                possible_attacks = list(attacker.attacks.keys())
                possible_attacks = np.random.choice(possible_attacks, min(len(possible_attacks), 4), replace=False)
                make_dialog = False
                print(possible_attacks)
                # attacker might have a status, so check if they recover
                status_recovery(attacker)  # TODO: maybe display something

        if perform_attack:
            print('performing attack')
            # get current attack
            attack_nr = get_current_attack(text_positions, cursor_rect.x, cursor_rect.y)
            attack_nr = attack_nr if attack_nr < len(possible_attacks) else 0
            print('attacking with attack nr: ', attack_nr + 1)
            print("here")

            conduct_status_based_action(attacker=attacker, defender=defender,
                                        attack=attacker.attacks[possible_attacks[attack_nr]])
            damagesound.play()

            if defender.is_defeated():
                print(f"{defender.name} is defeated")
                return attacker.name

            # switch player (round might be over or not)
            attacker, defender, switched_player, current_round = switch_player(attacker=attacker,
                                                                               character1=character1,
                                                                               character2=character2,
                                                                               switched_player=switched_player,
                                                                               current_round=current_round)
            possible_attacks = list(attacker.attacks.keys())
            possible_attacks = np.random.choice(possible_attacks, min(len(possible_attacks), 4), replace=False)
            print(possible_attacks)
            # attacker might have a status, so check if they recover
            if not (attacker.status is None):
                stat = attacker.status
                status_recovery(attacker)  # TODO: maybe display something
                if stat == attacker.status:
                    print(f"{attacker.name} is still {stat}")
                else:
                    print(f"{attacker.name} is not longer {stat}")

            perform_attack = False
            make_dialog = False
            show_attacker_name = True

            # refresh the screen
            set_standard_image(screen, background_image,
                               load_image(character1.image_path),
                               load_image(character2.image_path))

        # refresh the screen
        pygame.display.flip()
        clock.tick(60)
    return "It's a tie!"


def team_battle(characters1, characters2):
    defeated1 = np.repeat(False, len(characters1))
    defeated2 = np.repeat(False, len(characters2))

    character1 = characters1[0]
    character2 = characters2[0]

    index1 = 0
    index2 = 0
    while (not (all(defeated1)) and not (all(defeated2))):
        result = single_battle(character1, character2)
        if result == "Game quit":
            return "Game quit"

        set_standard_image(screen, defeated_image,
                           load_image(character1.image_path),
                           load_image(character2.image_path))
        screen.blit(font.render(f"{result} wins!", True, (0, 0, 0)),
                    (100, 100))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(5 * 1000)

        if character1.is_defeated():
            defeated1[index1] = True
            index1 += 1
            character1 = characters1[np.min([index1, len(characters1) - 1])]

        if character2.is_defeated():
            defeated2[index2] = True
            index2 += 1
            character2 = characters2[np.min([index2, len(characters2) - 1])]

        if all(defeated1) and all(defeated2):
            return "Draw"

        if all(defeated1):
            return "Team 2"

        if all(defeated2):
            return "Team 1"


ps1 = Character(name="Player 1", char_type="smart",
                max_health=100,
                attack=25, defense=10,
                speed=10, attacks={'travel\nmoney': travel_money_use,
                                   'group': group_presentation},
                image_path=os.path.join('Resources/Philomons', 'torKant.png')
                )

ps2 = Character(name="Player 2", char_type="smart",
                max_health=100,
                attack=25, defense=10,
                speed=10, attacks={'delay': delay_of_publication,
                                   'group': group_presentation},
                image_path=os.path.join('Resources/Philomons', 'Leviator.png')
                )

sv = Character(name="JanoMon", char_type="smart",
               max_health=400,
               attack=25, defense=10,
               speed=10, attacks={'mattermost': mattermost_message_concerning_everybody,
                                  'travel': restricted_travel_funds,
                                  'proposal': proposal_help,
                                  'telling': telling_different_phd_duration_times,
                                  'cancels': cancels_meeting,
                                  'declares': declares_as_expert
                                  },
               image_path=os.path.join('Resources/Philomons', 'astronaut.png')
               )

characters = [ps1, ps2]
winner = []
game_active = True

set_standard_image(screen, background_image, load_image(sv.image_path),
                   load_image(characters[0].image_path))
while game_active:
    for _ in range(1):
        winner.append(team_battle([ps1, ps2], [sv]))
        ps1.heal(ps2.max_health)
        ps2.heal(ps2.max_health)
        sv.heal(sv.max_health)

    winner.count("Team 1")
    break

# todo: display winner
print(winner)

# quit pygame
pygame.quit()
