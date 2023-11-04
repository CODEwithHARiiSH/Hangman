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







































 