import re
import csv


#1
text_1 = open('task1-ru.txt', encoding='utf-8').read()

print(re.findall(r'\bс[а-яё]+', text_1, flags=re.I))
print(re.findall(r'\bи\s+[а-яё]+', text_1, flags=re.I))


#2
html = open('task2.html', encoding='utf-8').read()
fonts = re.findall(r"font-family\s*:\s*'([^']+)'", html)
unique_fonts = set(fonts)

print(unique_fonts)


#3
file = open('task3.txt', encoding='utf-8').read().split()

ids = [id for id in file if re.fullmatch(r'\d+', id)]
l_name = [name for name in file if re.fullmatch(r'[A-Z][a-zA-Z]+', name)]
emails = [email for email in file if re.fullmatch(r'\S+@\S+', email)]
date = [date for date in file if re.fullmatch(r'\d{4}-\d{2}-\d{2}', date)]
web = [web for web in file if re.fullmatch(r'https?://\S+|www\.\S+', web)]

rows = [[ids[i], l_name[i], emails[i], date[i], web[i]] for i in range(len(ids))]

with open('sorted_database.csv','w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ID','Фамилия','Почта','Дата','Сайт'])
    w.writerows(rows)

print('количество строк в файле:', len(rows))