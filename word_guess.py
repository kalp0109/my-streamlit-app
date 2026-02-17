import random

class WordGuessGame:

    def __init__(self):
        self.words= [ "python", "laptop", "window", "garden", "bottle",
        "orange", "travel", "flower", "animal", "friend",
        "silver", "yellow", "market", "forest", 
        "island","developer", "algorithm", "function", "variable", "inheritance"]

        self.word = random.choice(self.words)
        self.attempts =10
        print(self.word)    


    def welcome(self):
        self.name = input("Please tell your name: ").capitalize()
        print(f"Welcome to word guessing game!, Good Luck {self.name}, you have 10 attempts to guess correct word.")
        print( f"\n Choose a word from list \n {self.words}")


    def play_game(self):
        while self.attempts>0:
            guess_words = input("\n Make a Guess!: ").lower()
            self.attempts-=1
                
            if guess_words == self.word:
                print("Congratulations! You guessed the word right!")
                break
            elif guess_words not in self.words:
                print(f"Please choose word from words list only. You have {self.attempts} attempts remaining.")
            else:
                print(f"Wrong!,You have {self.attempts} reamining.")

    
        else:
            print(f"You have no attempt remaining. Correct word is {self.word}")   


game = WordGuessGame()
game.welcome()
game.play_game()
