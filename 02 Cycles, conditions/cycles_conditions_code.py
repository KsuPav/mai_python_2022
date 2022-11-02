weight = 30_001
if weight <= 150:
	print("Не нужно регистрировать")
elif weight <= 30_000:
	print("Нужно регистрировать")
else:
	print("Нужно регистрировать со специальными условиями")

# по правилам Росавиации не нужно согласовывать полет, если 1) он в прямой видимости, 2) на высоте не более 150 м, 3) выполняется вне закрытых зон. Проверяем, нужно ли нам согласование?
# vlos = visual line of site, прямая видимость
vlos = True 
height = 151
closed_area = True
if vlos and height <=150 and not closed_area:
	print("Не нужно согласовывать, летайте спокойно!")
# else:
# 	print(f"Нужно согласовывать, т.к. минимум одно условие требует согласования")
else:
	conditions = ""
	if not vlos:
		conditions += "/полет вне зоны прямой видимости/"
	if height > 150:
		conditions += "/высота полета более 150 м/"
	if closed_area:
		conditions += "/полет в закрытой зоне/"
	print(f"Нужно согласовывать, т.к. {conditions}")

weights = [149, 9000, 151, 31000, 150]
no_perm = 0
locality = False
vlos = True
height = 120
reg_count = 0

for weight in weights:
	if weight <= 150:
		no_perm = no_perm + 145
	elif weight <= 30_000 and not locality and vlos and height<150:
		no_perm = no_perm + 1
		reg_count = reg_count + 1
	else:
		reg_count = reg_count + 1
		
print(f"Могут летать без согласования {no_perm} БВС, нужно \
регистрировать {reg_count} БВС")

for weight in weights:
	reg_count = reg_count+1 if weight > 150 else reg_count
	no_perm = (no_perm+1 if weight <= 150 else no_perm+1 if (weight <= 30_000 and not locality and  vlos and height<150) else no_perm)

print(f"Могут летать без согласования {no_perm} БВС, не нужно \
регистрировать {reg_count} БВС")

stop = False
while not stop:
	user_input = input("Введите массу БВС в граммах или q, чтобы выйти\n")
	if user_input.lower() == "q":
		stop = True
	else:
		# if isinstance(user_input, int):
		if user_input.isdigit():
			weight = int(user_input)
			if weight <= 150:
				print(f"БВС массой {weight} г. Не нужно регистрировать")
			else:
				print(f"БВС массой {weight} г. Нужно регистрировать")
		else:
			print("Вы ввели не число")

weights = [149, 9000, 151]
for id, weight in enumerate(weights):
	print(f"Проход цикла {id}")
	if weight <= 150:
			print(f"БВС массой {weight} г. Не нужно регистрировать")
	else:
		print(f"БВС массой {weight} г. Нужно регистрировать")


weights = [149, "9000", 151, 10000]
for id, weight in enumerate(weights[::-1]):
	if not isinstance(weight, int):
		continue
	print(f"Проход цикла {id}")
	if weight <= 150:
			print(f"БВС массой {weight} г. Не нужно регистрировать")
	else:
		print(f"БВС массой {weight} г. Нужно регистрировать")
