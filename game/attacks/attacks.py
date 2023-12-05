from game.attacks._base_attack_functions import simple_attack_uniform, attack_multiplier_by_type


def mathematics(attacker, defender):
        """
        Puzzles the defender.

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
        #print("math")
        defender.change_status("puzzled")

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
        #print("school_talk")
        defender.change_status("sleeping")

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
        #print("tackle")
        # Example attack logic, can be expanded with more complex mechanics
        damage = simple_attack_uniform(attacker, defender,
                                       power_attack=50,
                                       bound_multiplicator=0.1)
        
        #use advantages of types
        damage_adjusted = attack_multiplier_by_type(attacker, defender) * damage
        
        defender.take_damage(damage_adjusted)