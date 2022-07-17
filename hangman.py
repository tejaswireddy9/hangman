import random
from words import word_list
def get_word():
    word=random.choice(word_list)
    return word.upper()
def play(word):
    word_complete = "_" * len(word)
    count=6
    guessed_letters=[]
    guessed_words=[]
    guessed=False
    print("Lets play Hangman")
    print("no.of tries",count) 
    print(word_complete)
    print("\n")
    print("no.of letters in word is",len(word))
    print(display_hangman(count))
    while not guessed and count>0:
        guess=input("enter your guess ").upper()
        if(len(guess)==1 and guess.isalpha()):
            if(guess in guessed_letters):
                print("you already guessed the letter",guess)
            elif(guess not in word):
                guessed_letters.append(guess)
                count=count-1
                print("wrong guess,try again")
                print("no.of guesses left=",count)
            else:
                print("correct letter guessed")
                guessed_letters.append(guess)
                word_list_complete=list(word_complete)
                indices=[i for i,letter in enumerate(word) if letter==guess]
                for index in indices:
                   word_list_complete[index]=guess
                word_complete="".join(word_list_complete)
                if "_" not in word_complete:
                    guessed=True
        elif(len(guess)==len(word) and guess.isalpha()):
            if(guess in guessed_words):
                print("already guessed the word",guess)
            elif(guess!=word):
                print("wrong word guessed")
                guessed_words.append(guess)
                count=count-1
                print("no.of guesses left=" ,count)
            else:        
                guessed=True
                word_complete=word
        else:
            print("enter a valid guess")
        print(display_hangman(count))
        print(word_complete)
        print("\n")
    if guessed:
        print("Congrats")
        print("you guessed the word in",count, "tries")
    else:
        print("no more tries left")
        print("The word was",word)
def display_hangman(count):
    stages=["""
                ------
                |
                
            """,
            """
                ------
                |
                o
               
            """,
            """
                ------
                |
                o
                |

            """,
            """
                ------
                |
                o
               /|
               
            """,
            """
                ------
                |
                o
               /|\\
               
            """,
            """
                ------
                |
                o
               /|\\
                |

            """,
            """
                ------
                |
                o
               /|\\
                |
               / \\

            """
    ]
    return stages[6-count]      
def main():
    word=get_word()
    play(word)
    while(input("want to play again(Y/N)").upper()=='Y'):
        word=get_word()
        play(word)
if __name__=="__main__":
    main()

        
        

    

