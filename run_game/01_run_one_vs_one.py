import os
os.chdir("/home/manuel/Documents/game")

#import character class
from game.characters.character_class import Character 

#import attacks
from game.attacks.attacks import mattermost_message_concerning_everybody, \
                                 restricted_travel_funds, group_presentation, proposal_help, \
                                 telling_different_phd_duration_times, delay_of_publication, \
                                 cancels_meeting, declares_as_expert, travel_money_use

#import battle function
from game.battle import team_battle

ps1 = Character(name="Y1", char_type="smart",
                       max_health=100,
                       attack=25, defense=10,
                       speed=10, attacks=[travel_money_use, group_presentation],
                       attack_strategy="random")

ps2 = Character(name="Y2", char_type="smart",
                       max_health=100,
                       attack=25, defense=10,
                       speed=10, attacks=[delay_of_publication, group_presentation],
                       attack_strategy="random")

sv = Character(name="X", char_type="smart",
                       max_health=400,
                       attack=25, defense=10,
                       speed=10, attacks=[mattermost_message_concerning_everybody,
                                          restricted_travel_funds,
                                          proposal_help,
                                          telling_different_phd_duration_times,
                                          cancels_meeting,
                                          declares_as_expert
                                          ],
                       attack_strategy="random")

characters = [ps1, ps2]

winner = []
for _ in range(1):
    winner.append(team_battle([ps1, ps2], [sv]))
    ps1.heal(ps2.max_health)
    ps2.heal(ps2.max_health)
    sv.heal(sv.max_health)
    
winner.count("Team 1") 
winner.count("Team 2") 


# write graphics for the battles
