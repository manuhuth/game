import pygame
import random


def get_current_attack(text_positions, x, y) -> int:
    if x == text_positions["attack1"][0] - 25 and y == text_positions["attack1"][1]:
        return 0
    elif x == text_positions["attack2"][0] - 25 and y == text_positions["attack2"][1]:
        return 1
    elif x == text_positions["attack3"][0] - 25 and y == text_positions["attack3"][1]:
        return 2
    elif x == text_positions["attack4"][0] - 25 and y == text_positions["attack4"][1]:
        return 3


def set_standard_image(screen, back, p1, p2):
    screen.blit(back, (0, 0))
    screen.blit(p1, (375, 50))
    screen.blit(p2, (100, 175))
    return


def draw_health_bar(life, pv_start, screen, x, y):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 122, 8))
    if life > pv_start / 2:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, life / pv_start * 122, 8))
    elif life <= pv_start / 4:
        pygame.draw.rect(screen, (255, 0, 0), (x, y, life / pv_start * 122, 8))
    elif life <= pv_start / 2:
        pygame.draw.rect(screen, (255, 165, 0), (x, y, life / pv_start * 122, 8))
    return


def switch_player(attacker, character1, character2, switched_player, current_round):
    # switch player
    print('switching player')
    if not switched_player:
        # switch players to complete the round
        if attacker.name == character1.name:
            attacker = character2
            defender = character1
            switched_player = True
        else:
            attacker = character1
            defender = character2
            switched_player = True
    else:
        # player already switched, so round is over
        print("-------------------------------------------------------------------------------------------------------")
        switched_player = False
        current_round += 1

        # Determine turn order for the next round based on speed
        speed = random.normalvariate(character1.speed - character2.speed,
                                     (character1.speed + character2.speed) ** 0.5)

        attacker, defender = (character1, character2) if speed >= 0 else (character2, character1)
        print(f"Round {current_round + 1} - {attacker.name} is attacking first")
    return attacker, defender, switched_player, current_round


def load_image(path, width=150, height=150):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image


def wait(sec: int = 5):
    pygame.display.flip()
    # pygame.event.pump()
    pygame.time.delay(sec * 1000)
    return
