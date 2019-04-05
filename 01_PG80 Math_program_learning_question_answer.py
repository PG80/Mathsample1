# PG80 Math App

# levels
# Beginner_jump
# Easy_jump
# Standart_jump
# Hardcore_jump
# Professional_jump
from PG80_Math_program_Data_info import Beginner_jump, Easy_jump, Standart_jump, Hardcore_jump, Professional_jump

class basic_logic_for_first_app:

    def __init__(self, serial_number, number01, sign, number02, equals_sign, answer):
        self.serial_number = serial_number
        self.number01 = number01
        self.sign = sign
        self.number02 = number02
        self.equals_sign = equals_sign
        self.answer = answer

    def check_answer(self, try_answer):
        return try_answer == self.answer


Beginner_jump_for_use = Beginner_jump
Easy_jump_for_use = Easy_jump
Standart_jump_for_use = Standart_jump
Hardcore_jump_for_use = Hardcore_jump
Professional_jump_for_use = Professional_jump

question_list = []

for serial_number, number01, sign, number02, equals_sign, answer in Beginner_jump_for_use:
    print('Solve example:')
    print(number01, sign, number02, equals_sign, answer)
    current_question = basic_logic_for_first_app(serial_number, number01, sign, number02, equals_sign, answer)
    question_list.append(current_question)


    if current_question.check_answer(input('What answer?')):
        print('Good job')

    elif current_question.check_answer(input('Try, one more')):
        print('Excellent, Street forward!')

    elif current_question.check_answer(input('Try, last time')):
        print('Good job, Street ahead!')

    else:
        print(number01, sign, number02, equals_sign, answer)



for serial_number, number01, sign, number02, equals_sign, answer in Easy_jump_for_use:
    print(number01, sign, number02, equals_sign, answer)
    current_question = basic_logic_for_first_app(serial_number, number01, sign, number02, equals_sign, answer)
    question_list.append(current_question)
    while not current_question.check_answer(input('Enter answer, please')):
        print('This is not correct answer, try one more')


for serial_number, number01, sign, number02, equals_sign, answer in Standart_jump_for_use:
    print(number01, sign, number02, equals_sign, answer)
    current_question = basic_logic_for_first_app(serial_number, number01, sign, number02, equals_sign, answer)
    question_list.append(current_question)
    while not current_question.check_answer(input('Enter answer, please')):
        print('This is not correct answer, try one more')


for serial_number, number01, sign, number02, equals_sign, answer in Hardcore_jump_for_use:
    print(number01, sign, number02, equals_sign, answer)
    current_question = basic_logic_for_first_app(serial_number, number01, sign, number02, equals_sign, answer)
    question_list.append(current_question)
    while not current_question.check_answer(input('Enter answer, please')):
        print('This is not correct answer, try one more')


for serial_number, number01, sign, number02, equals_sign, answer in Professional_jump_for_use:
    print(number01, sign, number02, equals_sign, answer)
    current_question = basic_logic_for_first_app(serial_number, number01, sign, number02, equals_sign, answer)
    question_list.append(current_question)
    while not current_question.check_answer(input('Enter answer, please')):
        print('This is not correct answer, try one more')


