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


def play_round(secret_word, guesses, guess, turns_remaining):
    action = "Keep Guessing"
    if len(guess) >= 2:
        return guesses, turns_remaining, "Invalid Entry -----> Keep Guessing"
    if not guess.isalpha():
        return guesses, turns_remaining, "Invalid Entry -----> Keep Guessing"
    if not guess.islower():
        return guesses, turns_remaining, "Invalid Entry -----> Keep Guessing"
    if guess in guesses:
        return guesses, turns_remaining, action
    guesses.append(guess)
    if "-" not in get_mask_word(secret_word, guesses):
        return guesses, turns_remaining, "CONGRATZZ YOU WON"
    if guess not in secret_word:
        turns_remaining -=1
        if turns_remaining == 0:
            return guesses, turns_remaining, "GAME__OVER" 
    return guesses, turns_remaining, action    

def get_image(turns_remaining):
    if turns_remaining == 6:
    
        return """
      
----------
|        |
|
|
|
|
|
|
|
"""

    elif turns_remaining == 5:
    
        return """
      
----------
|        |
|        0
|
|
|
|
|
|
"""
    
    elif turns_remaining == 4:
    
        return """
      
----------
|        |
|        0
|        |
|
|
|
|
|
"""  

    elif turns_remaining == 3:
    
        return """
      
----------
|        |
|        0
|       /|
|
|
|
|
|
"""             

    
    elif turns_remaining == 2:
    
        return """
      
----------
|        |
|        0
|       /|/
|
|
|
|
|
""" 

    elif turns_remaining == 1:
    
        return """
      
----------
|        |
|        0
|       /|/
|       /
|
|
|
|
"""     
    
    elif turns_remaining == 0:
    
        return """
      
----------
|        |
|        0
|       /|/
|       / /
|
|
|
|
""" 


def main():
    print ("Welcome to Hangman!")
    print ("-------------------\n\n")
    secret_word = get_word()
    turns_remaining = 6
    guesses = []
    action=""
    while True:
        status = get_status(secret_word, turns_remaining, guesses)
        image = get_image(turns_remaining)
        print(image)
        print (status)
        print(action)
        guess = input("Enter your guess--->")
        guesses, turns_remaining, next_action = play_round(secret_word, guesses, guess, turns_remaining)
        action=next_action
        if next_action == "GAME__OVER":
            image = get_image(turns_remaining)
            print(image)
            print (f"You lost. The word is {secret_word}")
            print(next_action)
            break
        if next_action == "CONGRATZZ YOU WON":
            print (f"You won. The word is {secret_word}")
            print(next_action)
            break

if __name__ == "__main__":
    main()
        
    
    
    
    
    
    
    
    
    
    
