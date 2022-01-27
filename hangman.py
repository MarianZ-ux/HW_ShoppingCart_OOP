

hMan = ['coconut', 'copper', 'iron', 'lithium', 'cricket', 'ranunculus', 'girrafe', 'mango', 'banana', 'moose', 'wolf']
import random

random_int = random.randint(0,11)
#return hMan_list[random_int]) #int means integer

def random_word():
    return hMan[random_int]

def underscore_string():
    under_string = "_ " * len(random_word())
    return under_string

def main():
    tries = 0
    underscore_string = 0
    print(underscore_string)
    letter = input("Guess a letter: ")

    while tries < 7: # will use many many many while flags (if this then that) before stop        
        tries += 1
    while (tries != tries and random_int):
        if len(letter) == 1 :
            if letter in tries:
                first_index = letter
            elif first_index == -1:
                tries += 1
                print("wrong")
            else:
                print('right!')
            while tries == tries - 1 :
                print ('Total attempts: ', tries)
                if tries >= 8:
                    print("To the gallows with you!") #The mystery word was" (random_word)

    
    def guess_letter():
        letter = input("guess the mystery word; enter a letter: ")
        letter.strip()
        letter.lower()
        print (letter)
        return letter

    def play():
        answer = input("Would you like to play a game? y/n: ")
        if answer == 'y':
            print('get ready to hang')
            return answer
        else:
            print ("The gallows await your next visit")        
    return play()


main()