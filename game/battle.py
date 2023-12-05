import random
import numpy as np

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

def initialize_defeated_arrays(characters):
    return np.repeat(False, len(characters))

def team_battle(characters1, characters2):
    defeated1 = initialize_defeated_arrays(characters1)
    defeated2 = initialize_defeated_arrays(characters2)
    
    character1 = characters1[0]
    character2 = characters2[0]
    
    index1 = 0
    index2 = 0
    while (not(all(defeated1)) and not(all(defeated2))):
        print(character1.name)
        single_battle(character1, character2)
        if character1.is_defeated():
            defeated1[index1] = True
            index1 += 1
            character1 = characters1[np.min([index1, len(characters1)-1])]
            
        if character2.is_defeated():
            defeated2[index2] = True
            index2 += 1
            character2 = characters2[np.min([index2, len(characters2)-1])]
        
        if all(defeated1) and all(defeated2):
            return "Draw"
        
        if all(defeated1):
            return "Team 2"
        
        if all(defeated2):
            return "Team 1"

    
    
        
    
    
    
    
    