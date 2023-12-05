import os
os.chdir("/home/manuel/Documents/game")

#import character class
from game.characters.character_class import Character 

#import attacks
from game.attacks.attacks import tackle, mathematics, school_talk

#import battle function
from game.battle import battle

character1 = Character(name="Jonas", char_type="smart",
                       max_health=100,
                       attack=25, defense=10,
                       speed=10, attacks=[tackle, mathematics],
                       attack_strategy="random")

character2 = Character(name="Manu", char_type="funny",
                       max_health=100,
                       attack=25, defense=10,
                       speed=10, attacks=[tackle, mathematics],
                       attack_strategy="random")

winner = []
for _ in range(1000):
    winner.append(battle(character1, character2))
    character1.heal(character1.max_health)
    character2.heal(character2.max_health)
winner.count("Jonas") 
winner.count("Manu") 

# include types of attacks
# write graphics for the battles
