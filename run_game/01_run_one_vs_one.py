import os
os.chdir("/home/manuel/Documents/game")

#import character class
from game.characters.character_class import Character 

#import attacks
from game.attacks.attacks import tackle, mattermost_message_concerning_everybody, \
                                 restricted_travel_funds, group_presentation, proposal_help, \
                                 telling_different_phd_duration_times, delay_of_publication, \
                                 cancels_meeting, declares_as_expert

#import battle function
from game.battle import single_battle

character1 = Character(name="Jonas", char_type="smart",
                       max_health=100,
                       attack=25, defense=10,
                       speed=10, attacks=[delay_of_publication, group_presentation],
                       attack_strategy="random")

character2 = Character(name="Jan", char_type="smart",
                       max_health=100,
                       attack=25, defense=10,
                       speed=10, attacks=[mattermost_message_concerning_everybody,
                                          restricted_travel_funds,
                                          proposal_help,
                                          telling_different_phd_duration_times,
                                          cancels_meeting,
                                          declares_as_expert
                                          ],
                       attack_strategy="random")

winner = []
for _ in range(1000):
    winner.append(single_battle(character1, character2))
    character1.heal(character1.max_health)
    character2.heal(character2.max_health)
winner.count("Jonas") 
winner.count("Jan") 


# write graphics for the battles
