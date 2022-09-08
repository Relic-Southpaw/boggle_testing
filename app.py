from crypt import methods
from flask import Flask, render_template, redirect, session, make_response, jsonify, request
from boggle import Boggle

bogs = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "boggleMind"

@app.route('/')
def board_to_page():
    if session == {}:
        make_board = bogs.make_board()
        session['board'] = make_board
        board = session['board']
        print(session)
    else:
        board = session['board']
    return render_template('base.html', board = board)
    
@app.route('/word_check')
def is_word():
    word = request.args["word"]
    board = session['board']
    print(board)
    print (word)
    valid_word = bogs.check_valid_word(board=board, word=word)
    print(valid_word)
    return jsonify({'result':valid_word})

@app.route('/new_board')
def new_board():
    session.clear()
    return redirect('/')
