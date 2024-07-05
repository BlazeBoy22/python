#Step 1 
import random
from words import word_list
from hangart import stages

 

length = len(word_list)
a = (int(random.random()*length))
# b= random.randint(0,2)
chosen_word = word_list[a]
 

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
n = len(chosen_word)
# print('printing n ',n)
blank_word =['_']*n
 



live_count = 7
while True :
    count = 0
    if '_' not in blank_word:
        print('player won!!!')
        break
  
    guess = input("enter the char")
    check = False
    if guess in blank_word:
        print(f'{guess} is already in word_list')
    for index,item in enumerate(chosen_word): 
        if item == guess:
            check = True
            blank_word[index]=guess
    print(f'current live count is {live_count}')
    print(blank_word)
    if check is False:
        live_count-=1
    
    if live_count==0:
        print('you lose')
        break
    print(stages[live_count-1])
    
