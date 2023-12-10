from typing import Optional

import numpy as np
import random
   

def simple_attack_uniform(attacker, defender, power_attack, bound_multiplicator=0.1):
    """
    Executes a simple attack with variable damage determined by a uniform distribution.

    The damage is calculated based on the attacker's attack power, the power of the attack,
    and the defender's defense. It is then adjusted randomly within a specified range.

    Parameters
    ----------
    attacker : Character
        The character executing the attack.
    defender : Character
        The character defending against the attack.
    power_attack : int
        The base power of the attack.
    bound_multiplicator : float, optional
        A multiplier to determine the range of variability in the damage (default is 0.1).

    Returns
    -------
    float
        The calculated damage value.
    """
    # Calculate the mean damage value
    damage_mean = attacker.attack + power_attack - defender.defense

    # Ensure the lower bound is not negative
    lower_bound = max(0, damage_mean * (1 - bound_multiplicator))

    # Calculate the upper bound
    upper_bound = damage_mean * (1 + bound_multiplicator)

    # Generate and return the damage value
    return np.random.uniform(lower_bound, upper_bound, 1)[0]


def conduct_attack(attacker, defender, attack: Optional[callable] = None):
    """
    Executes an attack from the attacker to the defender.

    This function allows the attacker to choose an attack and then execute it against the defender.

    Parameters
    ----------
    attacker : Character
        The character who is conducting the attack.
    defender : Character
        The character who is defending against the attack.
    attack : function, optional
        The attack to be executed (default is None). If None, the attacker will choose an attack.

    Returns
    -------
    None
    """
    if attack is None:
        attack = attacker.choose_attack(defender)
    if attack:
        attack(attacker, defender)


def conduct_status_based_action(attacker, defender, attack: Optional[callable] = None):
    """
    Performs an action based on the attacker's status.

    Depending on the status of the attacker (e.g., 'sleeping', 'puzzled'), this function determines
    what action the attacker takes. If 'sleeping', no action is taken. If 'puzzled', there's a chance
    the attacker will harm themselves or conduct a normal attack.

    Parameters
    ----------
    attacker : Character
        The character who might take an action based on their status.
    defender : Character
        The character who would defend against any attack, if one occurs.
    attack : function, optional
        The attack to be executed (default is None). If None, the attacker will choose an attack.

    Returns
    -------
    None

    """
    if attacker.status in ["sleeping", "sad", "occupied"]:
        print(f"{attacker.name} is {attacker.status}")
        pass  # No action is taken
    elif attacker.status == "puzzled":
        print(f"{attacker.name} is {attacker.status}")
        if random.uniform(0.0, 1.0) > 0.4:
            print(f"{attacker.name} damaged itself")
            attacker.take_damage(attacker.max_health * 0.2)
        else:
            print(f"{attacker.name} was able to attack")
            conduct_attack(attacker, defender, attack=attack)
    else:
        print(f"{attacker.name} attacked")
        conduct_attack(attacker, defender, attack=attack)


def attack_multiplier_by_type(attacker, defender):
    """
    Calculates an attack multiplier based on the types of the attacker and defender.

    The function uses a predefined set of types each associated with a numerical value. 
    The difference in these values between the attacker and defender is used to determine
    the attack multiplier, which represents the effectiveness of the attack based on type match-up.

    Parameters
    ----------
    attacker : Character
        The character who is conducting the attack. The character should have a 'type' attribute.
    defender : Character
        The character who is defending against the attack. The character should have a 'type' attribute.

    Returns
    -------
    float
        The calculated attack multiplier. A value greater than 1 indicates an effective attack, 
        less than 1 indicates a less effective attack, based on the types.

    """
    types = {"physical": 5, "popular": 4, "smart": 3, "strong": 2, "funny": 1}
    diff = types[attacker.type] - types[defender.type]
    if diff in [1, -4]:
        return 1.3
    elif diff in [-1, 4]:
        return 0.7
    else:
        return 1.0 

    
    
    
    
    
    
    