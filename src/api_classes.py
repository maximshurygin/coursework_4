from abc import ABC, abstractmethod
import requests
import os


class API(ABC):

    def __init__(self, keyword):
        self.keyword = keyword

    @abstractmethod
    def get_vacancies(self):
        pass