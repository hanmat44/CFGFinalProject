from db_utils import view_score, clear_scores

player_score = view_score('person')
computer_score = view_score('computer')

print("Your score is {}. The computer's score is {}.".format(player_score, computer_score))
clear_scores()
print("Scores reset")