def break_words(stuff):
    """THis function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in full sentence and returns sorted words"""
    words = break_words(sentence)
    print sort_words(words)

def print_first_and_last(sentence):
    """Prints first and last word of sentence"""
    words = break_words(sentence)
    print_first_word(sentence)
    print_last_word(sentence)

sentence = "All is well";
print break_words(sentence)
