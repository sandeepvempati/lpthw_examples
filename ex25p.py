def break_words(stuff):
    print "This function will break the words for us"
    words = stuff.split(' ')
    return words

#print break_words("break the words")


def sort_words(words):
    print "sort the words"
    return sorted(words)

#print sort_words("I am good boy")

def print_first_word(words):
    print "print the first word after popping it off."
    word = words.pop(0)
    return word

#print print_first_word([1,2,3])

def print_last_word(words):
    print "print the last word after popping it."
    wordl = words.pop(-1)
    return wordl

#print print_last_word([1,3,4,2,5,5,6,5,7,7,8,9])

def sort_sentence(sentence):
    "Takes in full sentence and sort the words"
    words = break_words(sentence)
    return words

#print sort_sentence("sort the full word sentences")

def print_first_and_last_sentence(sentence):
    print "first and last words of the sentence"
    words = break_words(sentence)
    print print_first_word(words)
    print print_last_word(words)

#print print_first_and_last_sentence("first breaking the first and last")

def print_first_last_words_after_sorted(sentence):
    print "first and last word after sorted"
    words = sort_sentence(sentence)
    print "words %s" %words
    print print_first_word(words)
    print print_last_word(words)

#print print_first_last_words_after_sorted("first breaking the first and last")
