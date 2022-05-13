'''Игра Угадай число'''
import numpy as np

number = np.random.randint(1, 101) #загадываем число

count = 0
while True:
    count += 1
    predict_number = int(input('Угдай число от 1 до 100 '))
    if predict_number > number:
        print("Число должно быть менешье!")
    elif predict_number < number:
        print("Число должго быть больше!")
    else:
        print(f'Вы угадали число! это число = {number}, за {count} попыток')
        break