import random

def status_recovery(character, probability=0.5):
    """
    Attempts to recover a character from their current status based on a probability.

    The function checks if the character has a status. If so, it then determines randomly, 
    based on the specified probability, whether the character recovers from that status.

    Parameters
    ----------
    character : Character
        The character for whom status recovery is being attempted.
    probability : float, optional
        The probability of recovering from the status (default is 0.3).

    Returns
    -------
    None

    """
    if character.status is not None:
        if random.uniform(0.0, 1.0) > 1 - probability:
            character.change_status(None)

def status_influence(character):
    """
    Applies the effects of a character's current status.

    Depending on the status of the character (e.g., 'sleeping', 'puzzled'), this function 
    determines the effects on the character. For example, if the status is 'puzzled', 
    the character takes a small amount of damage.

    Parameters
    ----------
    character : Character
        The character affected by their current status.

    Returns
    -------
    None

    """
    if character.status == "sleeping":
        pass  # No action taken for sleeping status
    elif character.status == "puzzled":
        if random.uniform(0.0, 1.0) > 0.5:
            character.take_damage(character.max_health * 0.1)
