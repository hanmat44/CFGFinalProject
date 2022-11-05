from database.db_utils import view_score, clear_scores


class CheckScore:
    def __init__(self):
        self.player_score = view_score('person')
        self.computer_score = view_score('computer')

    def check_score(self):
        print("Your score is {}. The computer's score is {}.".format(self.player_score, self.computer_score))

    def reset_game(self):
        clear_scores()
        print("Scores reset")


if __name__ == '__main__':
    c = CheckScore()
    c.check_score()
    c.reset_game()
