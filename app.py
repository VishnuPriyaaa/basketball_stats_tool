import constants
import copy


players_data = []
team_data = copy.deepcopy(constants.TEAMS)
teams_with_players = {}


def clean_data():
    """Cleans the player data by changing the values of guardians, experience and height properties"""
    temp_players_data = copy.deepcopy(constants.PLAYERS)
    for data in temp_players_data:
        player_data = {'name': data['name'], 'guardians': []}
        if len(data['guardians'].split("and")) > 1:
            player_data['guardians'] = data['guardians'].split(" and ")
        else:
            player_data['guardians'].append(data['guardians'])
        if data['experience'] == 'YES':
            player_data['experience'] = True
        else:
            player_data['experience'] = False
        player_data['height'] = int(data['height'].split(" ")[0])
        players_data.append(player_data)


def balance_teams():
    """Balances the team by reorganising the players for each time based on experience"""
    experienced_players = []
    non_experienced_players = []
    for player in players_data:
        if player['experience']:
            experienced_players.append(player)
        else:
            non_experienced_players.append(player)
    num_ex_players = int(len(experienced_players)/len(constants.TEAMS))
    num_non_ex_players = int(len(non_experienced_players)/len(constants.TEAMS))
    index = 0
    for team in constants.TEAMS:
        teams_with_players[team] = experienced_players[index:(index+num_ex_players)] \
                                   + non_experienced_players[index:(index+num_non_ex_players)]
        index += num_ex_players


def display_team_names():
    """Displays all the team names"""
    [print("{}) {}".format(count+1, team_name)) for count, team_name in enumerate(team_data)]


def display_avg_height(team_name):
    """Displays the average height by taking selected team name as parameter"""
    tot_height = sum([player['height'] for player in teams_with_players[team_name]])
    print("Average height: {}\n".format(tot_height/len(teams_with_players[team_name])))


def display_players_on_team(team_name):
    """Displays all the players under the selected team name"""
    print("Players on Team:")
    print(", ".join(player_details['name'] for player_details in teams_with_players[team_name]))


def display_guardians(team_name):
    """Displays the guardians list for the selected team name"""
    print("\nGuardians:")
    guardians_list = []
    for player in teams_with_players[team_name]:
        guardians_list.extend(player['guardians'])
    print(", ".join(guardian for guardian in guardians_list))


def display_players_count(team_name):
    """Displays the total, experienced and non-experienced player count for selected team name"""
    print("Total players: {}".format(len(teams_with_players[team_name])))
    exp_players_count = 0
    non_exp_players_count = 0
    for player in teams_with_players[team_name]:
        if player['experience']:
            exp_players_count += 1
        else:
            non_exp_players_count += 1
    print("Total experienced: {}".format(exp_players_count))
    print("Total inexperienced: {}".format(non_exp_players_count))


def display_team_stats():
    """Displays all the stats for the teams"""
    display_team_names()
    try:
        selected_team_index = int(input("Enter an option: ")) - 1
        if team_data[selected_team_index]:
            team_name = team_data[selected_team_index]
            print("Team: {} Stats".format(team_name))
            print("--------------------")
            display_players_count(team_name)
            display_avg_height(team_name)
            display_players_on_team(team_name)
            display_guardians(team_name)
        else:
            print("Please select valid option")
    except ValueError:
        print("Please enter valid option to select team name")
        display_team_stats()
    except IndexError:
        print("Please enter a numeric value within the range of 1-{}".format(len(team_data)))
        display_team_stats()


def display_menu():
    """Displays menu for users"""
    print("""---- MENU----
Here are your choices:
    1) Display Team Stats
    2) Quit
    """)
    user_choice = input("Enter an option: ")
    if user_choice == '1':
        display_team_stats()
        input("Press Enter to continue...")
        display_menu()
    elif user_choice == '2':
        print("Thank you exploring our tool !!!")
    else:
        print("Please enter valid option")
        display_menu()


if __name__ == "__main__":
    print("BASKETBALL TEAM STATS TOOL")
    clean_data()
    balance_teams()
    display_menu()


