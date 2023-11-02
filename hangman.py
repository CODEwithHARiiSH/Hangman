import random


def get_word(wordlist="/usr/share/dict/words"):
    good_words=[]
    with open(wordlist) as f:
        words=[x.strip() for x in f]
        for word in words:
            if not word.islower():
                continue
            elif not word.isalpha():
                continue
            good_words.append(word)
    return random.choice(good_words)
        
