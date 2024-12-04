import random

from game.attacks.base_attack_functions import simple_attack_uniform, attack_multiplier_by_type


attack_messages = {
    'travel': 'used travel funds',
    'overleaf': 'multiple overleaf docs',
    'julia': 'used julia, got TypeError',
    'janitor': 'burned unicorn',
    'math': 'math was too complicated',
    'rebellion': 'group rebellion',
    'delay': 'delayed publication',
    'postdoc': 'postdoc power - failed',
    'mattermost': 'concerning everybody',
    'funds': 'restricted travel funds',
    'proposal': 'proposal help requested',
    'telling': 'new phd duration time',
    'cancel': 'cancelled meeting',
    'declare': 'declared as expert',
    'paperol': 'aperol spritz',
    'research': 'bad research',
    'research ': 'good research',
    'gpu': 'unicorn is fully blocked',
    'tom': 'is busy, tom called',
    'absence': 'is absent',
}


def bad_research(attacker, defender):
    """
        Basic attack, rather weak.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} did bad research")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=20,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage
    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")


def cancels_meeting(attacker, defender):
    """
        Cancels meeting and might make student sad.

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
        Really strong attack. Delay of publication.

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


def gpu_attack(attacker, defender):
    """
        Blocks the GPU on the unicorn. Weak attack since resources on Marvin are still free.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} blocked the gpu on unicorn. But resources on Marvin are still free...")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=20,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage
    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")


def good_research(attacker, defender):
    """
        Attack the defender based on good research.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} did amazing research")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=60,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage
    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")


def jan_absence(attacker, defender):
    """
        Janitor is absent, heals himself and makes opponent puzzled.

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
    print(f"{attacker.name} is absent.")
    attacker.heal(attacker.max_health * 0.1)
    print(f"{attacker.name} healed 10% of his health")

    defender.change_status("puzzled")
    print(f"{defender.name} became {defender.status}")


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
    print(f"{attacker.name} burned unicorn")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=50,
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
                                   power_attack=20,
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
                                   power_attack=80,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage

    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")
    attacker.change_attack_status(False)
    print(f"{attacker.name} became exhausted")


def paperol(attacker, defender):
    """
        Makes the defender puzzled due to alcohol.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} got drunk. {defender.name} has to pay!")
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=20,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage
    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")

    defender.change_status("puzzled")
    print(f"{defender.name} became {defender.status}")


def proposal_help(attacker, defender):
    """
        Makes the defender occupied. Weak attack.

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
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=20,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage

    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")
    defender.change_status("occupied")
    print(f"{defender.name} became {defender.status}")


def postdoc_power(attacker, defender):
    """
        Increases the attacker's base damage in the next round.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} used the postdoc power.")
    if random.uniform(0.0, 1.0) > 0.25:
        #attacker.attack = attacker.attack * 1.5
        print(f"{attacker.name} would have increased damage by 50% if thesis would have been finished.")


def restricted_travel_funds(attacker, defender):
    """
        Makes others really sad. Weak attack.

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
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=10,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage

    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")
    defender.change_status("sad")
    print(f"{defender.name} became {defender.status}")


def telling_different_phd_duration_times(attacker, defender):
    """
        Makes the defender puzzled. Weak attack.

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
    damage = simple_attack_uniform(attacker, defender,
                                   power_attack=10,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage

    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")
    defender.change_status("puzzled")
    print(f"{defender.name} became {defender.status}")


def travel_money_use(attacker, defender):
    """
        Attacker uses travel money. Strong attack.

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
                                   power_attack=60,
                                   bound_multiplicator=0.2)

    # use advantages of types
    damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage

    defender.take_damage(damage_adjusted)
    print(f"{defender.name} took {damage_adjusted} damage")


def tom_calls(attacker, defender):
    """
        Makes the attacker busy and unable to attack in this round.

        Parameters
        ----------
        attacker : Character
            The character executing the attack.
        defender : Character
            The character defending against the attack.
    """
    print(f"{attacker.name} got a call by Tom and is occupied now.")
    pass
