from abc import ABC, abstractmethod
import requests
import os


class API(ABC):

    def __init__(self, keyword):
        self.keyword = keyword

    @abstractmethod
    def get_vacancies(self):
        pass


class HHApi(API):

    def __init__(self, keyword):
        super().__init__(keyword)
        self.url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self):
        """Возвращает по ключевому слову список вакансий из Head Hunter"""
        vacancies = []
        params = {'text': self.keyword}
        response = requests.get(self.url, params=params)
        for row in response.json()['items']:
            if row['salary'] is not None:
                vacancies.append({
                    'name': row['name'],
                    'firm': row['employer']['name'],
                    'salary from': row['salary']['from'],
                    'salary to': row['salary']['to'],
                    'url': row['alternate_url'],
                    'area': row['area']['name'],
                })

        return vacancies


class SJApi(API):

    def __init__(self, keyword):
        super().__init__(keyword)
        self.url = "https://api.superjob.ru/2.0/vacancies"

    def get_vacancies(self):
        """Возвращает по ключевому слову список вакансий из SuperJob"""
        vacancies = []
        params = {'keyword': self.keyword}
        headers = {'X-Api-App-Id': os.getenv('SJ_API_KEY')
                   }
        response = requests.get(self.url, headers=headers, params=params)

        for row in response.json()['objects']:
            vacancies.append({
                'name': row['profession'],
                'firm': row['firm_name'],
                'salary from': row['payment_from'],
                'salary to': row['payment_to'],
                'url': row['link'],
                'area': row['town']['title'],
            })

        return vacancies
