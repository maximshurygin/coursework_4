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

