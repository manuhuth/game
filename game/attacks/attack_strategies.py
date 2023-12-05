import random


def choose_attack_randomly(attacks):
    """
    Chooses an attack randomly from a list of available attacks.

    Parameters
    ----------
    attacks : list
        A list of attack functions from which to randomly select.

    Returns
    -------
    function
        A randomly chosen attack function from the list. If the list is empty, returns None.

    Notes
    -----
    This function does not execute the attack; it only selects an attack function.
    """
    if attacks:
        return random.choice(attacks)
    else:
        return None
