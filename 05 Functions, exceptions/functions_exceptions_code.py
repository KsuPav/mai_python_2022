# вызов справки по функции
print("===============\nhelp() и docstring\n===============")
# help(print)

# docstring - документация к функции
def my_func(num):
	'''Функция my_func. Принимает число num и возвращает его же'''
	return num
print(my_func(4))
help(my_func)


print("===============\nФункции и аргументы\n===============")
# функция с одним аргументом и возвратом результата
def my_func(num):
	return num
print(my_func(4))

# функция с одним аргументом без возврата результата (вернет None)
def my_func(num):
	pass
print(my_func(4))

# функция с аргументом по умолчанию
def my_func(num, mul=2):
	print(num, mul)
	print(num * mul)

my_func(4)
my_func(4,3)

# функция с переменным количеством аргументов
def my_func(*args):
	print(type(args))
	for arg in args:
		print(arg)
	print(args[0] * args[1])

my_func(4, 2)

# функция с переменным количеством именованных аргументов
def my_func(**kwargs):
	print(type(kwargs))
	for k,v in kwargs.items():
		print(k, v)
	print(kwargs["num"]*kwargs["mul"])

my_func(num=4, mul=2)

print("===============\nОбласти видимости функции\n===============")
salary = 500
bonus = 500
onetime_bonus = 300
print(f"Начальные salary={salary}, bonus={bonus}, onetime_bonus={onetime_bonus}")
def pay():
	print(f"pay - внешние salary({salary}) + bonus({bonus}):",salary + bonus)
pay()

def pay2():
	bonus = 1000
	print(f"pay2 - внеш. salary({salary}) + внутр. bonus({bonus}):",salary + bonus)
pay2()

def pay3():
	salary = 1200
	bonus = 1000
	print("pay3 - внутр. salary({salary}) + bonus({bonus}):",salary + bonus)
pay3()

print("===============\nglobal\n===============")
def pay4g():
	global onetime_bonus
	onetime_bonus = 700
	print(f"pay4g - внешние salary({salary}) + bonus({bonus}) + global onetime_bonus({onetime_bonus}): {salary + bonus + onetime_bonus}")

print(f"До вызова pay4g onetime_bonus={onetime_bonus}")
pay4g()
print(f"После вызова pay4g onetime_bonus={onetime_bonus}")

print("===============\nnonlocal\n===============")
print("И создание функции внутри функции")
onetime_bonus = 300
is_heroic = True
def pay5nl():
	onetime_bonus = 0
	def heroic():
		if is_heroic:
			nonlocal onetime_bonus
			onetime_bonus = 700
	heroic()
	print(f"pay5nl - внешние salary({salary}) + bonus({bonus}) + nonlocal onetime_bonus({onetime_bonus}): {salary + bonus + onetime_bonus}")

print(f"До вызова pay5nl onetime_bonus={onetime_bonus}")
pay5nl()
print(f"После вызова pay5nl onetime_bonus={onetime_bonus}")


print("\n===============\nИсключения\n===============")

budget = 1000
def pay_ex():
	dangerous_coeff = 0
	return budget/dangerous_coeff
# print(pay_ex())
	
try:
	pay_ex()
	print("Вызвали pay_ex")
except Exception as e:
	print(e)
finally:
	print("Всегда будет работать")

# raise ZeroDivisionError

try:
	raise ZeroDivisionError
except:
	print("Поймали исключение")

assert 5 in [1, 2, 3, 4]

try:
	assert 5 in [1, 2, 3, 4]
except:
	print("Поймали исключение")
