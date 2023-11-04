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
            elif len(word) < 5:
                continue
            good_words.append(word)
    secret_word= random.choice(good_words)
    return secret_word
    
def get_mask_word(word, guesses):
    ret=[]
    for i in word:
        if i in guesses:
            ret.append(i)
        else:
            ret.append("-")
    return "".join(ret)
    
def get_status(secret_word, turns_remaining, guesses):
    masked_word = get_mask_word(secret_word, guesses)
    guesses = "".join(guesses)
    return f"""Secret word : {masked_word}
Turns remaining : {turns_remaining}
Guesses so far : {guesses}
"""    

    

            

    


    
    



    
    
    
    
    
    
    
    
    
    
    
