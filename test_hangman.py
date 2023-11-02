import hangman

def test_get_word_lowercase():
    assert hangman.get_word().islower()
    
def test_random_word_no_punctuation():
    assert hangman.get_word().isalpha()
    
def test_random_words_minlen5():
    assert len(hangman.get_word()) >= 5


 
