"""
Необходимо написать программу, записывающую и читающую текстовый файл.
Файл должен состоять из строк. Каждая строка должа иметь поля. Поля должны быть разделены с помощью какого-либо символа,
например, запятой, двоеточием или любым другим, который не используется в тексте поля. Программа должна производить
разбоp полей, а не воспринимать считанную строку как единое целое.
"""


data = open('first.txt', encoding="utf8").read()
print(data.split("\n"))
name = []
last_name = []
year = []
city = []

for element in data.split("\n"):
    str =element.split(';')
    name.append(str[0])
    last_name.append(str[1])
    year.append(str[2])
    city.append(str[3])


file_2 = open('name.txt', 'w', encoding="utf8")
for name in name:
    file_2.write(name + '\n')
file_3 = open('last_name.txt', 'w', encoding="utf8")
for last_name in last_name:
    file_3.write(last_name + '\n')
file_4 = open('year.txt', 'w', encoding="utf8")
for year in year:
    file_4.write(year + '\n')
file_5 = open('city.txt', 'w', encoding="utf8")
for city in city:
    file_5.write(city + '\n')