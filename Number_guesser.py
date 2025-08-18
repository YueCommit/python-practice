our_number = 42
guess = None
quit = False

# main while loop
while quit == False:
# while loop for guessing and comparing numbers
    while guess != our_number:
        guess = int(input("Enter an integer: "))
        if guess == our_number:
            print("Congratulations!")
        elif guess > our_number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
# if statement to check if the user wants to play again
        want_to_play_again = input("Do you want to play again? (yes/no): ")
        if want_to_play_again.lower() == "yes":
            print("Great! Let's play again.")
        if want_to_play_again == "no":
            quit = True