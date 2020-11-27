# def fun check_quess
def check_quess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 2:
        if guess.lower() == answer.lower():
            print('Correct answer!')
            score+=1
            still_guessing=False
        else:
            if attempt < 1:
                guess = input('Sorry wrong answer. Try again ')
            attempt = attempt + 1
    if attempt == 2:
        print('The correct answer is ' + answer)


score = 0
print ('world men\'s soccer Quiz')
print ('You have a 2 chances to quess')
# quess 1
guess1 = input('In which year was the first men\'s soccer world championship?\n \
A) 1930 B) 1938 C) 1944 D) 1950. Type A, B, C or D ')
check_quess(guess1, 'A')

# quess 2
guess2 = input('Which team was the first world champion in men\'s soccer?\n \
A) Italy B) Uruguay C) Germany D) France. Type A, B, C or D ')
check_quess(guess2, 'B')

# quess 3
guess3 = input('Which team was the second world champion in men\'s soccer?\n \
A) France B) Spain C) Italy D) Brazil. Type A, B, C or D ')
check_quess(guess3, 'C')

# quess 4
guess4 = input('When was the last soccer world cup?\n \
A) 2010 B) 2014 C) 2018 D) 2020. Type A, B, C or D ')
check_quess(guess4, 'C')

# quess 5
guess5 = input('Which team has played the most World Cup finals?\n \
A) Germany B) Brazil C) Chile D) Spain. Type A, B, C or D ')
check_quess(guess5, 'A')

# quess 6
guess6 = input('Which team has the most soccer world titles?\n \
A) Germany B) Uruguay C) Italy D) Brazil. Type A, B, C or D ')
check_quess(guess6, 'D')

# quess 7
guess7 = input('Who is the current world men\'s soccer champion?\n \
A) Germany B) Italy C) Croatia D) France. Type A, B, C or D ')
check_quess(guess7, 'D')

# quess 8
guess8 = input('In which year were the most goals scored in the final during regular playing time?\n \
A) 1954 B) 1958 C) 1962 D) 1966. Type A, B, C or D ')
check_quess(guess8, 'B')
print('Brazil won 5:2 against Sweden.')

# quess 9
guess9 = input('In which year were the most goals scored in the final after regular playing time?\n \
A) 1998 B) 2002 C) 2006 D) 2010. Type A, B, C or D ')
check_quess(guess9, 'C')
print('Italy won against France 5:3 after penalty.')

# quess 10
guess10 = input('Which European team has won the most titles in men\'s football?\n \
A) Germany B) Italy C) Spain D) England. Type A, B, C or D ')
check_quess(guess10, 'A')
print('Germany won 4 times world championship in men\'s soccer.')


print ('Your score is ' + str(score))
