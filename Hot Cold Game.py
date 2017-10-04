#Hot/Cold Game

import random

#NO NEGATIVES OR WORDS PROMPT DEFINITION
def get_non_negative_int(prompt):
    while True:
        try:
            value = int(raw_input(prompt))
        except ValueError:
            print("Sorry, that's not a valid response")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value

#WHAT DOES A GUESS LOOK LIKE
def guess_number():
    guess = get_non_negative_int("What's your guess? ")
    if true_value > guess:
        print "Nope. Too low."
        x=0
    elif true_value < guess:
        print "Nope. Too high."
        x=0
    else:
        print "Correct!"
        x=1
    return x

#NOW LET'S PLAY THIS OUT
print "*" * 20
print "*" * 20
print "*" * 20
print "*" * 20
print "*" * 20
print "*" * 20
difficulty = get_non_negative_int("What would you like the upper bound to be? ")
print "I am generating a random number between 1 and %s." %difficulty

true_value = random.randrange(1,difficulty)

z=0
x=0
while (x<1):
    z = z + 1
    x = guess_number()
    
print "You got the right answer in %d tries!" %z