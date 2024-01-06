import random as r
from colorama import Fore, Back, Style

MASK = "____"
DICTIONARY = "five_letters"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
colors_dic = {0: Back.LIGHTWHITE_EX, 1: Back.YELLOW, 2: Back.GREEN}


class Wordly:
    def __init__(self, display=print, user_input=input):
        self.mask = [0, 0, 0, 0, 0]
        self.display = display
        self.user_input = user_input
        self.dictionary = self._load_dictionary()
        self.word = self._get_word()

    @staticmethod
    def _load_dictionary():
        with open(DICTIONARY) as file:
            lst = [word.strip().upper() for word in file.readlines()]
            return lst

    def _get_word(self):
        return r.choice(self.dictionary)

    def print_color(self, word):
        for i, c in enumerate(word):
            print(Fore.BLACK + colors_dic[self.mask[i]] + c, end="")
        print(Style.RESET_ALL)

    def get_letter(self, prompt: str = "Adivina una letra\n"):
        output = self.user_input(prompt)
        return output

    def next_word(self, prompt: str = "Escribe una palabra\n"):
        while True:
            try:
                word = self.user_input(prompt).upper()
                if len(word) != 5:
                    raise ValueError("Solo 5 letras!")
                if not all([c in ABC for c in word]):
                    raise ValueError("Solo letras ingles!")
                if word not in self.dictionary:
                    raise ValueError("Solo las palabras que existen!")
                return word
            except ValueError as e:
                self.display(e)

    def move(self):
        for attempt in range(5):
            candidate = self.next_word()
            if candidate == self.word:
                self.mask = [2, 2, 2, 2, 2]
                self.print_color(candidate)
                self.display("you win!")
                return
            for i, c in enumerate(candidate):
                if c in self.word:
                    if candidate[i] == self.word[i]:
                        self.mask[i] = 2
                    else:
                        self.mask[i] = 1
                else:
                    self.mask[i] = 0
            self.print_color(candidate)
            # print(self.mask)


game = Wordly()
game.display(game.word)
# game.display(game.next_word())
# game.get_letter()
game.move()
