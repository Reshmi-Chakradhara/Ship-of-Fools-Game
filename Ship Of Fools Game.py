import random


class Die:
    """Die class to generate random integer values"""

    def __init__(self):
        """init method to roll the die """
        self.roll()

    def roll(self):
        """roll method to generate random integer between 1-6"""
        self._value = random.randint(1, 6)

    def get_value(self):
        """get_value method to return the die value"""
        return self._value


class DiceCup:
    """DiceCup class to handle five objects of the Die class"""

    def __init__(self, variable):
        """init method to store the variable object value in the list of die"""
        self._dice = []
        self._bank = [False, False, False, False, False]
        for i in range(5):
            self._dice.append(Die())
        for i in range(variable):
            self._dice.append(Die())

    def value(self, index):
        """value method to get the value of the die"""
        return self._dice[index].get_value()

    def bank(self, index):
        """bank method to bank the die"""
        self._bank[index] = True

    def is_banked(self, index):
        """is_banked method to set the flag to true after the die is banked"""
        if self._bank[index] == True:
            return True
        else:
            return False

    def release(self, index):
        """release method to release a die"""
        self._bank[index] == False

    def release_all(self):
        """release_all method to release all the die"""
        self._bank = [False, False, False, False, False]

    def roll(self):
        """roll method to roll the die"""
        for i in range(0, 5):
            if self._bank[i] == False:
                self._dice[i].roll()


class Player:
    """Player class to calculate the score of each individual player"""

    def __init__(self, name_of_the_player):
        """init method to set the initial score of the player"""
        self._name = self.set_name(name_of_the_player)
        self._score = 0

    def set_name(self, name_string):
        """set_name method to set the name of the player"""
        return name_string

    def current_score(self):
        """current_score to give the current score of the player"""
        return self._score

    def reset_score(self):
        """reset_score to reset the score of the player"""
        self._score = 0

    def play_round(self, game_round):
        """play_round method is for the players to play the new round"""
        new_round = game_round
        self._score = self._score + new_round.round()


class PlayRoom:
    """PlayRoom class to handle a number of players and game every round,checks if any player reached the winning score"""

    def __init__(self):
        """init method to initialize the players of the playroom"""
        self._players = []

    def set_game(self, game):
        """set_game method to set the game"""
        self._game = game

    def add_player(self, player):
        """add_player method to add a player"""
        self._players.append(player)

    def reset_scores(self):
        """reset_scores method to reset the score of the game"""
        for i in range(len(self._players)):
            self._players[i].reset_score()

    def play_round(self):
        """play_round method to play next round"""
        for i in self._players:
            i.play_round(self._game)
            if self.game_finished():
                break
            else:
                pass

    def game_finished(self):
        """game_finished method to check the end of game"""
        empty = []
        x = 0
        while x < len(self._players):
            if self._players[x].current_score() >= 21:
                empty.append(True)
                x += 1
            else:
                empty.append(False)
                x += 1
        return any(empty)

    def print_scores(self):
        """print_scores method to print the score of the player"""
        for i in range(len(self._players)):
            print(self._players[i]._name, '=', self._players[i].current_score())

    def print_winner(self):
        """print_winner method to print the winner of the game"""
        for i in range(len(self._players)):
            if self._players[i].current_score() >= 21:
                print('The winner of the Ship Of Fools Game is:', self._players[i]._name)


class ShipOfFoolsGame:
    """ShipOfFoolsGame class to handle the logic of the game"""

    def __init__(self):
        """init method to initialize the value of dice cup and the winning score"""
        self._cup = DiceCup(5)
        self.winningscore = 21

    def round(self):
        """round method to carry out each round in the game and to calculate the crew score"""
        self._cup.release_all()
        self._cup.roll()
        has_a_ship = False
        has_a_captain = False
        has_a_crew = False
        crew = 0
        for rep in range(3):
            repl = []
            i = 0
            while i < 5:
                repl.append(self._cup._dice[i].get_value())
                i += 1
            print(repl)
            if not has_a_ship and (6 in repl):
                for i in range(5):
                    if repl[i] == 6:
                        self._cup.bank(i)
                        break
                has_a_ship = True
            else:
                if has_a_ship:
                    pass
                else:
                    self._cup.roll()
            if has_a_ship and not has_a_captain and 5 in repl:
                for i in range(5):
                    if repl[i] == 5:
                        self._cup.bank(i)
                        break
                has_a_captain = True
            else:
                if has_a_captain:
                    pass
                else:
                    self._cup.roll()
            if has_a_captain and not has_a_crew and (4 in repl):
                for i in range(5):
                    if repl[i] == 4:
                        self._cup.bank(i)
                        break
                has_a_crew = True
            else:
                if has_a_crew:
                    pass
                else:
                    self._cup.roll()
            if has_a_ship and has_a_captain and has_a_crew:
                if rep < 2:
                    for i in range(5):
                        if self._cup._dice[i].get_value() > 3:
                            self._cup.bank(i)
                        else:
                            self._cup.roll()
                elif rep == 2:
                    for i in range(5):
                        if self._cup.is_banked(i):
                            pass
                        else:
                            self._cup.bank(i)
        if has_a_ship and has_a_captain and has_a_crew:
            crew = sum(repl) - 15
            print('The Crew Score is:', crew)
            return crew
        else:
            print("The Crew Score is:", crew)
            return crew


if __name__ == '__main__':
    room = PlayRoom()
    room.set_game(ShipOfFoolsGame())
    room.add_player(Player('Bob'))
    room.add_player(Player('Rob'))
    room.reset_scores()
    print('The banked ship, the captain and the crew')
    while not room.game_finished():
        room.play_round()
        room.print_scores()
        room.print_winner()
