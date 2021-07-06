def restart():
        import sys
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restarting now")
        import os
        os.execv(sys.executable, ['python'] + sys.argv)
        
def getmatch():
    import random
    num = random.randint(0,999)
    if num <= 9:
        return '00'+str(num)
    if num >= 10 and num <=99:
        return '0'+str(num)

    return str(num)

print("\nI am thinking of a 3-digit number. Try to guess what it is.\nHere are some clues:\nWhen I say:\tThat means:\n  Pico \t\tOne digit is correct but in the wrong position.\n  Fermi \tOne digit is correct and in the right position.\n  Bagels \tNo digit is correct.\nI have thought up a number.\nYou have 10 guesses to get it.")
match = getmatch()
guess_count=0

while True:
    print('Guess #{}'.format(guess_count+1))
    guess = input('> ')
    guess_count +=1
    
    if len(guess)>3 or not guess.isdecimal() or len(guess)<3:
            print('DO YOU NOT UNDERSTAND WHAT A 3 DIGIT NUMBER IS YOU FUCKING MORON?!')
            guess_count-=1
            continue
        
    if guess_count==10:
        print('You ran out of guesses :(\nThe number was {}'.format(match))
        while True:
            new_game = input('Do you want to play again?[y/n] >')
            if new_game=='y' or new_game=='Y':
                restart()
            if new_game=='n' or new_game=='N':
                print('Thanks for playing!')
                break
            else:
                print('Invalid input')
        break
    
    if guess == match:
        print('***Congratulations! You got it!***')
        while True:
            new_game = input('Do you want to play again?[y/n] >')
            if new_game=='y' or new_game=='Y':
                restart()
            if new_game=='n' or new_game=='N':
                print('Thanks for playing!')
                break
            else:
                print('Invalid input')
        break

    i=0
    fermi_flag=0
    for i in range(0,3):
        if guess[i]==match[i]:
            fermi_flag=1
            print('Fermi')

    j=0
    k=0
    pico_flag=0
    for j in range(0,3):
        for k in range(0,3):
            if j==k:
                continue
            if guess[j]==match[k]:
                pico_flag=1
                print('Pico')
                break
    if pico_flag==0 and fermi_flag==0:
        print('Bagels')
