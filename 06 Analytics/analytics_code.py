# ========================
# ГЕНЕРАТОРЫ и yield
# ========================
# генераторы позволяют создавать простые последовательности максимально простым кодом
# разница в том, что мы можем на каждой итерации цикла вернуть значение наружу, не останавливая цикл. а вот с return так не выйдет
# исключения здесь тоже не используются
def create_range(start, end, step=1):
    while start < end:
        yield start
        start += step

print(create_range(1, 4, 1))

for i in create_range(1, 4):
	print("yield:", i)

my_range = range(1, 4, 1)
print(my_range)
print(list(my_range))

# list comprehension - цикл без цикла
my_list = [x for x in range(1, 4, 1)]
print(my_list)


# сложная структура пользователь -> посещенные локации
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def geoid(geoids):
	values = geoids.values() #[[213, 213, 213, 15, 213], [54, 54, 119, 119, 119], [213, 98, 98, 35]]
	for value in values: # на первом проходе будет [213, 213, 213, 15, 213]
		for el in value: # на первом проходе yield отдает 213, 213 и так далее
			yield el

# все значения выведутся в столбик
for id in geoid(ids):
	print(id)

# плоское представление - всего лишь конвертируем результат в list
ids_list = list(geoid(ids))
print(ids_list)

#генераторы и list comprehension
# стандартный алгоритм фильтрации целых чисел - мы все сделали вручную
test_list = list(range(10))
def create_filter(some_list):
	for el in some_list:
		if el % 2 == 0:
			yield el

print("yield с фильтром: ", list(create_filter(test_list)))

# list comprehension
# все то же самое, только код намного короче. 
# на самом деле внутри тоже зашит for...
my_list = [x for x in range(10) if x%2==0]
print(my_list)

# ========================
# ФУНКЦИЯ map
# ========================
print("Функция map")

def add_fn(*args):
	sum = 0
	for arg in args:
		sum += arg
	return sum

x = map(add_fn, [1, 2], [3, 4], [5, 6])
print(list(x))

# def add_fn(*args):
# 	sum = 0
# 	for arg in args:
# 		sum += arg
# 		print(arg)
# 	print(f"sum={sum}")
	# return sum

# функция 'plus' применяется к элементам 
# из всех последовательностей параллельно
# x = map(add_fn, [1, 2], [3, 4], [5, 6])
# print(list(x))

# вспомним странный пример про создание словаря из кортежей
def create_tuple(a, b):
    return a, b

# map заканчивает работу по самой короткой последовательности -
# так же, как это делает zip
x = map(create_tuple, ['a', 'b'], [3, 4, 5])
print(f"Создадим словарь из кортежей при помощи map:\n{dict(x)}")


# Можно также использовать любую встроенную функцию с функцией map() при условии, что функция принимает аргумент и возвращает значение
x = [1, 3, 5]
y = [3, 3, 3]
# вычисление при помощи встроенной функции 'pow()' 
# 'x' в степени 'y' для каждого элемента 2-х списков
print("Возведение в степень")
print(list(map(pow, x, y)))

# подсчет количества символов в строке
x = map(len, ("mavic 2 pro", "phantom 4", "mini 3 pro"))
print(f"Подсчитаем длины строк: {list(x)}")

# как очистить слова от мусора после разбивки текста
import re

text = "Так как функция map() написана на языке C и хорошо оптимизирована, ее внутренний цикл более эффективный, чем обычный цикл for в Python"

def clean_text(word):
	# print(word)
	res = re.sub(r"[^\w]", "", word)
	return res

words = text.split()
# print(words)
words_list = map(clean_text, words)
print(f"Выведем почищенный текст:\n{' '.join(words_list)}")

# ========================
# ФУНКЦИЯ filter
# ========================
print("Функция filter")
numbers = list(range(10))
even_list = list(filter(lambda x: x%2 == 0, numbers))
print(f"Все четные: {even_list}")

def filter_odd(x):
	if x%2 != 0:
		return x
odd_list = list(filter(filter_odd, numbers))
print(f"Все нечетные: {odd_list}")

# ========================
# ФУНКЦИЯ sum
# ========================
print("Функция sum")
# простое суммирование
numbers = list(range(10))
numbers.append(4.5)
numbers.append(8+8j)
result = sum(numbers)
print(f"Суммирование: {type(result)}, {result}")

# матрица в список
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
result = sum(matrix, [])
print(f"Объединение матрицы в список: {result}")

# расчет скалярного произведения векторов
x_vector = (1, 2, 3)
y_vector = (4, 5, 6)
#  1 × 4 + 2 × 5 + 3 × 6 = 32
result = sum(x * y for x, y in zip(x_vector, y_vector))
print(f"Скалярное произведение векторов:{result}")


# ========================
# ЛАМБДА-ФУНКЦИИ
# ========================
print("\nЛАМБДА-ФУНКЦИИ")

name_list = ["mavic 2 pro", "phantom 4", "mini 3 pro"]
name_list.sort()
print("Стандартная сортировка (по кодам букв)")
print(name_list)

# тем не менее, можно изменить поведение функции list.sort, написав собственную функцию сортировки:
# кастомная функция сортировки. Возвращает длину слова, которую и использует list.sort
def sort_by_len(word):
	return len(word)

# по возрастанию длины
name_list = ["mavic 2 pro", "phantom 4", "mini 3 pro"]
name_list.sort(key=sort_by_len)
print("Сортировка функцией по длине фразы")
print(name_list)

# того же самого результата можно добиться, не загромождая свой код простыми маленькими функциями
# lambda-функция - это функция, которая а) не имеет имени, б) создается непосредственно в месте использования и сразу уничтожается, в) записывается в одну строку, г) всегда возвращает значение, но без ключевого слова return

# реализация кастомной сортировки того же списка при помощи lambda-фукции
name_list = ["mavic 2 pro", "phantom 4", "mini 3 pro"]
name_list.sort(key=lambda x: len(x))
print("Сортировка ламбда-функцией по длине фразы")
print(name_list)

# запись lambda x: len(x) эквивалентна
# def sort_by_len(word):
# 	return len(word)

# lambda-функцию можно присвоить переменной и тогда она не удалится. хотя все равно останется безымянной
print("lambda-функцию можно присвоить переменной")
sort_by_len = lambda x: len(x)
name_list = ["mavic 2 pro", "phantom 4", "mini 3 pro"]
name_list.sort(key=sort_by_len)
print(name_list)

# функцию можно удалить так же, как любой другой объект:
del sort_by_len

# осторожно - здесь сгенерируется исключение
# name_list.sort(key=sort_by_len)
# print(name_list)

# ========================
# ПРИМЕРЫ на ЛАМБДА-ФУНКЦИИ, MAP, FILTER
# ========================
numbers = list(range(0, 10))

# пример отбора четных чисел из списка функцией filter:
even_list = list(filter(lambda x: x%2 == 0, numbers))
print(f"Отбор четных - filter: {even_list}")

# lambda-функцию можно запустить сразу в месте объявления. Передача параметра будет выглядеть так (проверка числа на четность):
print("Проверка числа на четность - ламбда") 
print((lambda x: x%2 == 0)(2))

# пример вычисления над каждым элементом списка. вычисление квадратов чисел функцией map:
square_list = list(map(lambda x: x*x, numbers))
print(f"Вычислить квадраты чисел - ламбда и map: {square_list}")

# пример вычисления над каждым элементом списка. вычисление квадратов чисел функцией map с условием - обрабатываем только четные числа:
square_list = list(map(lambda x: x*x if x%2 == 0 else None, numbers))
# на месте нечетных чисел будет значение, задаваемое в условии else, т.к. функция map, в отличие от filter, не умеет пропускать значения
print(f"Вычислить квадраты только четных чисел - ламбда и map: {square_list}")

# пример совместного использования map и filter. результатом будут все четные числа, возведенные в квадрат
# filter поможет "вычистить" лишние None
square_list_filtered = list(filter(lambda x: x is not None, map(lambda x: x*x if x%2 == 0 else None, numbers)))
print(f"Вычислить квадраты только четных чисел - ламбда, map и filter:  {square_list_filtered}")
