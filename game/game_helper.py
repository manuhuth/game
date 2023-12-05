import pygame


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
    screen.blit(p2, (10, 175))
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
