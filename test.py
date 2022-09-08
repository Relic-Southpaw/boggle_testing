from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    """for these test cases I referenced and re-factored the solution to
    work with my current code set up.  Some of this I might not have figured
    out quickly and to be honest I am quite strapped for time and put a lot of 
    time figuring out the rest of this."""

    # TODO -- write tests for every view function / feature!
    def test_setup(self):
        """this checks to see that the request is valid
        as well as showing that the generated board is 
        set to the html"""
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertIn('<tr class="row">', html)
            self.assertEqual(res.status_code, 200)
    
    def test_word_good(self):
        """obviously I looked at the solution for this part
        I re-factored it to work with my code and I understand how 
        it works, would not have figured out about how to get the session
        board easily.  Anyways, this makes a fake session and tests
        if the word is in it."""
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]]
        response = client.get('/word_check?word=cat')
        self.assertEqual(response.json['result'], 'ok')
    
    def test_word_bad(self):
        """obviously I looked at the solution for this part
        I re-factored it to work with my code and I understand how 
        it works, would not have figured out about how to get the session
        board easily.  Anyways, this makes a fake session and tests
        if the word is not in it"""
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]]
        response = client.get('/word_check?word=dog')
        self.assertEqual(response.json['result'], 'not-on-board')
    
    def test_word_not_real(self):
        """obviously I looked at the solution for this part
        I re-factored it to work with my code and I understand how 
        it works, would not have figured out about how to get the session
        board easily.  Anyways, this makes a fake session and tests
        if the word isn't really a word."""
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]]
        response = client.get('/word_check?word=vegeta')
        self.assertEqual(response.json['result'], 'not-word')

    def test_new_game(self):
        """this checks to make sure it's redirected back to the home.
         on redirect back to '/' it will create a new board"""
        with app.test_client() as client:
            res = client.get('/new_board')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 302)