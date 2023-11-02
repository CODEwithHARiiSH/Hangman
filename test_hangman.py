import hangman

def test_get_word_lowercase():
    assert hangman.get_word().islower()
    
def test_random_word_no_punctuation():
    assert hangman.get_words().isalpha()


 
