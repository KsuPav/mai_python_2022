# ==================
# минимальная конструкция
# базовый класс для всех летательных аппаратов
# class Aircraft:
# 	weight = 0
# 	def __init__(self, w):
# 		weight = w

# здесь всегда weight = 0, потому что он статический
# aircraft1 = Aircraft(5000)
# aircraft2 = Aircraft(450)
# print(aircraft1.weight)
# print(aircraft2.weight)	

# здесь значение массы меняется, как и ожидалось. в каждом экземпляре - своя масса
# class Aircraft2:
# 	def __init__(self, w):
# 		self.weight = w

# aircraft1 = Aircraft2(5000)
# aircraft2 = Aircraft2(450)
# print(aircraft1.weight)
# print(aircraft2.weight)


# ==================
# НАСЛЕДОВАНИЕ ОТ ОДНОГО КЛАССА
# ==================
# минимальный пример наследования от базового класса Aircraft
class Aircraft:
	def __init__(self, model, weight):
		self.weight = weight
		self.model = model

	def takeoff(self):
		self.flight = True

	def landing(self):
		self.flight = False

# если мы не вызываем метод базового класса Aircraft, нам каждый раз придется вручную присваивать все те же параметры, которые уже умеет присваивать базовый класс:
class Multirotor(Aircraft):
	def __init__(self, model, weight):
		self.weight = weight
		self.model = model
		self.parachute = False
		self.can_hover = True
		
# упрощаем себе задачу ч.1: явно прописываем вызов __init__ базового класса
class Plane(Aircraft):
	def __init__(self, model, weight):
		Aircraft.__init__(self, model, weight)
		self.parachute = True
		self.can_hover = False

# теперь в классе Plane инициализация массы и модели происходит благодаря базовому классу
print("Инициализация явная, через родительский класс")
plane = Plane("Geoscan 201", 3000)
print(plane.model)
print(plane.weight)

# упрощаем себе задачу ч.2: вызываем инициализацию от основного родителя через super()
class Plane(Aircraft):
	def __init__(self, model, weight):
		super().__init__(model, weight)
		self.parachute = True
		self.can_hover = False

# теперь в классе Plane инициализация массы и модели происходит благодаря базовому классу
print("Инициализация через метод super()")
plane = Plane("Geoscan 201", 3000)
print(plane.model)
print(plane.weight)

# ==================
# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
# ==================
# сделаем самолет-беспилотник и квадрокоптер-беспилотник. для этого унаследуемся от двух классов: Aircraft (класс летательного аппарата) и UAV (автопилот). 
# У автопилота будет свойство "наличие автопилота" и способность планировать и сохранять полетные миссии
class UAV:
	def __init__(self):
		self.has_autopilot = True
		self.missions = []

# самолет-беспилотник - наследование сразу от двух классов.
# для самолета придется переопределить метод посадки (у самолета она сложная). для квадрокоптера можно либо вызвать метод родительского класса Aircraft, либо вообще не прописывать метод landing()
class PlaneUAV(Aircraft, UAV):
	def landing(self):
		if self.parachute:
			print("Парашют открыт")
		else:
			print("Посадка по-самолетному")
		super().landing()

class MultirotorUAV(Aircraft, UAV):
	# def landing(self):
	# 	super().landing()
	pass

print("Множественное наследование от Aircraft и UAV")
plane = PlaneUAV("Geoscan 201", 3000)
# два первых print отработают без проблем, т.к. сработает инициализация первого по порядку класса Aircraft
print(plane.model)
print(plane.weight)
# этот код вызовет исключение AttributeError, т.к. атрибуты еще не были созданы - инициализация второго и далее по порядку родительских классов автоматически не работает!
# print(plane.has_autopilot)
# print(plane.missions)

# модифицируем инициализацию PlaneUAV так, чтобы все работало:
class PlaneUAV(Aircraft, UAV):
	def __init__(self, model, weight):
		super().__init__(model, weight)
		UAV.__init__(self)
		
	def landing(self):
		if self.parachute:
			print("Парашют открыт")
		else:
			print("Посадка по-самолетному")
		super().landing()

# правильная инициализация при множественном наследовании:
print("Правильная инициализация при множественном наследовании")
plane = PlaneUAV("Geoscan 201", 3000)
print(plane.model)
print(plane.weight)
print(plane.has_autopilot)
print(plane.missions)
		
# посмотрим порядок поиска нужных методов по цепочке классов:
print("Порядок поиска методов в классах:")
print(PlaneUAV.mro())


# ==================
# ПЕРЕОПРЕДЕЛЕНИЕ БАЗОВЫХ МЕТОДОВ
# ==================
# переопределяем __str__
# переопределяем __gt__ - там нужен второй объект
class PlaneUAV(Aircraft, UAV):
	def __gt__(self, other):
		if not isinstance(other, Aircraft):
				return
		else:
			return self.weight > other.weight
			
	def __str__(self):
		return f"=== {self.model} ==="
	
	def __init__(self, model, weight):
		super().__init__(model, weight)
		UAV.__init__(self)
		
	def landing(self):
		if self.parachute:
			print("Парашют открыт")
		else:
			print("Посадка по-самолетному")
		super().landing()

plane = PlaneUAV("Geoscan 201", 3000)
print(plane)
print(plane.__str__())

plane2 = PlaneUAV("Geoscan 201 Геодезия", 3700)
print("Смотрим атрибут model, а потом - что выведет сам класс")
print(plane.model)
print(plane)

plane = PlaneUAV("Geoscan 201", 3000)
plane2 = PlaneUAV("Geoscan 201 Геодезия", 3700)
print("Сравним два объекта класса PlaneUAV - который из них тяжелее?")
print(f"{plane.model} тяжелее {plane2.model}" if plane > plane2 else f"{plane.model} легче {plane2.model}")

# ==================
# МОДИФИКАТОРЫ ДОСТУПА
# ==================
# переопределим массу летательного аппарата и параметры автопилота
class Aircraft:
	def __init__(self, model, weight):
		self.weight = weight
		self.model = model

	def takeoff(self):
		self.flight = True

	def landing(self):
		self.flight = False

class UAV:
	def __init__(self):
		self._has_autopilot = True
		self.__missions = []

class PlaneUAV(Aircraft, UAV):
	def landing(self):
		if self.parachute:
			print("Парашют открыт")
		else:
			print("Посадка по-самолетному")
		super().landing()
		
class PlaneUAV(Aircraft, UAV):
	def __init__(self, model, weight):
		super().__init__(model, weight)
		UAV.__init__(self)
		self.__missions = [(1,2), (3,4)]
		
	def __gt__(self, other):
		if not isinstance(other, Aircraft):
				return
		else:
			return self.weight > other.weight
			
	def __str__(self):
		return f"=== {self.model} ==="

	def landing(self):
		if self.parachute:
			print("Парашют открыт")
		else:
			print("Посадка по-самолетному")
		super().landing()

plane = PlaneUAV("Geoscan 201", 3000)
print(plane._UAV__missions)
print(plane._PlaneUAV__missions)
# print(plane.__missions)
print(dir(plane))
print(plane._has_autopilot)

# ==================
# ДОБАВЛЕНИЕ И УДАЛЕНИЕ ФУНКЦИЙ
# ==================
# объявляем функцию вне класса:
def need_reg(self):
		return "Нужно регистрировать" if self.weight > 150 else "Не нужно регистрировать"

# и присваиваем ее атрибуту внутри класса:
class PlaneUAV(Aircraft, UAV):
	puav_need_registration = need_reg
	
	def __init__(self, model, weight):
		super().__init__(model, weight)
		UAV.__init__(self)
		self.__missions = [(1,2), (3,4)]

plane = PlaneUAV("Geoscan 201", 3000)
print(dir(plane))
print(plane.puav_need_registration())

# удаляем функцию базового класса Aircraft при инициализации
class PlaneUAV(Aircraft, UAV):
	def __init__(self, model, weight):
		super().__init__(model, weight)
		UAV.__init__(self)
		self.parachute = True
		del Aircraft.landing
		
	def landing(self):
		if self.parachute:
			print("Парашют открыт")
		else:
			print("Посадка по-самолетному")
		super().landing()

plane = PlaneUAV("Geoscan 201", 3000)
print(dir(plane))
print(dir(Aircraft))
# теперь у нас будут проблемы с вызовом метода landing() из класса PlaneUAV, т.к. он внутри себя вызывал тот самый landing() из Airplane, который мы удалили
plane.landing()