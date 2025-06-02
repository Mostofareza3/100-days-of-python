import random

names = ["Luke", "Quang", "Bao", "Vu", "Josh", "Zulqarnine", "Mikhail", "Mostofa"]
random_name = random.choice(names).lower()  # Convert to lowercase for consistent comparison
lives = len(random_name) + 3
guessed_letters = set()


def get_star_sign(name):
    starred_name = ""
    for letter in name:
        if letter in guessed_letters:
            starred_name += letter
        else:
            starred_name += "*"
    return starred_name


print("Guess the name! You have", lives, "lives.")
while lives > 0:
    print("\nCurrent word:", get_star_sign(random_name))

    guessed_letter = input("Guess a letter: ").lower()

    if not guessed_letter.isalpha() or len(guessed_letter) != 1:
        print("Please enter a single valid letter.")
        continue

    if guessed_letter in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guessed_letter)

    if guessed_letter in random_name:
        print("Good guess!")
    else:
        lives -= 1
        print("Wrong guess. Lives left:", lives)

    if get_star_sign(random_name) == random_name:
        print("\nCongratulations! You guessed the name:", random_name.title())
        break
else:
    print("\nGame over! The correct name was:", random_name.title())