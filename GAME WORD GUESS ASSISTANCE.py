# ----------------------------------------------------------------------------------------------------------------GAME WORD GUESS ASSISTANCE

# writing letters

letters = [['h','o','l','i','d','a','y'],
           ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm','i','n','g'],
           ['b','o','o','t','c','a','m','p'],
           ['f','l','o','w','c','h','a','r','t'],
           ['w', 'o', 'r', 'd', 's', 'c', 'a','p','e','s']]

# writing words 

words = [["hi","hay","day","had","lay","dal","lad","lid","hold","lady","hail"],
         ["go","an","in","no","on","map","mom","gap","gag","pig","man","ping",
          "pong","pram","prom","ramp"],
         ["am","at","to","cab","cap","cob","cop","map","mop","act","bat","camp",
          "comb","boom","pact","atom"],
         ["of","at","or","to","caw","cow","how","who","calf","claw","flaw","flow",
          "fowl","wolf","crow","half"],
         ["we","do","as","cap","caw","cop","cow","paw","cod","dew","pad","cape",
          "cope","crap","crew","crop","pace"]]

# 1st we have defined the play game.

def play_game():
    wrong_guesses = 0
    for level, (level_letters, level_words) in enumerate(zip(letters, words), start=1):
# enumerate : it allows to iterate through  a sequence and keep a track of index of each element.
        
        print(f"Level {level}:")
        print("Letters:", "".join(level_letters))
        guessed_correctly = False
        for word in level_words:
            guess = input("Guess a word: ")
            if guess in level_words:
                print("Correct!")
            else:
                print("Wrong guess.")
                wrong_guesses += 1
                if wrong_guesses == 5:
                    print("You've made 5 wrong guesses. Game over.")
                    return
        guessed_correctly = True

    if guessed_correctly:
        print("Congratulations! You've completed all levels successfully.")

play_game() 
