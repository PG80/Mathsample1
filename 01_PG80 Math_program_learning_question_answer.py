# PG80 Math App

# levels
# Beginner_jump
# Easy_jump
# Standart_jump
# Hardcore_jump
# Professional_jump

import random

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
        first_is_correct_some_good_worlds = [
        'Unbelievable!',
        'Super!',
        'It’s impossible!',
        'It can’t be true!',
        'I can’t believe it!',
        'Incredible!',
        'I’m speechless!',
        'How amazing!',
        'I am astounded!',
        'I am shocked!',
        'That’s a good one!',
        'I can’t imagine you did that!',
        'I’ll believe it when pigs fly!',
        ]
        print(random.choice(first_is_correct_some_good_worlds))


    elif current_question.check_answer(input('Try, one more')):
        print('Excellent, Street forward!')

    elif current_question.check_answer(input('Try, last time')):
        print('Good job, Street ahead!')

    else:
        print(number01, sign, number02, equals_sign, answer)

        a = [
            'У тебя все получится!',
            'Ты на правильном пути!',
            'Не расстраивайся, все впереди!',
            'Посмотри внимательно на правильный ответ и продолжай!',
            'Запоминай выражения все отлично!',
        ]
        print(random.choice(a))




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


