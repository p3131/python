import random

print("welcome to hangman")
print("-------------------------------------------------------\n")

word_dictionary = ["house", "flower", "computer"]

random_word = random.choice(word_dictionary)

for x in random_word:
    print("_", end=" ")

def print_hangman(wrong):
    if wrong == 1:
        print("\n +----+\n\n")
    elif wrong == 2:
        print("\n +----+")
        print(" |     ")
        print(" |     ")
        print(" |       ")
        print(" |     ")
        print(" |       ")
        print(" |     ")
        print("       ")
    elif wrong == 3:
        print("\n +----+")
        print(" |    |")
        print(" |     ")
        print(" |       ")
        print(" |     ")
        print(" |       ")
        print(" |     ")
        print("       ")
    elif wrong == 4:
        print("\n +----+")
        print(" |    |")
        print(" |     ")
        print(" |       ")
        print(" |     ")
        print(" |       ")
        print(" |     ")
        print("---    ")
    elif wrong == 5:
        print("\n +----+")
        print(" |    |")
        print(" |    O")
        print(" |       ")
        print(" |     ")
        print(" |       ")
        print(" |     ")
        print("---    ")
    elif wrong == 6:
        print("\n +----+")
        print(" |    |")
        print(" |    O")
        print(" |    |  ")
        print(" |    |")
        print(" |       ")
        print(" |     ")
        print("---    ")
    elif wrong == 7:
        print("\n +----+")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |    |")
        print(" |       ")
        print(" |     ")
        print("---    ")
    elif wrong == 8:
        print("\n +----+")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |    |")
        print(" |   / \\")
        print(" |     ")
        print("---    ")

def print_word(guessed_letter):
    counter = 0
    right_letters = 0
    for char in random_word:
        if char in guessed_letter:
            print(random_word[counter], end=" ")
            right_letters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return right_letters

def print_lines():
    print("\r")
    for char in random_word:
        print("\u203E", end=" ")
    print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")

length_of_word_to_guess = len(random_word)
amount_of_times_worng = 0
current_letters_guessed = []
current_letters_right = 0
while(amount_of_times_worng < 8 and current_letters_right != length_of_word_to_guess):
    if current_letters_guessed:
        print("\nletters guessed so far:")
        for letter in current_letters_guessed:
            print(letter, end=" ")
    letter_guessed = input("\n\nGuess a letter: ")
    if letter_guessed in current_letters_guessed:
        print("You guessed this letter")
        continue
    elif letter_guessed not in random_word:
        amount_of_times_worng += 1
        print_hangman(amount_of_times_worng)
    current_letters_guessed.append(letter_guessed)
    current_letters_right = print_word(current_letters_guessed)
    print_lines()
print("\n\nGame is over! Thank you for playing.\n")
