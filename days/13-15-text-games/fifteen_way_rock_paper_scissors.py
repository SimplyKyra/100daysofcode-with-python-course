import csv
import random

FILE_NAME = "data/battle-table.csv"
win_or_lose = {}


class Player:
    def __init__(self, name, games_won = 0):
        self.name = name
        self.games_won = games_won

    def increase_games_won(self):
        self.games_won += 1

    def get_games_won(self):
        return self.games_won


def print_header():
    print('-----------------------------------')
    print(' Fifteen Way Rock, Paper, Scissors ')
    print('-----------------------------------')
    print()


def store_the_options():
    with open(FILE_NAME) as fin:
        reader = csv.DictReader(fin)

        # Date from the csv file:
        # OrderedDict([('Attacker', 'Rock'), ('Rock', 'draw'), ('Gun', 'lose'), ('Lightning', 'lose'), ('Devil', 'lose'), ('Dragon', 'lose'), ('Water', 'lose'), ('Air', 'lose'), ('Paper', 'lose'), ('Sponge', 'win'), ('Wolf', 'win'), ('Tree', 'win'), ('Human', 'win'), ('Snake', 'win'), ('Scissors', 'win'), ('Fire', 'win')])
        # OrderedDict([('Attacker', 'Gun'), ('Rock', 'win'), ('Gun', 'draw'), ('Lightning', 'lose'), ('Devil', 'lose'), ('Dragon', 'lose'), ('Water', 'lose'), ('Air', 'lose'), ('Paper', 'lose'), ('Sponge', 'lose'), ('Wolf', 'win'), ('Tree', 'win'), ('Human', 'win'), ('Snake', 'win'), ('Scissors', 'win'), ('Fire', 'win')])

        for row in reader:
            attacker_name = row['Attacker']
            del row['Attacker']
            del row[attacker_name]

            win_or_lose[attacker_name] = {}

            for k in row.keys():
                can_defeat = row[k].strip().lower()
                win_or_lose[attacker_name][k] = can_defeat


def get_players_name():
    return input("What is your name?   ").strip()


def player_chooses_roll(name):
    roll_choice = ", ".join(win_or_lose)
    choice = input(f"Which do you choose {name}? {roll_choice}")
    while choice not in win_or_lose:
        choice = input(f"Did you spell it wrong? Which do you choose {name}?")
    return choice


def game_loop(player1, player2):
    count = 0
    max_games = 3

    while count < max_games:
        p1_roll = player_chooses_roll(player1.name)
        p2_roll = random.choice(list(win_or_lose.keys()))

        outcome = win_or_lose[p1_roll][p2_roll]

        print(f"Player1 ({player1.name}) rolled {p1_roll} against Player2 ({player2.name}) {p2_roll}.")

        if outcome == "draw":
            print("You tied! Adding a game to the play.")
            max_games += 1
        elif outcome == "win":
            player1.increase_games_won()
            print(f"{player1.name} won!")
        else:
            player2.increase_games_won()
            print(f"{player2.name} won!")
        count += 1

    print()
    print(f"Game over! Out of a total of {count} games:")
    if player1.get_games_won() == player2.get_games_won():
        print("     You tied!")
    elif player1.get_games_won() > player2.get_games_won():
        print(f"     Player1 ({player1.name}) won!")
    else:
        print(f"     Player2 ({player2.name}) won!")


def main():
    print_header()

    store_the_options()

    player1 = Player(get_players_name())
    player2 = Player("computer")

    print(f"Welcome to the game {player1.name}!")
    print()

    game_loop(player1, player2)


if __name__ == '__main__':
    main()


