# Word games
The rules of the game are as follows:
#### Dealing ####
A player is dealt a hand of n letters chosen at random (assume n=7 for now).
The player arranges the hand into a set of words using each letter at most once.
Some letters may remain unused (these won't be scored).

#### Scoring ####
The score for the hand is the sum of the score for the words.
The score for a word is the sum of the points for letters in the word, plus 50 points if all n
letters are used on the first go.

Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E
is worth 1, and so on. We have defined the dictionary `SCRABBLE_LETTER_VALUES`
that maps each lowercase letter to its Scrabble letter value.

For example, `'weed'` would be worth 8 points (4+1+1+2=8), as long as the hand actually
has 1 `'w'`, 2 `'e'`s, and 1 `'d'`.
As another example, if n=7 and you get `'waybill'` on the first go, it would be worth 65
points (4+1+4+3+1+1+1=15, +50 for the `'bingo'` bonus of using all seven letters).

