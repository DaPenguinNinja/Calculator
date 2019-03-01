#Guessing Game

#secret word entered by user
secret_word=input("Enter in your secret word to guess: ") 


guess = ""

#Guess counter: you only get 3 tries

counter=0   
while guess != secret_word and counter<3:
        guess = input("Enter in your guess: ")
        print (counter)
        counter += 1

#Issue right there where counter in the while loop iterates so counter =3 so it still gives an error and says I lose
if counter <3:
    print("You win and guessed correctly")
else:
    print("You lose and out of guesses")
