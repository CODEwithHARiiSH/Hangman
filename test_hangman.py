import hangman

def test_get_word_lowercase():
    assert hangman.get_word().islower()
