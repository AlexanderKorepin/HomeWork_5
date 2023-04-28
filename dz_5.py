# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
import random
def zadacha_1():
    number = random.randint(1, 10)
    n = [random.randint(1, 10) for n in range(10)]
    print(n)
    n = list(filter(lambda x: x > 5, n))
    print(n)
zadacha_1()    
#-----------------------------------------------
# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.
def zadacha_2():
  list = [1, 5, 2, 3, 4, 6, 1, 7]
  result_list = []
  count = 0
  for i in range(0, len(list)-1):
      temp_list = [list[i]]
      for j in range(i+1, len(list)):
          if list[j] > temp_list[-1]:
              temp_list.append(list[j])
              count += 1
      result_list.append(temp_list)
  print(result_list)
#-------------------------------------------------------
# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают. Список уникальных элементов
# [1, 4, 2, 3, 6, 7]
import random
def zadacha_3():
    numbers = [random.randint(1, 10) for _ in range(10)]
    print(numbers)    
    single = list(set(numbers))
    repeat_sum = 0
    len_unique = len(single)   
    for i in range(len_unique):
        repeat = 0
        repeat = numbers.count(single[i]) 
        if repeat > 1:
            repeat_sum += repeat      
    print(f'{repeat_sum} элементов совпадают')
    print(f'Список уникальных элементов: ', single)
