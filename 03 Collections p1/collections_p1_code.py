l = [1,2,3]
l2 = [1, [2,3], 4]
print(len(l2))
print(l2[1][0])

l2.append(5)
l2.append([6, 7])
# l2.append(6,7)
# print(l2)
# l3 = l + l2
# print(l3)
# l.extend(l2)
# print(l)

l2.insert(0, 99)
print(l2)
try:
	l2.remove(999)
except Exception as e:
	print(e)
print(l2)

# print(l2.index([2, 3]))
l2.extend(l)
print(l2)
print(l2.count(1))

# l2.reverse()
# print(l2)
l3 = reversed(l2)
print(type(l3))
print(list(l3))

l3 = [1, 7, 0, 3.8]
l3.sort()
l3.sort(reverse=True)
print(l3)

l4 = l3.copy()
l4.remove(0)
print(l4)
print(l3)

l5 = list("Привет")
print(" ".join(l5))
l6 = ["Иванов", "Николай", "Яковлевич"]
print(" ".join(l6))

print(l3 * 3)

print(l2)
# print(l2[2])
# print(l2[2:3])
# print(l2[-2:-3:-1])
# print(l2[-3:])
print(l2[-2::-2])

print(range(10))
print(list(range(10)))

t = (1, 2, 3)
t2 = (4, 5)
print(t + t2)
print(t[2])
# t[2] = 0
t2 = list(t)
t2[2] = 0
print(t2)
t2 = tuple(t2)
print(type(t2))

names = ["Мария", "Петр", "Екатерина", "Елена"]
ages = [44, 23, 17]
gender = ["ж", "м", "ж", "ж"]
names_ages = zip(names, ages)
print(type(names_ages))
print(names_ages)
print(tuple(names_ages))

for n, a, g in zip(names, ages, gender):
	print(f"{n} {a} лет, пол {g}")

n1, n2, *ns = names
print(n1, n2, ns)