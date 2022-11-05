from back_end.full_game import FullGame
from flask import Flask, render_template

app = Flask(__name__)
game = FullGame()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit/', methods=['POST'])
def start_game():
    game.new_instance()
    cards = game.get_cards()
    player_card = cards[0]
    computer_card = cards[1]

    return render_template('player-turn.html',
                           player_name=player_card['Name'],
                           player_image_link=player_card['Image'],
                           player_lifespan=player_card['Lifespan'],
                           player_minimum_length=player_card['Minimum length'],
                           player_maximum_length=player_card['Maximum length'],
                           player_minimum_weight=player_card['Minimum weight'],
                           player_maximum_weight=player_card['Maximum weight'],
                           )


@app.route('/submit/lifespan/', methods=['POST'])
def lifespan():
    cards = game.get_cards()
    computer_card = cards[1]
    player_card = cards[0]

    result = game.run_game('Lifespan')
    if result == 1:
        reason = "{} has a lifespan greater than a {}".format(player_card['Name'], computer_card['Name'])
        message = 'CONGRATULATIONS, YOU WON!'
        alert = 'success'
    elif result == -1:
        reason = "{} and {}, have the same lifespan".format(player_card['Name'], computer_card['Name'])
        message = "IT'S A DRAW!"
        alert = 'warning'
    else:
        reason = "{} has a lifespan greater than a {}".format(computer_card['Name'], player_card['Name'])
        message = 'SORRY, YOU LOSE!'
        alert = 'danger'

    return render_template('results.html',
                           player_name=player_card['Name'],
                           player_image_link=player_card['Image'],
                           player_lifespan=player_card['Lifespan'],
                           player_minimum_length=player_card['Minimum length'],
                           player_maximum_length=player_card['Maximum length'],
                           player_minimum_weight=player_card['Minimum weight'],
                           player_maximum_weight=player_card['Maximum weight'],

                           opponent_name=computer_card['Name'],
                           opponent_image_link=computer_card['Image'],
                           opponent_lifespan=computer_card['Lifespan'],
                           opponent_minimum_length=computer_card['Minimum length'],
                           opponent_maximum_length=computer_card['Maximum length'],
                           opponent_minimum_weight=computer_card['Minimum weight'],
                           opponent_maximum_weight=computer_card['Maximum weight'],

                           reason=reason,
                           message=message,
                           alert=alert
                           )


@app.route('/submit/minimum_length/', methods=['POST'])
def min_len():
    cards = game.get_cards()
    player_card = cards[0]
    computer_card = cards[1]

    result = game.run_game('Minimum length')
    if result == 0:
        reason = "{} is shorter than a {}".format(player_card['Name'], computer_card['Name'])
        message = 'CONGRATULATIONS, YOU WON!'
        alert = 'success'
    elif result == -1:
        reason = "{} and {}, have the same min length".format(player_card['Name'], computer_card['Name'])
        message = "IT'S A DRAW!"
        alert = 'warning'
    else:
        reason = "{} is shorter a than {}".format(computer_card['Name'], player_card['Name'])
        message = 'SORRY, YOU LOSE!'
        alert = 'danger'

    return render_template('results.html',
                           player_name=player_card['Name'],
                           player_image_link=player_card['Image'],
                           player_lifespan=player_card['Lifespan'],
                           player_minimum_length=player_card['Minimum length'],
                           player_maximum_length=player_card['Maximum length'],
                           player_minimum_weight=player_card['Minimum weight'],
                           player_maximum_weight=player_card['Maximum weight'],

                           opponent_name=computer_card['Name'],
                           opponent_image_link=computer_card['Image'],
                           opponent_lifespan=computer_card['Lifespan'],
                           opponent_minimum_length=computer_card['Minimum length'],
                           opponent_maximum_length=computer_card['Maximum length'],
                           opponent_minimum_weight=computer_card['Minimum weight'],
                           opponent_maximum_weight=computer_card['Maximum weight'],

                           reason=reason,
                           message=message,
                           alert=alert
                           )


@app.route('/submit/maximum_length/', methods=['POST'])
def max_len():
    cards = game.get_cards()
    player_card = cards[0]
    computer_card = cards[1]

    result = game.run_game('Maximum length')
    if result == 1:
        reason = "{} is longer than a {}".format(player_card['Name'], computer_card['Name'])
        message = 'CONGRATULATIONS, YOU WON!'
        alert = 'success'
    elif result == -1:
        reason = "{} and {}, have the same max length".format(player_card['Name'], computer_card['Name'])
        message = "IT'S A DRAW!"
        alert = 'warning'
    else:
        reason = "{} is longer than a {}".format(computer_card['Name'], player_card['Name'])
        message = 'SORRY, YOU LOSE!'
        alert = 'danger'

    return render_template('results.html',
                           player_name=player_card['Name'],
                           player_image_link=player_card['Image'],
                           player_lifespan=player_card['Lifespan'],
                           player_minimum_length=player_card['Minimum length'],
                           player_maximum_length=player_card['Maximum length'],
                           player_minimum_weight=player_card['Minimum weight'],
                           player_maximum_weight=player_card['Maximum weight'],

                           opponent_name=computer_card['Name'],
                           opponent_image_link=computer_card['Image'],
                           opponent_lifespan=computer_card['Lifespan'],
                           opponent_minimum_length=computer_card['Minimum length'],
                           opponent_maximum_length=computer_card['Maximum length'],
                           opponent_minimum_weight=computer_card['Minimum weight'],
                           opponent_maximum_weight=computer_card['Maximum weight'],

                           reason=reason,
                           message=message,
                           alert=alert
                           )


@app.route('/submit/minimum_weight/', methods=['POST'])
def min_weight():
    cards = game.get_cards()
    player_card = cards[0]
    computer_card = cards[1]

    result = game.run_game('Minimum weight')
    if result == 0:
        reason = "{} is lighter than a {}".format(player_card['Name'], computer_card['Name'])
        message = 'CONGRATULATIONS, YOU WON!'
        alert = 'success'
    elif result == -1:
        reason = "{} and {}, have the same min weight".format(player_card['Name'], computer_card['Name'])
        message = "IT'S A DRAW!"
        alert = 'warning'
    else:
        reason = "{} is lighter than a {}".format(computer_card['Name'], player_card['Name'])
        message = 'SORRY, YOU LOSE!'
        alert = 'danger'

    return render_template('results.html',
                           player_name=player_card['Name'],
                           player_image_link=player_card['Image'],
                           player_lifespan=player_card['Lifespan'],
                           player_minimum_length=player_card['Minimum length'],
                           player_maximum_length=player_card['Maximum length'],
                           player_minimum_weight=player_card['Minimum weight'],
                           player_maximum_weight=player_card['Maximum weight'],

                           opponent_name=computer_card['Name'],
                           opponent_image_link=computer_card['Image'],
                           opponent_lifespan=computer_card['Lifespan'],
                           opponent_minimum_length=computer_card['Minimum length'],
                           opponent_maximum_length=computer_card['Maximum length'],
                           opponent_minimum_weight=computer_card['Minimum weight'],
                           opponent_maximum_weight=computer_card['Maximum weight'],

                           reason=reason,
                           message=message,
                           alert=alert
                           )


@app.route('/submit/maximum_weight/', methods=['POST'])
def max_weight():
    cards = game.get_cards()
    player_card = cards[0]
    computer_card = cards[1]

    result = game.run_game('Maximum weight')
    if result == 1:
        reason = "{} is heavier than a {}".format(player_card['Name'], computer_card['Name'])
        message = 'CONGRATULATIONS, YOU WON!'
        alert = 'success'
    elif result == -1:
        reason = "{} and {}, have the same max weight".format(player_card['Name'], computer_card['Name'])
        message = "IT'S A DRAW!"
        alert = 'warning'
    else:
        reason = "{} is heavier than a {}".format(computer_card['Name'], player_card['Name'])
        message = 'SORRY, YOU LOSE!'
        alert = 'danger'

    return render_template('results.html',
                           player_name=player_card['Name'],
                           player_image_link=player_card['Image'],
                           player_lifespan=player_card['Lifespan'],
                           player_minimum_length=player_card['Minimum length'],
                           player_maximum_length=player_card['Maximum length'],
                           player_minimum_weight=player_card['Minimum weight'],
                           player_maximum_weight=player_card['Maximum weight'],

                           opponent_name=computer_card['Name'],
                           opponent_image_link=computer_card['Image'],
                           opponent_lifespan=computer_card['Lifespan'],
                           opponent_minimum_length=computer_card['Minimum length'],
                           opponent_maximum_length=computer_card['Maximum length'],
                           opponent_minimum_weight=computer_card['Minimum weight'],
                           opponent_maximum_weight=computer_card['Maximum weight'],

                           reason=reason,
                           message=message,
                           alert=alert
                           )


if __name__ == '__main__':
    app.run()
