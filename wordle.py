from termcolor import colored, cprint
import random

word_bank = open('word_bank.py','r')
words = word_bank.read()
allowed_words = words.split('\n')

answer = {1:'S', 2:'S', 3:'S', 4:'O', 5:'N'}
current = {1:'_', 2:'_', 3:'_', 4:'_', 5:'_'}

response = ''
turn = 1

print('WORDLE'.center(9))
#counters
answer_count = {}
for a in answer.values():
    answer_count.setdefault(a,0)
    answer_count[a] = answer_count[a] + 1
#convert user response to dict
while turn <= 6:
    color = {1: '', 2: '', 3: '', 4: '', 5: ''}
    word_count = {}
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
        word_count.setdefault(c,0)
        word_count[c] = word_count[c] + 1
        if current[n] == answer[n]:
            color[n] = 'green'
            continue
        for x,a in answer.items():
            if word_count[c] <= answer_count[a]:
                if c == a:
                    color[n] = 'yellow'
                    continue
                elif color[n] != '':
                    break
            elif color[n] != '':
                break
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
