# ДЕКОРАТОРЫ
# декоратор - это функции-обертки, которые позволяют сделать дополнение к уже существующей функции. Внимание: поведение самой функции вы изменить не сможете.
# но, например, сможете провести дальнейшую обработку результата, возвращаемого из функции, или добавить вывод информации для пользователя

# пример: пусть существует простая функция a_simple, которая умеет только возвращать строку, содержащую арифметическое выражение "1+1"
# считать она не может, поэтому создадим вторую функцию a_complex, которая способна вычислять выражение, которое возвращает a_simple
# как это работает: 1) в a_complex передается указатель на a_simple, 2) функция вычисляет значение и возвращает результат,
# 3) если бы мы остановились на 2), это был бы стандартный вызов функции. Но нам нужна функция-обертка, поэтому a_complex возвращает не результат расчета "1+1",
# а функцию, которая все это делает.
# Обратите внимание: т.к. в переменную decorator возвращается функция, ее тоже нужно вызвать (с круглыми скобками без параметров)

def decorator(fun):
	print("decorator")
	def wrapper():
		print("Работает функция wrapper")
		return eval(fun())
	return wrapper

def simple():
	print("Работает функция simple")
	return "1+1"

decor = decorator(simple)
print(decor())

# то же самое более простым способом: чтобы не писать двойной вызов функции - используется декоратор
# это название функции с @ спереди:
def decorator(fun):
	print("decorator")
	def wrapper():
		print("Работает функция wrapper")
		return eval(fun())
	return wrapper

@decorator
def simple():
	print("Работает функция simple с декоратором")
	return "1+1"

print(simple())

# ================
# пример с simple_fun, возвращающей "1+1", может показаться надуманным, однако именно так работают системы символьной математики, которые вычисляют ввод пользователя. Или, например, такое пригодится для вычисления Польской нотации https://ru.wikipedia.org/wiki/Польская_нотация
# ================

# декораторов может быть и больше одного к одной функции:
def decorator(fun):
	print("decorator")
	def wrapper():
		print("Работает функция wrapper")
		return eval(fun())
	return wrapper
	
def decorator2(fun):
	print("decorator2")
	def wrapper():
		print("Работает функция wrapper")
		return fun()
	return wrapper

# в этом случае они вызываются в порядке "кто ближе к функции": decorator -> decorator2 ->...
# или decorator2(decorator(simple))
@decorator2
@decorator
def simple():
	print("Работает функция simple с несколькими декораторами")
	return "1+1"

print(simple())

# ================
# если нужно декорировать функцию, которая принимает аргументы,
# то в фукнцию-обертку также передаются эти аргументы
def decorator_args(fun):
	print("decorator_args")
	def wrapper(arg):
		print(f"Входные аргументы: {arg}")
		print("Работает функция wrapper")
		return fun(arg)
	return wrapper

# здесь пример все так же для вычисления символьной математики
@decorator_args
def simple(args):
	print("Работает функция simple с аргументами")
	return eval(args)

print(simple("3+4"))

# пример декоратора для функции с множеством аргументов
def decorator2_args(fun):
	print("decorator2_args")
	def wrapper(*args):
		print(f"Входные аргументы: {args}")
		print("Работает функция wrapper")
		return fun(*args)
	return wrapper

# здесь уже стандартное вычисление суммы, без символьной математики и eval
@decorator2_args
def simple(*args):
	print("Работает функция simple с аргументами")
	return sum(args)

print(simple(1,2,3,4,5))

# ================
# декоратор для логирования вызова кода
import logging

def log(func):
	def wrap_log(*args, **kwargs):
		name = func.__name__
		logger = logging.getLogger(name)
		logger.setLevel(logging.DEBUG)
		
		fh = logging.FileHandler("%s.log" % name)
		fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
		formatter = logging.Formatter(fmt)
		fh.setFormatter(formatter)
		logger.addHandler(fh)
		
		logger.info("Вызов функции: %s" % name)
		# info("Вызов функции: %s" % name)
		result = func(*args, **kwargs)
		# logger.info("Результат: %s" % result)
		logger.info("Результат: %s" % result)
		return func

	return wrap_log

# обратите внимание: функция, декорированная логгером, ничего не пишет на экране! она пишет результат в лог-файл с именем, соответствующим имени функции
# поэтому ищите файл simple.log
@log
def simple(*args):
	print("Работает функция simple с логированием")
	return sum(args)

# print(simple(1,2,3,4,5))

# ================
# декоратор для оценки времени выполнения кода
from datetime import datetime
import time

def estimate_time(fun):
	def wrapper(*args):
		start = datetime.now()
		res = fun(*args)
		end = datetime.now()
		elapsed = (end - start).total_seconds() * 1000
		print(f'{fun.__name__} время выполнения (ms): {elapsed}')
		return res
		
	return wrapper

@estimate_time
def simple(*args):
	print("Работает функция simple с оценкой времени выполнения")
	return sum(args)

print(simple(1,2,3,4,5))

# ================
# декоратор для "обезопашивания" функций (перехватчик исключений)
def error_handler(fun):
	def wrapper(*args, **kwargs):
		res = 0
		try:
			res = fun(*args, **kwargs)
		except Exception as e:
			print(f"Ошибка {e} при вызове {fun.__name__}")
		return res
	return wrapper

# потенциально "опасная" функция
def not_safe(*args):
	if len(args) == 0:
		return 0
	print('Работает "опасная" функция not_safe')
	div_res = args[0]
	for arg in args:
		div_res/= arg
	return div_res

@error_handler
def simple(*args):
	print('Работает "безопасная" функция simple')
	return not_safe(*args)

print(simple(1,2,3,4,5))
print(simple(1,2,0,4,5))

# ================
# вызов функции с двумя декораторами: одновременно с перехватом исключений и оценкой длительности выполнения
@estimate_time
@error_handler
def simple(*args):
	print('Работает функция simple с двумя декораторами')
	return not_safe(*args)

print(simple(1,2,3,4,5))
print(simple(1,2,0,4,5))

# ================
# декоратор-класс. в этом случае в классе создается функция __call__
from datetime import datetime
class DecoratorArgs:
	def __init__(self, dec_name):
		print(f"Входные аргументы __init__: {dec_name}")
		
# метод-декоратор из класса. обратите внимание: аргументы идут напрямую в декоратор, а не в метод __init__ класса
	def __call__(self, fun):
		def wrapper(*args):
			print(f"Входные аргументы wrapper: {args}")
			start = datetime.now()
			res = fun(*args)
			end = datetime.now()
			elapsed = (end - start).total_seconds() * 1000
			print(f'{fun.__name__} время выполнения (ms): {elapsed}')
			return res
		return wrapper

@DecoratorArgs("класс-декоратор")
def simple(*args):
	print(f"Работает функция simple с оценкой времени выполнения")
	return sum(args)

print(simple(1,2,3,4,5))


# ================
# ДЕКОРАТОРЫ В КЛАССАХ
# "встроенные" декораторы: @classmethod, @staticmethod, @property
# до тех пор, пока вы не используете наследование, декораторы @classmethod и @staticmethod ведут себя одинаково: они делают так, что декорированную ими функцию можно вызывать как из экземпляра класса, так и статически из самого класса
# при наследовании @classmethod будет относиться к классу-наследнику, а @staticmethod - к базовому (родительскому) классу

class Aircraft:
	def __init__(self, model, weight):
		self.weight = weight
		self.model = model

	#  статический метод, "привязанный" к определению класса
	@staticmethod
	def get_spare(weight, model):
		return Aircraft(weight, model)

	#обычный метод класса, "привязанный" к экземпляру класса
	# @classmethod
	# def get_spare(self, weight, model):
	# 	return self(weight, model)

# класс-наследник. если оставить статический get_spare, он будет возвращать объект класса Aircraft
# если объявить get_spare как @clssmethod, он будет возвращать объект класса Multirotor
class Multirotor(Aircraft):
	def __init__(self, model, weight, rotors=4):
		self.weight = weight
		self.model = model
		self.rotors = rotors	

# экземпляр класса Aircraft
print("===Работает экземпляр класса Aircraft===")
aircraft1 = Aircraft("DJI Mavic 2 Pro", 907)
spare = aircraft1.get_spare("DJI Mavic 2 Pro", 907)
print(type(spare))
# экземпляр класса Multirotor
print("===Работает экземпляр класса Multirotor===")
aircraft2 = Multirotor("DJI Mavic 2 Pro", 907, 4)
spare = aircraft2.get_spare("DJI Mavic 2 Pro", 907)
print(type(spare))

# объявление свойств в классах Python
class Aircraft:
	def __init__(self, model, weight):
		self.__weight = weight
		self.__model = model
		self.__regnum = ""

	@property
	def regnum(self):
		return self.__regnum

	@regnum.setter
	def regnum(self, num):
		self.__regnum = num

	# @staticmethod
	# def get_spare(weight, model):
	# 	return Aircraft(weight, model)

	@classmethod
	def get_spare(self, weight, model):
		return self(weight, model)

print("===Работает экземпляр класса Aircraft===")
aircraft1 = Aircraft("DJI Mavic 2 Pro", 907)
print(aircraft1.regnum)
aircraft1.regnum = "a0rdk9s"
print(aircraft1.regnum)
