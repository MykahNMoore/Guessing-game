import random
number = random.randint(1,10)

player_name = input("Hello! What's your name?" )
number_of_guesses = 0
print(player_name+', '+'guess a number between one through ten.')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        print("Congrats, you win!")
        break
if guess == number:
    print("You guessed the number in " + str(number_of_guesses) +" " + "tries!")
 
else:
     print("You lose! The number was " + str(number))
