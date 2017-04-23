#!/usr/bin/python
# -*- coding: utf-8 -*-

# Global Declaration is done in order to ensure that the code works properly

blanks = ['_1_', '_2_', '_3_', '_4_']

# Declaring of the question
# easy question list

easy_ques = \
    '''_1_ stands for hyper-text markup language.
 _2_ stands for cascadind sytle sheets.
 _3_ language uses .py extension.
_4_ language use .cpp extension.
'''

# medium question list

medium_ques = \
    '''Earth is protected from Ultra voilet radiation by _1_.
 Solid carbon dioxide is known as _2_.
Shora is the parliament of _3_.
  Wular Lake is in _4_.
 '''

# hard question list

hard_ques = \
    '''The Battle of Plassey was fought in _1_.
 Tripitakas are sacred books of _2_.
 Todar Mal was associated with _3_.
 The language of discourses of Gautama Buddha was _4_'''

# Answers are declared
# easy answer list

easy_answers = ['HTML', 'CSS', 'PYTHON', 'C++']

# med answer list

medium_answers = ['OZONE', 'DRY ICE', 'AFGHANISTAN', 'JAMMU AND KASHMIR']

# hard answer list

hard_answers = ['1757', 'BUDDHISTS', 'FINANCE', 'PALI']


# Answer check function
# takes 3 arguments and check ans is correct or not
# replaces the string with ans and count the score

def answer_check(level, question_paragraph, answer):
    index_number = 0
    count = 0
    max_index = 3
    for blank in blanks:
        question = 'Enter your answer for ' + blank + ' '  # user is asked to enter the answer for the blank
        print question  # question is displayed so that user can enter the answer
        get_input = raw_input('Enter the answer ').upper()
        while get_input != answer[index_number]:  # if the user enters wrong answer he is prompted to enter it again and if it is correct it is replaced
            print 'YOU GOT IT WRONG'  # alerting the user that you entered the wrong answer
            count = count - 1
            get_input = raw_input('Enter Once Again ').upper()
        print 'Correct'
        count = count + 1
        question_paragraph = question_paragraph.replace(blanks[index_number], get_input)
        print question_paragraph
        index_number += 1  # index_number is incremented so that it can switch to next blank
        if index_number > max_index:
            return count


# defining the level choose function
# takes user input and checks the level and calls function for ans check

def level_choose():
    level = raw_input('''1.EASY   2.MEDIUM    3.HARD   ''')  # inputting the level
    if level.upper() in ['1','2','3','EASY','MEDIUM','HARD',]:
        (question_paragraph, answers) = level_select(level)
        print question_paragraph
        score = answer_check(level, question_paragraph, answers)

        # user choice whether he wants to continue or quit the gaame
        # if yes then again function call
        # if no then it print score and exit

        choice = raw_input('You DID IT \nDo you want to play again? Yes/No').lower()
        if choice == 'yes':
            print 'your result for previous game\n'
            result(score)
            level_choose()
        else:
            print 'Thanks for playing the game'
            result(score)
            exit(0)
    else:
        print 'Choose appropriate level\n'
        level_choose()


# define /print score and takes 1 argument

def result(score):
    print 'your total score'
    print score


# User chooses the level
# takes 1 argument and conditions are checked and return values regarding to there level

def level_select(level):
    if level == 'EASY' or level == '1':
        print 'You choose the easy level\n'

        # returning is done here

        return (easy_ques, easy_answers)
    if level == 'MEDIUM' or level == '2':
        print 'You choose the Medium level\n'
        print 'good choice'
        return (medium_ques, medium_answers)
    else:
        print 'You Choose the Hard level\n'
        return (hard_ques, hard_answers)


# User enter the name
# takes / asks user for name and convert it to upper case letter using upper function

def user_info(player_name):
    print 'WELCOME ' + player_name.upper() + '. Lets complete the game'
    print 'Choose the following levels listed below: \n'


# some lines printed during the execution of prog

print 'Hello, Friends!'
print '\t\t\tWelcome to The Quiz - Python Edition\t\t'
print '\t\t\t.....................................\t\t'
print '\t\t\tWelcome to my first quiz'
print '\n'

# time is imported and is used for time wait bcoz when game starts it gets load

import time
print 'loading game....wait for sometime!!!'
time.sleep(1)
print '\t\t\tWelcome and just few Instructions to the game'
print '\t\t\tJust answer my questions in capital Letters only'
print '\t\t\tRules for the quiz'
print '\t\t\t1.Give answer in capital letters only\n'
print '\t\t\t2.For every correct answer 1 credit is given and for any wrong answer 1 credit will be deducted\n'

# asks for user name and continue with that name

player_name = raw_input('Enter your name ')  # asking the name of the user
user_info(player_name)

# level function call which level u want to select

level_choose()


			
