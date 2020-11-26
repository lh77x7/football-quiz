# def fun check_quess
def check_quess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer')
            score+=1
            still_guessing=False
        else:
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again ')
            attempt = attempt + 1
    if attempt == 3:
        print('The correct answer is ' + answer)


score = 0
print ('world men\'s soccer Quiz')
# quess 1
guess1 = input('In which year was the first men\'s soccer world championship? ')
check_quess(guess1, "1930")
# quess 2
guess2 = input('Which team was the first world champion in men\'s soccer? ')
check_quess(guess2, 'Uruguay')
# quess 3
guess3 = input('Which team was the second world champion in men\'s soccer? ')
check_quess(guess3, 'Italy')
# quess 4
guess4 = input('When was the last soccer world cup? ')
check_quess(guess4, '2018')
# quess 5
guess5 = input('Which team has played the most World Cup finals? ')
check_quess(guess5, 'Germany')
# quess 6
guess6 = input('Which team has the most soccer world titles? ')
check_quess(guess6, 'Brazil')
# quess 7
guess7 = input('Who is the current world men\'s soccer champion? ')
check_quess(guess7, 'France')
# quess 8
guess8 = input('In which year were the most goals scored in the final during regular playing time? ')
check_quess(guess8, '1958')
print('Brazil won 5:2 against Sweden.')
# quess 9
guess9 = input('In which year were the most goals scored in the final after regular playing time? ')
check_quess(guess9, '2006')
print('Italy won against France 5:3 after penalty.')
# quess 10
guess10 = input('Which European team has won the most titles in men\'s football? ')
check_quess(guess10, 'Germany')
print('Germany won 4 times world championship in men\'s soccer.')


print ('Your score is ' + str(score))
print ('If you score more than 9 points your knowlage about world men\'s soccer champion is really impressive!')
