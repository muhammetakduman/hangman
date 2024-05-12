name = input("Enter Name:")

print("hello  " + name + " , time to play hangman!")

secretWord = input("Please enter a word for the hangman game ,\nDo not show it to the user when entering the word : ").lower()

guess_string = ""

lives = 10

while lives > 0:
	
    
    character_left = 0

    for character in secretWord:

    	if character in guess_string:
    		print(character,end="")

    	else :
    		
    		print("-", end="")
    		character_left += 1
 
    if character_left == 0:
    	print(" , congratt !!!")
    	break


    guess = input ("Guess a word: ").lower()

    guess_string += guess

    if guess not in secretWord:
        lives -= 1
        print (",  Wrong!!!")
        print(f"You have {lives} left" )
        if lives == 0 :
        		print ("You died!")



	
