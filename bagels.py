print("I am thinking of a 3-digit number. Try to guess what it is.\nHere are some clues:\nWhen I say:\tThat means:\n  Pico \t\tOne digit is correct but in the wrong position.\n  Fermi \tOne digit is correct and in the right position.\n  Bagels \tNo digit is correct.\nI have thought up a number.\nYou have 10 guesses to get it.")
match = '420'
guess_count=0
while True:
    print('Guess #',guess_count+1)
    guess = input()
    guess_count +=1
    if guess_count==10:
        print('You ran out of guesses')
        break
    
    if len(guess) > 3:
            print('DO YOU NOT UNDERSTAND WHAT A 3 DIGIT NUMBER IS YOU FUCKING MORON?!')
            guess_count-=1
            continue
            
    if guess == match:
        print('You got it!\nnow fuck off!')
        break

    i=0
    fermi_flag=0
    for i in range(0,3):
        if guess[i]==match[i]:
            fermi_flag=1
            print('Fermi')
            break

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

        
        
