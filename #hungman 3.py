def get_secret_word():  
    word_list = ["Indonesia", "India", "Malaysia", "Singapore", "Vietnam", "Thailand"]
    return random.choice(word_list)
   
def play_game():
    secret_word = get_secret_word()  
    guessed_letters = []
    chances = 6

    while chances > 0:
        print("Word:", ''.join([letter if letter.lower() in guessed_letters else '_' for letter in secret_word]))
        guess = input("Guess a letter in my secret word: ")
        if len(guess) != 1:
            print("Please give me one letter.")
        elif not guess.isalpha():
            print("Please give me a letter.")
        elif guess.lower() in guessed_letters:  
            print("You already guessed that letter.")
        else:
           guessed_letters.append(guess.lower())
           if all(letter.lower() in guessed_letters for letter in secret_word):  
                print("Congratulations! You guessed the word.")
                return True
           elif guess.lower() in secret_word.lower():  
                print("Congrats, you guessed a letter!")
           else:
                chances -= 1
                print("Better luck next time. You have {} chances left.".format(chances))


    if chances == 0:
        print("Sorry, you ran out of chances. The word was:", secret_word)
        return False


def main():
    wins = 0
    losses = 0

    while True:
        if play_game():
            wins += 1
        else:
            losses += 1

        print("Wins: {}, Losses: {}".format(wins, losses))
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
    