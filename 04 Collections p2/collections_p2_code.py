# my_dict = {("Иванов", "Павел", "Андреевич"):
# 	{"passport":"1111 101202", "date_of_birth":"01.01.1980", "address":"11402, г. Москва, ул. Кетчерская, д.16"},
# 	("Никитина", "Елена","Геннадьевна"):{},
# 	("Никитина", "Елена","Евгеньевна"):{"passport":"1112 111222"}}

# find_people = [("Никитина", "Елена","Евгеньевна"), ("Петров","Олег","Евгеньевич")]
# for p in find_people:
# 	print(my_dict.get(p))



# my_dict = {"brand":"DJI","name":"Mavic 2 Pro","weight":907, "prices":None}
# print(my_dict["weight"])
# uavs_list = [{"brand":"DJI","name":"Mavic 2 Pro","weight":907},
# 						{"brand":"DJI","name":"Mavic 2 Zoom","weight":905},
# 						{"brand":"Eachine","name":"Trashcan","weight":100}]
# for uav in uavs_list:
# 	print(f'{uav["brand"]}, {uav["name"]}')

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print()
# print(my_dict["brand"])
# try:
# 	print(my_dict["price"])
# except:
# 	print("Нет такого ключа")

# print(my_dict.get("name"))

# if "price" in my_dict.keys():
# 	print(my_dict["price"])
# else:
# 	print(None)

# test_dict = dict.fromkeys(["brand", "name", "price", "weight"], "")
# print(test_dict)

# test_dict.setdefault("certs", [])
# print(test_dict)
# test_dict.setdefault("certs", ["ГОСТ"])

# if "certs" not in test_dict.keys():
# 	test_dict["certs"] = ["ГОСТ"]

# print(test_dict)

# for uav in uavs_list:
# 	uav.setdefault("certs", [])
# 	uav["certs"].append("ГОСТ")

# for uav in uavs_list:
# 	if "certs" not in uav.keys():
# 		uav["certs"] = []
# 	uav["certs"].append("ГОСТ")

# print(uavs_list)

# my_dict2 = my_dict.copy()
# # my_dict2 = my_dict
# print(id(my_dict2), id(my_dict))
# my_dict2["prices"] = [1000, 2000]
# print(my_dict2)
# print(my_dict)

# set1 = {"DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "Eachine Trashcan", "DJI Inspire 2"}
# set2 = {"DJI Mavic 2 Pro", "DJI Phantom 4", "DJI Inspire 1"}
# set3 = {"DJI Matrice 300", "DJI Mavic 2 Pro"}

list1 = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "Eachine Trashcan", "DJI Inspire 2"]
list2 = ["DJI Mavic 2 Pro", "DJI Phantom 4", "DJI Inspire 1"]
list3 = ["DJI Matrice 300", "DJI Mavic 2 Pro"]

intersect_set = set(list1) & set(list2) & set(list3)
intersect_set = set(list1).intersection(set(list2), set(list3))
# print(intersect_set)

union_set = set(list1) | set(list2) | set(list3)
print(union_set)
print(len(union_set))
union_list = list1 + list2 + list3
print(union_list)
print(len(union_list))

res_list = []
for uav in union_list:
	if uav not in res_list:
		res_list.append(uav)
print(res_list)
print(len(res_list))

print("Разность множеств")
diff1 = set(list2) - set(list3)
diff2 = set(list3) - set(list2)
diff2 = set(list3).difference(list1, list2)
print(diff2)
print(diff1)
diff2 = set(list3) - set(list2) - set(list1)
print(diff2)

print("Симметрическая разность множеств")
diff1 = set(list2) ^ set(list3)
diff2 = set(list3) ^ set(list2)
diff2 = set(list3).symmetric_difference(set(list2))
print(diff1)
print(diff2)