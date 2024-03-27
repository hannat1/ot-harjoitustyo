import random

class Hangman:
    def __init__(self):
        self.words = ["ohjelmistotuotanto", "tietokone", "peli", "puhelin", "ohjelma", "pääsiäinen", "saippuakauppias", "suklaamuna", "keltainen", "hirsipuu", "yliopisto", "ammatti", "vaaleanpunainen"]

    def generate_word(self):
        self.word = random.choice(self.words)
        self.dictionary = {}
        index = 0 
        for i in self.word:
            self.dictionary[index] = i
            index += 1

    def amountof_letters(self):
        self.letters = {}
        for i, t in enumerate(self.word):
            self.letters[t] = i
        self.unique_letters_intheword = len(self.letters)


    def beginning(self):
        self.games_word = []
        print("")
        comand = input("start the game! press anything")
        self.generate_word()
        for i in self.word:
            self.games_word.append("_")
        print("guess the word")
        print("the length of the word is ", len(self.games_word))
        print("you are allowed 6 mistakes")
        print(self.games_word)
        self.amountof_letters()


    def main(self):
        self.beginning()
        given_letters = []
        count = 0
    
    
        while True:
            command = input("enter a letter: ")
            if command in given_letters:
                print("you gave this letter already!")
                print("try again")
                continue
            if command not in "abcdefghijklmnopqrstuvwxyzåäö":
                print("you didn't enter a valid letter")
                print("try again")
                continue
            if command == "":
                print("you didn't enter a valid letter")
                print("try again")
                continue
    
            if command in self.letters:
                count += 1
        
            given_letters.append(command)

            for key, value in self.dictionary.items():
                if value == command:
                    self.games_word[key] = value

            print((len(given_letters) - count), "mistakes")
            print(self.games_word)

            if count == self.unique_letters_intheword:
                print("YOU WON!")
                break
            if (len(given_letters) - count) == 6:
                print("YOU LOST")
                print("the word was", self.word)
                break



            
            


sovellus = Hangman()
sovellus.main()

