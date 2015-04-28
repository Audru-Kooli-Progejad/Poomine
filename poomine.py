



from random import randint


def _get_words(file_path):
    "Votab filei asukoha, annab tagasi listi sonadest."
    file_text = open(file_path, "r") # "r" tahendab lugemis mode
    return file_text.readlines()


def get_random_word():
    "Give back random word"
    words = _get_words("sonad") # Teil .txt
    nr_words = len(words) - 1
    random_index = randint(0, nr_words)
    return words[random_index]


def hide_word(word):
    return len(word) * "_ "


def get_user_letter():
    pass


def find_letters(letter, word):
    pass


def show_letters(letter, word):
    pass


def dec_life():
    pass


def play_again():
    pass


def display_guessed_letters():
    pass
