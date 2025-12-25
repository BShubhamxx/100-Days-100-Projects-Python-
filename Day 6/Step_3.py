import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
correct = []
game_end = False
while not game_end:
    guess = input("Guess a letter: ").lower()

    display = ""

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct.append(guess)
        elif letter in correct:
            display += letter
        else:
            display += "_"

    print(display)

    if '_' not in display:
        game_end = True
        print("You win!")
