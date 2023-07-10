import json
from abc import ABC, abstractmethod


class JSON(ABC):
    FILENAME = 'vacancies.json'

    @abstractmethod
    def save_json(self, api_object):
        pass

    @abstractmethod
    def get_vacancy_by_salary(self, x):
        pass

    @abstractmethod
    def delete_vacancy(self, x):
        pass


class JSONSaver(JSON):

    def save_json(self, api_object):
        """Записывает в JSON-файл найденные вакансии"""
        object_list = []
        for vacancy in api_object.get_vacancies():
            object_list.append(vacancy)

        with open(self.FILENAME, 'w', encoding='utf-8') as file:
            json.dump(object_list, file, indent=2, ensure_ascii=False)

    def get_vacancy_by_salary(self, salary_from):
        """Возвращает список вакансий соответствующих указанной минимальной з/п"""
        vacancy_list = []
        with open(self.FILENAME, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for x in data:
                if x['salary from']:
                    if x['salary from'] >= salary_from:
                        vacancy_list.append(x)

        return vacancy_list

    def delete_vacancy(self, new_data):
        """Перезаписывает  JSON-файл оставляя только отсортированные вакансии"""
        with open(self.FILENAME, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=2, ensure_ascii=False)
