'''Игра угадай число
Компьютер угадывает число сам!'''

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    mx = 101 # Максимально возможное было задано на 1 больше, для того
    # чтобы не ловить бесконечный цикл если загаданым числом будет 100
    
    mn = 0 # Аналогично для минимума.
    count = 0
    predict_number = np.random.randint(1, 101)
    
    while True:
        count += 1
        
        if number < predict_number: # Сравниваем загадное число 
            mx = predict_number # Задаем новый максимум
        elif number > predict_number:
            mn = predict_number # Задаем новый минимум 
        else:
            break
        
        predict_number = int((mn+mx) // 2) # Вычисляем среднее возмонжное число
    
    return (count)


print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов  
        угадывает наш алгоритм
    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: Среднее число попыток
    """
    count_ls =[] 
    np.random.seed(1) #Фиксируем сид 
    random_array = np.random.randint(1, 101, size=(10000)) # Загадываем 
    # 10000 раз число от 1 до 100  и заносим их в массив 
    
    for number in random_array:
        count_ls.append(random_predict(number)) 
    
    score = int(np.mean(count_ls)) #Вычисляем среднеий результат 
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

  
score_game(random_predict)