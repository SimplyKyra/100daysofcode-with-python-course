import random


class Player:
    def __init__(self, name, games_won = 0):
        self.name = name
        self.games_won = games_won

    def increase_games_won(self):
        self.games_won += 1

    def get_games_won(self):
        return self.games_won


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def print_header():
    print('---------------------------------')
    print('      Rock, Paper, Scissors      ')
    print('---------------------------------')


def get_players_name():
    name = input("What is your name?   ")
    print(f"Welcome to the game {name}!")
    print()
    return name


def build_the_three_rolls():
    return ['rock', 'paper', 'scissor']


def player_chooses_roll(name, rolls):
    roll_choice = ", ".join(rolls)
    choice = input(f"Which do you choose {name}? {roll_choice}")
    while not choice in rolls:
        choice = input(f"Which do you choose {name}? {roll_choice}")
    return choice


def can_defeat(p1_roll, p2_roll):
    if p1_roll == "rock" and p2_roll == "rock" or \
    p1_roll == "paper" and p2_roll == "paper" or \
    p1_roll == "scissor" and p2_roll == "scissor":
        return -1 # tie
    elif p1_roll == "rock" and p2_roll == "scissor" or \
    p1_roll == "paper" and p2_roll == "rock" or \
    p1_roll == "scissor" and p2_roll == "paper":
        return 1 # player one wins
    else:
        return 2 # player two wins


def game_loop(player1, player2, rolls):
    count = 0
    max_games = 3

    while count < max_games:
        p2_roll = random.choice(rolls)
        p1_roll = player_chooses_roll(player1.name, rolls)

        outcome = can_defeat(p1_roll, p2_roll)

        print(f"Player1 ({player1.name}) rolled {p1_roll} against Player2 ({player2.name}) {p2_roll}")

        if outcome == -1:
            print("You tied!")
            max_games += 1
        elif outcome == 1:
            player1.increase_games_won()
            print(f"{player1.name} won!")
        else:
            player2.increase_games_won()
            print(f"{player2.name} won!")
        count += 1

    print()
    print(f"Game over! Out of a total of {count} games")
    if player1.get_games_won() == player2.get_games_won():
        print("you tied!")
    elif player1.get_games_won() > player2.get_games_won():
        print(f"Player1 ({player1.name}) won!")
    else:
        print(f"Player2 ({player2.name}) won!")


if __name__ == '__main__':
    main()




