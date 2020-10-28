import requests
import json
import string
import pymorphy2

URL = 'https://api.hh.ru/vacancies'
params = {
    'text': 'Python AND Москва',
    'only_with_salary': True,
    'page': 1,
    'per_page': 100
}

result = requests.get(URL, params = params).json()
found_vacanc = result['found']
pages = result['pages']

print('Всего найдено {} вакансий на {} страницах'. format(result['found'], result['pages']))

#соберем все навыки
text = ''
for i in range(1, pages):
    URL = 'https://api.hh.ru/vacancies'
    params = {'text': 'Python AND Москва',
              'only_with_salary': True,
              'page': i,
              'per_page': 100}
    result = requests.get(URL, params=params).json()
    items = result['items']

    for i in items:
        snippet = i['snippet']
        requirement = snippet['requirement']
        responsibility = snippet['responsibility']
        text += str(responsibility)
        text += str(requirement)

#почистим и получим dict, в котором ключ - слово, значение - количество появлений в тексте.
for i in string.punctuation:
    text = text.replace(i, ' ')

text = text.lower()
text = text.split()

skills = ['python', 'sql', 'git', 'linux', 'javascript', 'django', 'hive', 'sas', 'scrum',
          'aosp', 'unix', 'ruby', 'php', 'nodejs', 'matlab', 'frontend', 'backend', 'web',
          'office', 'qt', 'pyqt', 'java', 'c+', 'c#', 'experience', 'r', 'pandas', 'numpy']

dict = {}
for i in text:
    dict[i] = text.count(i)

list = list(dict.items())

def sort_count(inputStr):
    return inputStr[1]

list = sorted(list, key=sort_count, reverse=True)
n = 1
print('Топ 10 навыков профессии и как часто встречаются (в процентах):')

for i in range(len(list)):
    if list[i][0] in skills:
       print(f'{n}) {list[i][0].capitalize()}: встречается в {round(list[i][1]*100/found_vacanc, 2)} % вакансий')
       n += 1
    if n == 11:
        break

