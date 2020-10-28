import requests
import pprint
import json
import string

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

#почистим и получим dict, в котором ключ - слово, значение - количество появлений в тексте. В конце выведем топ-10
for i in string.punctuation:
    text = text.replace(i, ' ')
text = text.lower()
text = text.split()
skills = ['python', 'django',  'flask', 'pandas', 'api', 'sql', 'nodejs', 'php', 'git','numpy']
dict = {}
for i in text:
    dict[i] = text.count(i)
list = list(dict.items())
for i in range(len(list)):
    if list[i][0] in skills:
       print(f'навыки встречаются:{list[i]} - в {round(list[i][1] * 100 / found_vacanc)} % вакансий')