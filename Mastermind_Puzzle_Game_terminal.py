import random
cracked = 'no'
#attempt the code and raise the number of attempts
code = str(random.randint(100,999))
attempts = 0
#print(code)

while cracked == 'no':


    correct_placement = 0
    correct_number = 0

    code_attempt = input('Guess the three digit code: ')
    attempts += 1
    temp_code_attempt = list(code_attempt)
    first_digit = 'not checked'
    second_digit = 'not checked'
    third_digit = 'not checked'

    
    if code_attempt == code:
        print("\nYou've cracked the code! C O N G R A T U L A T I O N S ! You cracked the code in {} attempts!".format(attempts))
        cracked = 'yes'
    
    else:

#Find out how many numbers are correct and in the correct place
#When a number is fully correct, it also puts a 'check' where it is in the temp code, so that it won't be recounted in the existance check

#FIRST digit test   
     
        if code[0] == code_attempt[0]:
            correct_placement += 1
            first_digit = 'check'
            temp_code_attempt[0] = 'check'

#SECOND digit test 
        
        if code[1] == code_attempt[1]:
            correct_placement += 1
            second_digit = 'check'
            temp_code_attempt[1] = 'check'
 
#THIRD digit test
        
        if code[2] == code_attempt[2]:
            correct_placement += 1
            third_digit = 'check'
            temp_code_attempt[2] = 'check'


# # # Existance check! # # # 
    
        #first check
        if first_digit != 'check':
            if code[0] == temp_code_attempt[0]:
                correct_number += 1
                temp_code_attempt[0] = 'check'

            if code[0] == temp_code_attempt[1]:
                correct_number += 1
                temp_code_attempt[1] = 'check'

            if code[0] == temp_code_attempt[2]:
                correct_number += 1
                temp_code_attempt[2] = 'check'

        #second check
        if second_digit != 'check':
            if code[1] == temp_code_attempt[0]:
                correct_number += 1
                temp_code_attempt[0] = 'check'

            if code[1] == temp_code_attempt[1]:
                correct_number += 1
                temp_code_attempt[1] = 'check'

            if code[1] == temp_code_attempt[2]:
                correct_number += 1
                temp_code_attempt[2] = 'check'

        #third check
        if third_digit != 'check':
            if code[2] == temp_code_attempt[0]:
                correct_number += 1
                temp_code_attempt[0] = 'check'

            if code[2] == temp_code_attempt[1]:
                correct_number += 1
                temp_code_attempt[1] = 'check'

            if code[2] == temp_code_attempt[2]:
                correct_number += 1
                temp_code_attempt[2] = 'check'

#Finally show how many are correct and in the right place, then reset those values

        print('''Correct number: {}
Correct number and placement: {}\n'''.format(correct_number,correct_placement))

        correct_number = 0
        correct_placement = 0
