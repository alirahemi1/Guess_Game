secret = 9
number_of_guesses = 0
guess_limit = 3
while number_of_guesses < guess_limit:
    user_guess = int(input("Guess a number: "))
    number_of_guesses += 1
    if number_of_guesses == guess_limit:
        print("You lose!")
        break
    if user_guess == secret:
        print("You win!")
        break
