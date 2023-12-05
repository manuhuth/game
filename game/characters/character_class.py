from game.attacks.attack_strategies import choose_attack_randomly

class Character:
    """
    A class to represent a character in the game.

    Attributes
    ----------
    name : str
        The name of the character.
    max_health : int
        The maximum health points of the character.
    health : int
        The current health points of the character.
    attack : int
        The attack strength of the character.
    defense : int
        The defense strength of the character.
    speed : int
        The speed of the character.

    Methods
    -------
    take_damage(damage)
        Reduces the character's health by the given damage amount.
    heal(healing_points)
        Heals the character by a given number of points without exceeding max health.
    is_defeated()
        Checks if the character's health has dropped to zero or below.
    """

    def __init__(self, name, char_type, max_health, attack, defense, speed, attacks,
                 attack_strategy):
            """
            Constructs all the necessary attributes for the character object.
    
            Parameters
            ----------
                name : str
                    The name of the character.
                max_health : int
                    The maximum health points of the character.
                attack : int
                    The attack strength of the character.
                defense : int
                    The defense strength of the character.
                speed : int
                    The speed of the character.
                attacks : list
                    A list of attack functions that the character can perform.
                attack_strategy : str
                    A strategy choosing the attack
            """
            if not(char_type in ["physical", "smart", "strong", "popular", "funny"]):
                raise ValueError('The type of a charcter must either be physical, smart, strong, popular, or funny.')
            self.name = name
            self.type = char_type
            self.max_health = max_health
            self.health = max_health
            self.attack = attack
            self.defense = defense
            self.speed = speed
            self.attacks = attacks
            self.attack_strategy = attack_strategy
            self.status = None
            self.can_attack = True

    def take_damage(self, damage):
        """
        Reduces the character's health by the given damage amount.

        Parameters
        ----------
        damage : int
            The amount of damage to inflict on the character.
        """
        self.health = max(self.health - damage, 0)

    def heal(self, healing_points):
        """
        Heals the character by a given number of points without exceeding max health.

        Parameters
        ----------
        healing_points : int
            The number of health points to restore.
        """
        self.health = min(self.health + healing_points, self.max_health)

    def is_defeated(self):
        """
        Checks if the character's health has dropped to zero or below.

        Returns
        -------
        bool
            True if the character is defeated, False otherwise.
        """
        return self.health <= 0
    
    def choose_attack(self, defender):
        """
        Chooses an attack based on the character's strategy.

        This implementation chooses an attack randomly from the available attacks.

        Returns
        -------
        function
            A function representing the chosen attack.
        """
        if self.attack_strategy == "random":
            return choose_attack_randomly(self.attacks)
    
    def change_status(self, new_status):
        """
        Updates the status of the character.

        This method allows for changing the current status of the character to a new status.
        Meaningful statuses are "bored", "interested", "puzzled". 

        Parameters
        ----------
        new_status : str
            The new status to be assigned to the character.

        Returns
        -------
        None
        """
        self.status = new_status
    
    def change_attack_status(self, new_status):
        """
        Updates the attack status of the character.

        This method allows for changing the current status of the character to a new status. 

        Parameters
        ----------
        new_status : bool
            The new status to be assigned to the character.

        Returns
        -------
        None
        """
        self.can_attack = new_status

