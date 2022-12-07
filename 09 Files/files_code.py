# ====ТЕКСТОВЫЕ ФАЙЛЫ====
# источник данных для файла CSV - файл с записями о полетах дронов (согласованных) в г.Блумингтон
# исходные данные https://data.bloomington.in.gov/dataset/uav/resource/a7d8c9c4-13ca-4972-9b63-59b3a896c2da

# чтение текстового файла построчно. подходит для файлов очень большого размера, которые не умещаются целиком в память
# количество строк в файле придется считать вручную счетчиком
lines_count = 0
with open("files/uav.csv") as f:
	for line in f:
		print(line)
		lines_count += 1
print(f"Всего в файле {lines_count} строк")

# чтение текстового файла целиком. файл прочитается как единая текстовая строка
# на самом деле в исходном файле 1 строка = 1 запись, поэтому их можно разделить по символу переноса строки "\n"
with open("files/uav.csv", encoding="utf-8") as f:
	lines = f.read().split("\n")
print(f"Всего в файле {len(lines)} строк")
print(lines)

# чтение текстового файла целиком как списка строк
# отличие от предыдущего варианта - функция readlines() сама разбивает текст на строки
with open("files/uav.csv") as f:
	lines = f.readlines()
	for line in lines:
		print(line)
print(f"Всего в файле {len(lines)} строк")

# запись в текстовый файл. делается построчно функцией write()
with open("files/uav.txt", "w") as f:
	for line in lines:
		f.write(line)

# ====CSV====
import csv

# источник данных для файла CSV - файл с записями о полетах дронов (согласованных) в г.Блумингтон
# исходные данные https://data.bloomington.in.gov/dataset/uav/resource/a7d8c9c4-13ca-4972-9b63-59b3a896c2da

# при открытии файла лучше задавать параметр newline="", чтобы избежать появления пустых строк. особенно при записи файла

# чтение по одной записи в list
with open("files/uav.csv", newline="") as f:
	reader = csv.reader(f)
	for line in reader:
		print(line)

# чтение всех записей сразу в список списков [[], [], ...]
with open("files/uav.csv", newline="") as f:
	reader = csv.reader(f)
	lines_list = list(reader)
print(lines_list[:3])

# чтение по одной записи в dict
with open("files/uav.csv") as f:
	reader = csv.DictReader(f)
	for line in reader:
		print(line["Timestamp"], 
					line["Drone Make & Model:"])

# сохранение по одной записи (list) при помощи writerow
with open("files/uav2.csv", "w") as f:
	writer = csv.writer(f)
	for line in lines_list:
		writer.writerow(line)

# создание "диалекта" - набора настроек для открытия или сохранения csv с выбранным разделителем значений и настройками экранирования спецсимволов
csv.register_dialect("semicol_no_escape", delimiter=";", quoting = csv.QUOTE_NONE, escapechar="\\")

# сохранение всех записей сразу writerows
with open("files/uav2.csv", "w") as f:
	writer = csv.writer(f, "semicol_no_escape")
	writer.writerows(lines_list)

# ====JSON====
import json
from pprint import pprint

# источник данных для файла JSON - сайт с API прогноза погоды
# https://open-meteo.com/en
# https://archive-api.open-meteo.com/v1/era5?latitude=55.75&longitude=37.62&start_date=2022-11-21&end_date=2022-11-21&hourly=temperature_2m,windspeed_10m,windspeed_100m,winddirection_10m,winddirection_100m,windgusts_10m&daily=sunrise,sunset&timezone=Europe%2FMoscow

# чтение JSON. load - из файла, loads - из переменной-строки
with open("files/open_meteo_api.json") as f:
	json_data = json.load(f)
pprint(json_data)

# сохранение JSON. dump - в файл, dumps - в строку (можно потом передать в функцию или на сервер либо эту строку записать как значение в dict)
with open("files/open_meteo_api2.json", "w") as f:
	json.dump(json_data, f, ensure_ascii=False, indent=2)


# ====XML====
# источник данных для файла XML - rss feed (новостной поток) с сайте DroneLife - новости о дронах 
# https://dronelife.com/feed/

# чтение XML. XML - это, по сути, вложенные списки, где все работает на индексах
# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
# если будет проблема с кодировкой, сначала нужно создать парсер и явно задать кодировку файла
parser = ET.XMLParser(encoding="utf-8")
# подставляем парсер при разборе xml
tree = ET.parse("files/drone_news.xml", parser)
# что такое корневой элемент xml
root = tree.getroot()
# тег (название элемента)
print(root.tag)
# атрибут ("настройки" элемента)
print(root.attrib)
# текст - то, что находится между открывающим и закрывающим тегом
print(root.text)

# работа с элементами - через "язык запросов" XPath
# findall находит все теги с нужным именем, find - находит только первый и останавливается
# теги записываются по уровням (и работают примерно как файловая система)
# в этом примере получаем все новости из rss-потока в список
news_list = root.findall("channel/item")
print(len(news_list))
# и далее выводим заголовок (тег title) и содержание (тег description) каждой новости
for news in news_list:
	print(f'Заголовок: {news.find("title").text}')
	print(f'Содержание: {news.find("description").text}')

# альтернатива - можно сразу найти все title или все description
# * заменяет собой любой тег, в том числе отсутствующий, поэтому поиск идет на указанном уровне и на уровнях выше
# поэтому результат - найдено 11 тегов title (10 новостей и title самого канала, который находится уровнем выше)
titles_list = root.findall("./*/*/title")
print(len(titles_list))
# здесь явно указано, что title находится строго на третьем уровне вложенности
# результат - найдено 10 тегов title, все они относятся к новостям
titles_list = root.findall("channel/item/title")
print(len(titles_list))
for title in titles_list:
	print(f'Заголовок: {title.text}')

# сохранение xml. сохраняется без отступов
tree.write("files/drone_news2.xml")

# чтобы сохранить xml в более читаемом виде, его придется сначала отформатировать. штатных способов в старых версиях питона (до 3.9) нет, через minidom - появляются лишние строки, поэтому проще установить и подключить модуль xmlformatter
# в параметрах указывается тип отступа (пробел, табулятор) и количество отступов
import xmlformatter
formatter = xmlformatter.Formatter(indent="2", indent_char=" ")
prettyxml = formatter.format_string(ET.tostring(root)).decode("utf-8")

with open("files/drone_news3.xml", "w") as f:
	f.write(prettyxml)

# ====PICKLE - бинарные файлы====
# небольшая структура данных для теста
import pickle
test_data = { 
	"latitude":55.75,
	"longitude":37.625,
	"elevation":(0.0, 0.3, 0.8, 10.0, 50.0, 152.0),
	"current_weather":{
		"temperature":-4.1, 
		"windspeed":10.1, 		
		"winddirection":86.0, 
		"weathercode":3, 
		"time":"2022-11-21T17:00"
	}
}

# сохранение в pickle. синтаксис тот же, что и для JSON, но файл должен быть открыт как двоичный на запись "wb"
with open("files/open_meteo_sample.pickle", "wb") as f:
	pickle.dump(test_data, f)

# чтение файла pickle. синтаксис тот же, что и для JSON, но файл должен быть открыт на чтение как двоичный. писать "rb" - обязательно
with open("files/open_meteo_sample.pickle", "rb") as f:
	json_data = pickle.load(f)
print(json_data)

# кстати, JSON научился записывать и кортежи (преобразовывает их в list автоматически. раньше он на кортежах падал)
import json
with open("files/open_meteo_sample.json", "w") as f:
	json.dump(test_data, f)