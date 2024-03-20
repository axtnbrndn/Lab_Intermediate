secretword = "apple"
letters_guessed = []
chances = 6
while chances > 0:
  guess = input("guess a letter in secret word:")
  if len(guess) !="1":
    print("you can only guess one letter.")
  elif not guess.isalpha():
    print("you can only guess letters.")
  elif guess.lower()in letters_guessed:
    print("you have already guessed the letter")
  else:
    letters_guessed.append(guess.lower())
  if guess.lower() in secretword:
    print("correct guess")
  else:
    print("incorrect guess")
    chances-=1