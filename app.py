import constants
from copy import deepcopy

# https://docs.python.org/3/library/copy.html
# This site is where I read about deepcopy

teams = deepcopy(constants.TEAMS)
players = deepcopy(constants.PLAYERS)
players_per_team = []


def clean_data():
    for player in players:
        player['height'] = player['height'].split()
        player['height'] = int(player['height'][0])
        player['guardians'] = player['guardians'].split('and')
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
    return players


def balance_teams(players):
    panthers = []
    bandits = []
    warriors = []
    #  https://levelup.gitconnected.com/item-for-item-in-list-comprehensions-if-you-want-to-master-it-237e2f7213ee
    #  This website helped me understand how looking for a condition in a list works. It helped to know
    #  the classification of each item in the expression.
    #  Expression -> Item -> Iterable -> Condition
    exp_players = [player for player in players if player['experience'] == True]
    inexp_players = [player for player in players if player['experience'] == False]
    while exp_players:
        panthers.append(exp_players.pop())
        bandits.append(exp_players.pop())
        warriors.append(exp_players.pop())
    while inexp_players:
        panthers.append(inexp_players.pop())
        bandits.append(inexp_players.pop())
        warriors.append(inexp_players.pop())
    teams_roster = [panthers, bandits, warriors]
    return teams_roster, panthers, bandits, warriors


def welcome_screen():
    print(('-'*7) + ' BASKETBALL TEAM STATS TOOL ' + ('-'*7) + '\n')
    print(('* '*9) + 'MENU ' + ('* '*9))
    print('\nHere are your choices:\n\n -- Main Menu --\n')


def select_team():
    print('\n\n -- Team Select menu --\n')
    for index, team in enumerate(teams, 1):
        print(f' {index}. {team}')
        

# Okay now this section... I was stuck displaying the team info for days!
# The hardest part was displaying the guardians in a neat way without them having
# weird spacing or getting put onto multiple lines.
# I eventually brute force replaced double spaces and spaces before commas by
# using a replace method. I know it isn't pretty but it got the job done lol.

def display_panthers():
    title_panthers = 'Team: Panthers Stats'
    panthers_length = len(panthers)
    panthers_roster = [player['name'] for player in panthers]
    panthers_string = ', '.join(panthers_roster)
    panthers_guardians = [player['guardians'] for player in panthers]
    exp_panthers = []
    inexp_panthers = []
    for player in panthers:
        if player['experience'] == True:
            exp_panthers.append(player)
        else:
            inexp_panthers.append(player)
    panther_avg_height = round(sum([player['height'] for player in panthers]) / panthers_length)
    print('\n\n' + title_panthers + '\n' + '-'*len(title_panthers))
    print('Total players: ' + str(panthers_length))
    print('Total experienced: ' + str(len(exp_panthers)))
    print('Total inexperienced: ' + str(len(inexp_panthers)))   
    print('Average height: ' + str(panther_avg_height))
    print('\nPlayers on Team:\n  ' + panthers_string + '\n')
    print('Guardians: ')
    panther_guardian_list = [item for guardian in panthers_guardians for item in guardian]
    guardian_list = str('  ' + ', '.join(panther_guardian_list) + '\n')
    panther_guardian_list = guardian_list.replace('  ', ' ')
    panther_guardian_list = panther_guardian_list.replace(' ,', ',')
    print(' ' + panther_guardian_list)

    
def display_bandits():
    title_bandits = 'Team: Bandits Stats'
    bandits_length = len(bandits)
    bandits_roster = [player['name'] for player in bandits]
    bandits_string = ', '.join(bandits_roster)
    bandits_guardians = [player['guardians'] for player in bandits]
    exp_bandits = []
    inexp_bandits = []
    for player in bandits:
        if player['experience'] == True:
            exp_bandits.append(player)
        else:
            inexp_bandits.append(player)
    bandit_avg_height = round(sum([player['height'] for player in bandits]) / bandits_length)
    print('\n\n' + title_bandits + '\n' + '-'*len(title_bandits))
    print('Total players: ' + str(bandits_length))
    print('Total experienced: ' + str(len(exp_bandits)))
    print('Total inexperienced: ' + str(len(inexp_bandits)))   
    print('Average height: ' + str(bandit_avg_height))
    print('\nPlayers on Team:\n  ' + bandits_string + '\n')
    print('Guardians: ')
    bandit_guardian_list = [item for guardian in bandits_guardians for item in guardian]
    guardian_list = str('  ' + ', '.join(bandit_guardian_list) + '\n')
    bandit_guardian_list = guardian_list.replace('  ', ' ')
    bandit_guardian_list = bandit_guardian_list.replace(' ,', ',')
    print(' ' + bandit_guardian_list)

def display_warriors():
    title_warriors = 'Team: Warriors Stats'
    warriors_length = len(warriors)
    warriors_roster = [player['name'] for player in warriors]
    warriors_string = ', '.join(warriors_roster)
    warriors_guardians = [player['guardians'] for player in warriors]
    exp_warriors = []
    inexp_warriors = []
    for player in warriors:
        if player['experience'] == True:
            exp_warriors.append(player)
        else:
            inexp_warriors.append(player)
    warrior_avg_height = round(sum([player['height'] for player in warriors]) / warriors_length)
    print('\n\n' + title_warriors + '\n' + '-'*len(title_warriors))
    print('Total players: ' + str(warriors_length))
    print('Total experienced: ' + str(len(exp_warriors)))
    print('Total inexperienced: ' + str(len(inexp_warriors)))   
    print('Average height: ' + str(warrior_avg_height))
    print('\nPlayers on Team:\n  ' + warriors_string + '\n')
    print('Guardians: ')
    warrior_guardian_list = [item for guardian in warriors_guardians for item in guardian]
    guardian_list = str('  ' + ', '.join(warrior_guardian_list) + '\n')
    warrior_guardian_list = guardian_list.replace('  ', ' ')
    warrior_guardian_list = warrior_guardian_list.replace(' ,', ',')
    print(' ' + warrior_guardian_list)
    

def menu_screen():
    while True:
        try:
            choices = ['Display Team Stats', 'Quit']
            for index, choice in enumerate(choices, 1):
                print(f' {index}. {choice}')
            user_choice = int(input('\nEnter an option: '))
            if user_choice == 1:
                select_team()
                team_choice = int(input('\nEnter an option: '))
                if team_choice == 1:
                    display_panthers()
                    input('\nInput any key and press ENTER to return to the main menu...')
                    print('\n')
                    continue
                elif team_choice == 2:
                    display_bandits()
                    input('\nInput any key and press ENTER to return to the main menu...')
                    print('\n')
                    continue
                elif team_choice == 3:
                    display_warriors()
                    input('\nInput any key and press ENTER to return to the main menu...')
                    print('\n')
                    continue
            elif user_choice == 2:
                quit()
            else:
                print('\nNot a valid option. Please try again.\n')
                continue
        except IndexError:
            print('\nThat is not a valid option. Please try again. \n')
        except ValueError:
            print('\nThat is not a valid option. Please try again. \n')
        

if __name__ == "__main__":
    teams_roster, panthers, bandits, warriors = balance_teams(clean_data())
    welcome_screen()
    menu_screen()

