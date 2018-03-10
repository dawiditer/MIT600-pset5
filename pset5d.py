# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    orig_hand = hand.copy()
    words_created = dict()
    total_score,current_score = 0,0
    while len(hand) > 0:
        print "Current Hand: ",
        display_hand(hand)
        word = get_usr_input(hand,word_list)
        if word == '.':
            print "-"*51
            print "Game exited"
            break
        current_score = get_word_score(word, HAND_SIZE)
        words_created[word] = words_created.get(word,current_score)
        total_score += current_score
        hand = update_hand(hand,word)
        print "'%s' earned you %i points" % (word,current_score)
        print "Current Total Score: %i points" % (total_score)
        if len(hand) == 0:
            print "-"*51
            print "You used all the letters, nice"
            break
        print "New Hand: ",
        display_hand(hand)
        print 
    print "Given",
    display_hand(orig_hand)
    print "You created %i words:" % len(words_created)
    for key,val in words_created.items():
        print "-> %s earned %i points" %(key,val)
    if len(hand) > 0:
        print "Unused: ",
        display_hand(hand)
    print "Total Score: %i points" % total_score
    print "-"*51
