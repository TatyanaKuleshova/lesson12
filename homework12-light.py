import requests
import pprint
import json

URL = 'https://api.hh.ru/vacancies'
params = {
    'text': 'Python AND Москва',
    'only_with_salary': True,
    'per_page': 100
}

#вычисляем количество вакансий с указанием зарплаты
result = requests.get(URL, params = params).json()
found_vacanc = result['found']
pages = result['pages']
salary_from = []
salary_to = []

print('Всего найдено {} вакансий с указанием зарплаты на {} страницах'. format(result['found'], result['pages']))

#вычисляем зарплату от и до
for i in range(1, pages):
    URL = 'https://api.hh.ru/vacancies'
    params = {'text': 'Python AND Москва',
              'only_with_salary': True,
              'page': i,
              'per_page': 20}
    result = requests.get(URL, params = params).json()
    items = result['items']

    for i in items:
        salary = i['salary']
        s_from = salary['from']
        s_to = salary['to']

        if s_from != None:
            salary_from.append(s_from)
        if s_to != None:
            salary_to.append(s_to)

mid_s_from = round(sum(salary_from)/len(salary_from))
mid_s_to = round(sum(salary_to)/len(salary_to))

print ('Зарплата Python-разработчика в Москве составляет от {} руб. до {} руб.'.format(mid_s_from, mid_s_to ))

