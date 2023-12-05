import random

from game.status_functions import status_recovery
from game.attacks._base_attack_functions import conduct_status_based_action 

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
    while not character1.is_defeated() and not character2.is_defeated():
        # Determine turn order based on speed
        speed = random.normalvariate(character1.speed - character2.speed,
                                      (character1.speed + character2.speed)**0.5)
        
        first, second = (character1, character2) if speed >= 0 else (character2, character1)
        
        # First character might heal status, chooses and executes an attack
        if first.can_attack:
            status_recovery(first)
            conduct_status_based_action(attacker=first, defender=second)
        else:
            first.change_attack_status(True)

        if second.is_defeated():
            return first.name

        # Second character might heal status, chooses and executes an attack
        if second.can_attack:
            status_recovery(second)
            conduct_status_based_action(attacker=second, defender=first)
        else:
            second.change_attack_status(True)

        if first.is_defeated():
            return second.name

    return "It's a tie!"