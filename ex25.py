def break_words(stuff):
    return stuff.split(' ')
def sort_words(words):
    return sorted(words)
def print_first_word(words):
    word = words.pop(0)
    print(word)
    return word


def print_last_word(words):
    word = words.pop(-1)
    print(word)
    return word

def sort_sentence(sentence):
    return sort_words(break_words(sentence))

def print_first_and_last(words):
    word = break_words(words)
    print_first_word(word)
    print_last_word(word)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
