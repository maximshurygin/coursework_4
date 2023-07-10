class Vacancy:
    def __init__(self, name, firm, salary_from, salary_to, url, area):
        self.__name = self.validate_str(name)
        self.__firm = self.validate_str(firm)
        self.__salary_from = self.validate_number(salary_from)
        self.__salary_to = self.validate_number(salary_to)
        self.__url = self.validate_str(url)
        self.__area = self.validate_str(area)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def firm(self) -> str:
        return self.__firm

    @property
    def salary_from(self) -> (int, float):
        return self.__salary_from

    @property
    def salary_to(self) -> (int, float):
        return self.__salary_to

    @property
    def url(self) -> str:
        return self.__url

    @property
    def area(self) -> str:
        return self.__area

    @staticmethod
    def validate_str(string) -> str:
        """Проверка строкового типа"""
        if isinstance(string, str):
            return string

    @staticmethod
    def validate_number(number) -> (int, float):
        """Проверка числового типа"""
        if isinstance(number, (int, float)):
            return number

    def __str__(self) -> str:
        """Вывод информации о классе для пользователя"""
        return f'Вакансия: {self.name}. ' \
               f'Фирма: {self.firm}. ' \
               f'Зарплата от {self.salary_from} до {self.salary_to}. ' \
               f'Ссылка: {self.url}. ' \
               f'Город: {self.area}.'

    def __eq__(self, other) -> bool:
        """Проверка равенства объектов по минимальной з/п"""
        return self.salary_from == other.salary_from

    def __lt__(self, other) -> bool:
        """Проверка того, что текущий объект меньше другого объекта по минимальной з/п"""
        return self.salary_from < other.salary_from

    def __le__(self, other) -> bool:
        """Проверка того, что текущий объект меньше или равен другому объекту по минимальной з/п"""
        return self.salary_from <= other.salary_from

    def __gt__(self, other) -> bool:
        """Проверка того, что текущий объект больше другого объекта по минимальной з/п"""
        return self.salary_from > other.salary_from

    def __ge__(self, other) -> bool:
        """Проверка того, что текущий объект больше или равен другому объекту по минимальной з/п"""
        return self.salary_from >= other.salary_from
