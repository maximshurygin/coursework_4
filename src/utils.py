import json
from src.vacancy import Vacancy
from src.api_classes import HHApi, SJApi
from src.json_classes import JSONSaver

FILENAME = 'vacancies.json'


def show_vacancy():
    """Возвращает список для показа в консоль"""
    with open(FILENAME, 'r', encoding='utf-8') as file:
        data = json.load(file)

    vacancies = [Vacancy(line["name"], line["firm"], line["salary from"],
                         line["salary to"], line["url"], line["area"]) for line in data]

    for x in vacancies:
        print(x)


def show_top_vacancy():
    """Возвращает список top-5 вакансий"""
    with open(FILENAME, 'r', encoding='utf-8') as file:
        data = json.load(file)
    vacancies = [Vacancy(line["name"], line["firm"], line["salary from"],
                         line["salary to"], line["url"], line["area"]) for line in data]
    top_vacancies = sorted(vacancies, key=lambda x: x.salary_from, reverse=True)[:5]

    if len(top_vacancies) >= 5:
        print('Топ-5 вакансий:\n')
        for x in top_vacancies[:5]:
            print(x)
    else:
        print('Недостаточно вакансий для отображения топ-5\n')
