#Write a program to demand a user to backup their THANKDADDY Online Account with 3 words and if @ # $ %  Characters Are Included the program should be able to tell the user to use another Word without those Characters

#Function To Complete Backup or Enter Words Again
def checknum(words):
    countt = 0
    global x
    x = 0
    while countt < 1:
        if words == '1':
            print('Backup Succesfully')
            x += 1
            break
        elif words != '2':
            print('Invalid Selection')
            words = input('Press 1 to Continue or Press 2 to Enter Words again   ')
        elif words == '2':
            break

    return
            


#Function to Check words if Invalid Characters Included
def checkWord(word,list):
    count = 0
    while count < 1:
        if '@' in word:
            print('@ # $ %  Characters were Added')
            word = input('Enter A different word without @ # $ %  Characters Included ')
        elif '#' in word:
            print('@ # $ %  Characters were Added')
            word = input('Enter A different word without @ # $ %  Characters Included ')
        elif '$' in word:
            print('@ # $ %  Characters were Added')
            word = input('Enter A different word without @ # $ %  Characters Included ')
        elif '%' in word:
            print('@ # $ %  Characters were Added')
            word = input('Enter A different word without @ # $ %  Characters Included ')
        else:
            count += 1 
            list.append(word)
    print(f'{word} has Been Added to Backup Words')
    return


#Create A list For the Words
list = []

#Getting User Input
inp = input('Do you Wish to backup your THANKDADDY!!! ACCOUNT? press 1 for YES OR press 2 for NO   ')


#Setting Count for Getting Users Input
count = 0

#Looping through
while count < 3:
    if inp == '1':
        firstWord = input('Enter First Word  ')
        checkWord(firstWord,list)
        count += 1
        secondWord = input('Enter Second Word  ')
        checkWord(secondWord,list)
        count += 1
        thirdWord = input('Enter Third Word  ')
        checkWord(thirdWord,list)
        count += 1
        input('Press any key to see the words you choosed  ')
        print(list)
        keY = input('Are you Sure of Words? ... Press 1 to Continue or Press 2 to Enter Words again   ')
        checknum(keY)
        if x == 1:
            count += 3
        else:
            count -= 3
        
    elif inp == '2':
        break
    else:
        print('Input Must Either be 1 or 2')
        inp = input('press 1 for YES OR press 2 for NO    ')

#Ending Program
print('Thank You For USING THANKDADDY!!!')