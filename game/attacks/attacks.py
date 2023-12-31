import random

from game.attacks.base_attack_functions import simple_attack_uniform, attack_multiplier_by_type


attack_messages = {
    'travel': 'used travel funds',
    'overleaf': 'multiple overleaf docs',
    'julia': 'used julia, got TypeError',
    'janitor': 'janitor burned unicorn',
    'unsupervised': 'unsupervised learning',
    'math': 'math was too complicated',
    'rebellion': 'group rebellion',
    'delay': 'delayed publication',
    'postdoc': 'postdoc added',
    'shield': 'peer reviewed shield',
    'mattermost': 'concerning everybody',
    'funds': 'restricted travel funds',
    'proposal': 'proposal help requested',
    'telling': 'new phd duration time',
    'cancel': 'cancelled meeting',
    'declare': 'declared as expert'
}


def cancels_meeting(attacker, defender):
    """
        Cancels meeting and  might make student sad.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.

        Returns
        -------
        None
        """
    print(f"{attacker.name} used canceling meeting")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=70,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage
    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")

    if random.uniform(0.0, 1.0) > 0.5:
        defender.change_status("sad")
        print(f"{defender.name} became {defender.status}")


def create_multiple_overleaf_documents(attacker, defender):
    """
        Makes the defender puzzled due to the multiple overleaf documents.
        Weak attack but will definitely puzzle the opponent.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} used multiple overleaf documents")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=20,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage
    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")

    defender.change_status("puzzled")
    print(f"{defender.name} became {defender.status}")


def declares_as_expert(attacker, defender):
    """
        Declares the opponent as an expert what might puzzle the opponent.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.

        Returns
        -------
        None
        """
    print(f"{attacker.name} used declaring as expert")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=70,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage
    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")

    if random.uniform(0.0, 1.0) > 0.5:
        defender.change_status("puzzled")
        print(f"{defender.name} became {defender.status}")


def delay_of_publication(attacker, defender):
    """
        Really strong attack.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.

        Returns
        -------
        None
        """
    print(f"{attacker.name} used delay of publication")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=100,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage

    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")


def group_presentation(attacker, defender):
    """
        Makes the defender sleeping, but no damage.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.

        Returns
        -------
        None
        """
    print(f"{attacker.name} used group presentation")
    defender.change_status("sleeping")
    print(f"{defender.name} became {defender.status}")


def group_rebellion(attacker, defender):
    """
        Makes the defender puzzled due to the group rebellion of the attacker.
        Make the attacker sleeping.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} used group rebellion")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=100,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage

    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")

    # weakens the attackers
    attacker.change_status("sleeping")
    print(f"{defender.name} became {defender.status}")


def hausmeister_power(attacker, defender):
    """
        Makes the defender sad due to the power of the Hausmeister. Weak attack.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} used hausmeister")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=20,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage

    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")

    defender.change_status("sad")
    print(f"{defender.name} became {defender.status}")


def julia_attacks(attacker, defender):
    """
        Makes the attacker puzzled due to unspecified type issues, attack bounces back to the attacker.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} used julia")
    attacker.change_status("puzzled")

    damage = simple_attack_uniform(defender, attacker,
                                   power_attack=50,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(defender, attacker) * damage
    if random.uniform(0.0, 1.0) > 0.5:
        attacker.take_damage(damage_adjusted)
        print(f"{attacker.name} took {damage_adjusted} damage")


def mathematics(attacker, defender):
    """
        Can puzzle defender and attacker due to complicated mathematics.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.

        Returns
        -------
        None
        """
    # print("math")
    print(f"{attacker.name} used mathematics")
    if random.uniform(0.0, 1.0) > 0.5:
        defender.change_status("puzzled")
        print(f"{defender.name} became {defender.status}")

        damage = simple_attack_uniform(attacker, defender,
                                       power_attack=70,
                                       bound_multiplicator=0.2)

        # use advantages of types
        damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage
        if random.uniform(0.0, 1.0) > 0.5:
            defender.take_damage(damage_adjusted)
            print(f"{defender.name} took {damage_adjusted} damage")

    if random.uniform(0.0, 1.0) > 0.5:
        attacker.change_status("puzzled")
        print(f"{attacker.name} became {attacker.status}")

        damage = simple_attack_uniform(defender, attacker,
                                       power_attack=70,
                                       bound_multiplicator=0.2)

        # use advantages of types
        damage_adjusted = attack_multiplier_by_type(defender, attacker) * damage
        if random.uniform(0.0, 1.0) > 0.5:
            attacker.take_damage(damage_adjusted)
            print(f"{attacker.name} took {damage_adjusted} damage")


def mattermost_message_concerning_everybody(attacker, defender):
    """
        Very strong attack due to public shaming.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.

        Returns
        -------
        None
        """
    print(f"{attacker.name} used Mattermost message concerning everybody")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=170,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage

    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")
    attacker.change_attack_status(False)
    print(f"{attacker.name} became exhausted")


def proposal_help(attacker, defender):
    """
        Makes the defender sleeping.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.

        Returns
        -------
        None
        """
    print(f"{attacker.name} used proposal help")
    defender.change_status("occupied")
    print(f"{defender.name} became {defender.status}")


def peer_reviewed_shield(attacker, defender):
    """
        Makes the defender sleeping due to the peer reviewed paper of the attacker.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} used peer reviewed paper")
    defender.change_status("sleeping")
    print(f"{defender.name} became {defender.status}")


def postdoc_power(attacker, defender):
    """
        Increases base damage of the attacker in the next round.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
        """
    print(f"{attacker.name} used her postdoc power")
    if random.uniform(0.0, 1.0) > 0.25:
        attacker.attack = attacker.attack * 1.5
        print(f"{attacker.name} increased her damage by 50%")


def restricted_travel_funds(attacker, defender):
    """
        Makes others really sad

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.

        Returns
        -------
        None
        """
    print(f"{attacker.name} used restricted travel funds")
    defender.change_status("sad")
    print(f"{defender.name} became {defender.status}")


def school_talk(attacker, defender):
    """
        Makes the defender sleeping.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.

        Returns
        -------
        None
        """
    print(f"{attacker.name} used talk about school")
    # print("school_talk")
    defender.change_status("sleeping")
    print(f"{defender.name} became {defender.status}")


def tackle(attacker, defender):
    """
        Executes the attack from the attacker to the defender.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.

        Returns
        -------
        None
        """
    print(f"{attacker.name} used tackle")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=50,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage

    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")


def telling_different_phd_duration_times(attacker, defender):
    """
        Makes the defender puzzled.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.

        Returns
        -------
        None
        """
    print(f"{attacker.name} used telling different PhD duration times")
    defender.change_status("puzzled")
    print(f"{defender.name} became {defender.status}")


def travel_money_use(attacker, defender):
    """
        Executes the attack from the attacker to the defender.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.

        Returns
        -------
        None
        """
    print(f"{attacker.name} used travel money")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=70,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage

    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")


def unsupervised_learning(attacker, defender):
    """
        Makes the defender puzzled due to the unsupervised learning outcome of the attacker.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} used unsupervised learning")
    defender.change_status("puzzled")
    print(f"{defender.name} became {defender.status}")


def wrong_results(attacker, defender):
    """
        Makes the defender puzzled due to the wrong results of the attacker.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} used wrong results")
    defender.change_status("puzzled")
    print(f"{defender.name} became {defender.status}")
