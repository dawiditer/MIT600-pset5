#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    word_freq_dict = get_frequency_dict(word)
    for letter in word_freq_dict:
        if letter not in hand or hand[letter] - word_freq_dict[letter] < 0:
            return False
    return word in word_list
def get_usr_input(hand,word_list):
    """Asks user for input, validates and returns valid input(lowercase)"""
    invalid_input = False
    while True:
        if invalid_input: print "Invalid Input, Try again..."
        usr_input = raw_input("Enter a word (or a dot '.' to finish): ")
        if is_valid_word(usr_input, hand, word_list) or usr_input == '.':
            return usr_input.lower()
        invalid_input = True
