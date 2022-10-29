from full_game import FullGame
from flask import Flask, render_template

app = Flask(__name__)
game = FullGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit/', methods = ['POST'])
def start_game():
    game.new_instance()
    cards = game.get_cards()
    player_card = cards[0]
    computer_card = cards[1]

    return render_template('player-turn.html',
                           player_name=player_card['Name'],
                           player_lifespan=player_card['Lifespan'],
                           player_minimum_length=player_card['Minimum length'],
                           player_maximum_length=player_card['Maximum length'],
                           player_minimum_weight=player_card['Minimum weight'],
                           player_maximum_weight=player_card['Maximum weight']
                           )

@app.route('/submit/lifespan/', methods = ['POST'])
def lifespan():
    cards = game.get_cards()
    player_card = cards[0]
    computer_card = cards[1]

    result = game.run_game('Lifespan')
    if result:
        message = 'You Won!'
        alert = 'success'
    else:
        message = 'You Lose!'
        alert = 'danger'

    return render_template('results.html',
                           player_name=player_card['Name'],
                           player_lifespan=player_card['Lifespan'],
                           player_minimum_length=player_card['Minimum length'],
                           player_maximum_length=player_card['Maximum length'],
                           player_minimum_weight=player_card['Minimum weight'],
                           player_maximum_weight=player_card['Maximum weight'],

                           opponent_name=computer_card['Name'],
                           opponent_lifespan=computer_card['Lifespan'],
                           opponent_minimum_length=computer_card['Minimum length'],
                           opponent_maximum_length=computer_card['Maximum length'],
                           opponent_minimum_weight=computer_card['Minimum weight'],
                           opponent_maximum_weight=computer_card['Maximum weight'],

                           message = message,
                           alert = alert
                           )


@app.route('/submit/minimum_length/', methods=['POST'])
def min_len():
    cards = game.get_cards()
    player_card = cards[0]
    computer_card = cards[1]

    result = game.run_game('Minimum length')
    if result:
        message = 'You Won!'
        alert = 'success'
    else:
        message = 'You Lose!'
        alert = 'danger'

    return render_template('results.html',
                           player_name=player_card['Name'],
                           player_lifespan=player_card['Lifespan'],
                           player_minimum_length=player_card['Minimum length'],
                           player_maximum_length=player_card['Maximum length'],
                           player_minimum_weight=player_card['Minimum weight'],
                           player_maximum_weight=player_card['Maximum weight'],

                           opponent_name=computer_card['Name'],
                           opponent_lifespan=computer_card['Lifespan'],
                           opponent_minimum_length=computer_card['Minimum length'],
                           opponent_maximum_length=computer_card['Maximum length'],
                           opponent_minimum_weight=computer_card['Minimum weight'],
                           opponent_maximum_weight=computer_card['Maximum weight'],

                           message=message,
                           alert=alert
                           )


@app.route('/submit/maximum_length/', methods=['POST'])
def max_len():
    cards = game.get_cards()
    player_card = cards[0]
    computer_card = cards[1]

    result = game.run_game('Maximum length')
    if result:
        message = 'You Won!'
        alert = 'success'
    else:
        message = 'You Lose!'
        alert = 'danger'

    return render_template('results.html',
                           player_name=player_card['Name'],
                           player_lifespan=player_card['Lifespan'],
                           player_minimum_length=player_card['Minimum length'],
                           player_maximum_length=player_card['Maximum length'],
                           player_minimum_weight=player_card['Minimum weight'],
                           player_maximum_weight=player_card['Maximum weight'],

                           opponent_name=computer_card['Name'],
                           opponent_lifespan=computer_card['Lifespan'],
                           opponent_minimum_length=computer_card['Minimum length'],
                           opponent_maximum_length=computer_card['Maximum length'],
                           opponent_minimum_weight=computer_card['Minimum weight'],
                           opponent_maximum_weight=computer_card['Maximum weight'],

                           message=message,
                           alert=alert
                           )


@app.route('/submit/minimum_weight/', methods=['POST'])
def min_weight():
    cards = game.get_cards()
    player_card = cards[0]
    computer_card = cards[1]

    result = game.run_game('Minimum weight')
    if result:
        message = 'You Won!'
        alert = 'success'
    else:
        message = 'You Lose!'
        alert = 'danger'

    return render_template('results.html',
                           player_name=player_card['Name'],
                           player_lifespan=player_card['Lifespan'],
                           player_minimum_length=player_card['Minimum length'],
                           player_maximum_length=player_card['Maximum length'],
                           player_minimum_weight=player_card['Minimum weight'],
                           player_maximum_weight=player_card['Maximum weight'],

                           opponent_name=computer_card['Name'],
                           opponent_lifespan=computer_card['Lifespan'],
                           opponent_minimum_length=computer_card['Minimum length'],
                           opponent_maximum_length=computer_card['Maximum length'],
                           opponent_minimum_weight=computer_card['Minimum weight'],
                           opponent_maximum_weight=computer_card['Maximum weight'],

                           message=message,
                           alert=alert
                           )


@app.route('/submit/maximum_weight/', methods=['POST'])
def max_weight():
    cards = game.get_cards()
    player_card = cards[0]
    computer_card = cards[1]

    result = game.run_game('Maximum weight')
    if result:
        message = 'You Won!'
        alert = 'success'
    else:
        message = 'You Lose!'
        alert = 'danger'

    return render_template('results.html',
                           player_name=player_card['Name'],
                           player_lifespan=player_card['Lifespan'],
                           player_minimum_length=player_card['Minimum length'],
                           player_maximum_length=player_card['Maximum length'],
                           player_minimum_weight=player_card['Minimum weight'],
                           player_maximum_weight=player_card['Maximum weight'],

                           opponent_name=computer_card['Name'],
                           opponent_lifespan=computer_card['Lifespan'],
                           opponent_minimum_length=computer_card['Minimum length'],
                           opponent_maximum_length=computer_card['Maximum length'],
                           opponent_minimum_weight=computer_card['Minimum weight'],
                           opponent_maximum_weight=computer_card['Maximum weight'],

                           message=message,
                           alert=alert
                           )

if __name__ == '__main__':
    app.run()




