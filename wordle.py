from termcolor import colored, cprint
import random

final_answer = {1:'', 2:'', 3:'', 4:'', 5:''}

word_bank = open('word_bank.py','r')
words = word_bank.read()
allowed_words = words.split('\n')

answer_bank = open('answer_bank.py', 'r')
answer = answer_bank.read()
answer = answer.split('\n')
answer = str.upper(random.choice(answer))
counter = 0

for letter in answer:
    counter += 1
    final_answer[counter] = letter

response = ''
turn = 1

print('WORDLE'.center(9))
#counters
answer_count = {}
for a in final_answer.values():
    answer_count.setdefault(a,0)
    answer_count[a] = answer_count[a] + 1
#convert user response to dict
while turn <= 6:
    current = {1:'', 2:'', 3:'', 4:'', 5:''}
    color = {1: '', 2: '', 3: '', 4: '', 5: ''}
    word_count = {}
    r_count = 0
    response = input()[:5]
    print ("\033[A                             \033[A")
    if response not in allowed_words or response == '':
        print ('', end = '')
        continue
    for r in response:
        r_count += 1
        current[r_count] = str.upper(r)
#compare current to answer
    for n, c in current.items():
        word_count.setdefault(c,0)
        word_count[c] = word_count[c] + 1
        if current[n] == final_answer[n]:
            color[n] = 'green'
            continue
        for x,a in final_answer.items():
            if word_count[c] <= answer_count[a]:
                if color[n] != '':
                    break
                elif c == a:
                    color[n] = 'yellow'
                    continue
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
print(answer)
print('Better luck next time!')
