
from termcolor import colored, cprint
import random

word_bank = open('word_bank.py','r')
words = word_bank.read()
allowed_words = words.split('\n')

answer = {1:'S', 2:'I', 3:'M', 4:'O', 5:'N'}
current = {1:'_', 2:'_', 3:'_', 4:'_', 5:'_'}
color = {1: '', 2: '', 3: '', 4: '', 5: ''}

response = ''
turn = 1

print('WORDLE'.center(9))
#convert user response to dict
while turn <= 6:
    r_count = 0
    response = input()[:5]
    print ("\033[A                             \033[A")
    if response not in allowed_words:
        print ('', end = '')
        continue
    for r in response:
        r_count += 1
        current[r_count] = str.upper(r)
#compare current to answer
    for n, c in current.items():
        for x,a in answer.items():
            if c == answer[x] and n == x:
                color[n] = 'green'
                break
            elif c == answer[x] and n != x:
                color[n] = 'yellow'
                break
            else:
                color[n] = ''
#display answer
    for k,c in color.items():
        if c == 'yellow' or c == 'green':
            cprint(current[k], 'grey', 'on_' + str(color[k]), end = ' ')
        else:
            print(current[k], end = ' ')
    print('')
#game resutls
    if color[1] == color[2] == color [3] == color[4] == color[5] == 'green':
        print('Congratulations, you guessed the word!')
        exit()
    else:
        turn += 1
print('Better luck next time!')
exit()
