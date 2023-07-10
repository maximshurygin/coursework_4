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
