



from random import randint

LIVES = 6


def _get_words(file_path):
    "Takes location of file, returns list of words."
    file_text = open(file_path, "r") # "r" tahendab lugemis mode
    return file_text.readlines()


def get_random_word():
    "Give back random word"
    words = _get_words("sonad") # Teil .txt
    nr_words = len(words) - 1
    random_index = randint(0, nr_words)
    return words[random_index]


def hide_word(word):
    "Takes word, returns word length times '_' "
    repres = []
    for c in word:
        repres.append("_ ")
    return repres


def get_user_letter():
    "Get letter from user, return that letter."
    return input("Guess a letter: ")


def find_letters(letter, word):
    "Takes a letter and a word, returns positions of letter in word."
    word = word.lower()
    positions = []
    for pos in range(len(word)):
        if word[pos] == letter:
            positions.append(pos)
    return positions

def show_letters(letter, word, repres):
    """Takes a letter, word and a representation of a word and 
    returns representation with letter revealed."""
    letter_positions = find_letters(letter, word)
    for pos in letter_positions:
        repres[pos] = letter
    return repres


def dec_life():
    "Decerease life."
    global LIVES
    LIVES -= 1 # LIVES = LIVES - 1
    if LIVES == 0:
        return "Game Over"
    else:
        return "Next Move"


def play_again():
    "Ask if user wants to play again."
    inp = input("Do you want to play again?")
    if inp == "NO":
        return False
    else:
        return True

def display_guessed_letters(repres):
    "Print out representaion of word"
    for hl in repres:
        print(hl + " ", end="")
    print()
