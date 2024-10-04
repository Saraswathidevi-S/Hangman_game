import random
from hangman_list import hangman_stages
from hangman_words import list1
print("Let's Play Hangman")
lists=random.choice(list1).lower()
length=len(lists)
lives=6
empty = ['_'] * length
print(hangman_stages[lives])
print(f"You have {lives} lives so try to guess the word within {lives} attempts! Good luck!!")
print(" ".join(empty))
game_over=False
while not game_over:
    user_input=input("Guess a letter:").lower()
    if len(user_input) != 1 or not user_input.isalpha():
        print("Please enter a valid single letter.")
        continue
    if user_input in lists:
        for i in range(length):
            if lists[i]==user_input:
                empty[i]=user_input
        print(" ".join(empty))
    else:
        lives-=1
        print(hangman_stages[lives])
        print(f"You guessed '{user_input}', which is not present in the word. You lose a life")
    if lives==0:
        game_over=True
        print("you lose!! The word was:",lists)
    if '_' not in empty:
        game_over=True
        print("Congratulations! You win!!")
