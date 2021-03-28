import turtle
window = turtle.Screen()
larry = turtle.Turtle()
import random

#the words
words=(
'quotes', 'spider', 'vowels', 'jacket', 'friend', 'family', 'tigers','picture',
'instant', 'example', 'diamond', 'kitchen', 'teacher', 'science', 'building', 'sandwich',
'mountain', 'basement', 'birthday', 'complete', 'princess', 'education', 'something',
'wednesday', 'integrity', 'knowledge', 'hamburger', 'influence', 'helicopter', 'silhouette',
'relaxation', 'watermelon', 'government', 'skateboard', 'rainforest')

i=random.randint(0, 34)
wrongGuesses=6
useless=0
empty=' _ '

#find word
if len(words[i]) == 6:
    word = words[i]
    fakeWord=[word[0],word[1],word[2],word[3],word[4],word[5]]
    display=[' _ ',' _ ',' _ ',' _ ',' _ ',' _ ']
    
elif len(words[i]) == 7:
    word = words[i]
    fakeWord=[word[0],word[1],word[2],word[3],word[4],word[5],word[6]]
    display=[' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ']
    
elif len(words[i]) == 8:
    word = words[i]
    fakeWord=[word[0],word[1],word[2],word[3],word[4],word[5],word[6],word[7]]
    display=[' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ']

elif len(words[i]) == 9:
    word = words[i]
    fakeWord=[word[0],word[1],word[2],word[3],word[4],word[5],word[6],word[7],word[8]]
    display=[' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ']

else:
    word = words[i]
    fakeWord=[word[0],word[1],word[2],word[3],word[4],word[5],word[6],word[7],word[8],word[9]]
    display=[' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ']
    
print("There are "+str(len(word))+ " letters in your word. Good luck!")

#hangman post
larry.penup()
larry.goto(-250,-280)
larry.pendown()
larry.left(90)
larry.forward(500)
larry.right(90)
larry.forward(60)
larry.right(135)
larry.forward(83)
larry.right(180)
larry.forward(83)
larry.right(45)
larry.forward(120)
larry.right(90)
larry.forward(80)
larry.right(90)

#guesses

while wrongGuesses>0:

    letterGuess=input('\nGuess a letter in your word: ')

    #if user chose right letter
    if letterGuess.lower() in word:
        
        print("There is a(n) "+letterGuess+" in your word.")
        letterLocation = word.find(letterGuess)
        fakeWord[letterLocation]=' '
        display[letterLocation]=letterGuess
        
        #if there's the same letter twice for display
        if letterGuess.lower() in fakeWord:
            letterLocation = ''.join(fakeWord).find(letterGuess)
           
            display[letterLocation]=letterGuess


        #checks if user has found the word 
        if empty in display:
            useless=6
        else:
            print(''.join(display))
            print("\nYou've found the word! Congrats!")
            break
        
    #if user incorrectly chose letter
    else:
        print("There is not a(n) "+letterGuess+" in your word.")
        wrongGuesses-=1
        
        if wrongGuesses == 5:
            #head
            larry.circle(50)

        elif wrongGuesses == 4:
            #body
            larry.penup()
            larry.left(90)
            larry.forward(100)
            larry.pendown()
            larry.forward(180)
            larry.right(180)
            larry.forward(130)

        elif wrongGuesses == 3:
            #right arm
            larry.right(55)
            larry.forward(100)
            larry.left(180)
            larry.forward(100)

        elif wrongGuesses == 2:
            #left arm
            larry.right(65)
            larry.forward(100)
            larry.left(180)
            larry.forward(100)

        elif wrongGuesses == 1:
            #left leg
            larry.right(60)
            larry.forward(130)
            larry.right(45)
            larry.forward(100)

        else:
            #right leg
            larry.right(180)
            larry.forward(100)
            larry.right(90)
            larry.forward(100)
            
    #display
    print(''.join(display))

#failure message
if wrongGuesses<1:
    print("\nYou lost :( ... The word was "+word)
