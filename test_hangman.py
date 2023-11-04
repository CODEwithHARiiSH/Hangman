import os
import hangman

def test_get_word_lowercase():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["Grape\n", "apple\n", "Mango\n"])
    for _ in range(100):
        assert hangman.get_word(fname) == "apple"
    os.unlink(fname)
    
def test_random_word_no_punctuation():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["grape's\n", "apple\n", "mango'j\n"])
    for _ in range(100):
        assert hangman.get_word(fname) == "apple"
    os.unlink(fname)
 
    
def test_random_words_minlen5():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["god\n", "apple\n", "dad\n"])
    for _ in range(100):
        assert hangman.get_word(fname) == "apple"
    os.unlink(fname)


def test_random_word_no_repeated_words():
    words = {hangman.get_word() for _ in range(10)}
    assert len(words) == 10

def test_mask_word_no_guesses():
    guesses = []
    word = "cat"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "---"

def test_mask_word_single_wrong_guess():
    guesses = ['x']
    word = "elephant"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "--------"
    
def test_mask_word_single_correct_guess():
    guesses = ['t']
    word = "cat"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "--t"

def test_mask_word_two_correct_guesses():
    guesses = ['p','t']
    word = "elephant"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "---p---t"
    
def test_mask_word_single_guess_multiple_occurrence():
    guesses = ['e', 'p','t']
    word = "elephant"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "e-ep---t"


def test_get_status():
    secret_word = "policeman"
    turns_remaining = 75
    guesses = ['i','c','x']
    status = hangman.get_status(secret_word,
                                 turns_remaining,
                                 guesses,
                                 )
    assert status ==  """Secret word : ---ic----
Turns remaining : 75
Guesses so far : icx
"""



def test_play_round_correct_guess():
    secret_word = "rhino"
    guesses = []
    guess = "i"
    turns_remaining = 8
    guesses, turns_remaining, next_action = hangman.play_round(secret_word,
                                                               guesses,
                                                               guess,
                                                               turns_remaining)
    assert guesses == ['i']
    assert turns_remaining == 8
    assert next_action == "Keep Guessing"



def test_play_round_wrong_guess_game_not_over():
    secret_word = "rhino"
    guesses = ['q']
    guess = "x"
    turns_remaining = 8
    guesses, turns_remaining, next_action = hangman.play_round(secret_word,
                                                               guesses,
                                                               guess,
                                                               turns_remaining)
    assert guesses == ['q','x']
    assert turns_remaining == 7
    assert next_action == "Keep Guessing"
    
    
def test_play_round_wrong_guess_game_over():
    secret_word = "rhino"
    guesses = ['q']
    guess = "x"
    turns_remaining = 1
    guesses, turns_remaining, next_action = hangman.play_round(secret_word,
                                                               guesses,
                                                               guess,
                                                               turns_remaining)
    assert next_action == "GAME__OVER"


def test_play_round_game_win():
    secret_word = "rhino"
    guesses = ['r','h', 'i', 'n']
    guess = "o"
    turns_remaining = 1
    guesses, turns_remaining, next_action = hangman.play_round(secret_word,
                                                               guesses,
                                                               guess,
                                                               turns_remaining)
    assert next_action == "CONGRATZZ YOU WON"

def test_play_round_repeated_guess():
    secret_word = "rhino"
    guesses = ['r','h']
    guess = "h"
    turns_remaining = 5
    guesses, turns_remaining, next_action = hangman.play_round(secret_word,
                                                               guesses,
                                                               guess,
                                                               turns_remaining)
    assert guesses == ['r', 'h']
    assert turns_remaining == 5
    assert next_action == "Keep Guessing"






















 
