print("#21 Building a Guessing Game!")
number=10
guess_count=1
guess_limit=3
while guess_count<=guess_limit:
    guess=int(input("Guess: "))
    guess_count=guess_count+1
    if guess==number:
        print("You Win!")
        break

else:print("Sorry, You Guessed wrong number.")