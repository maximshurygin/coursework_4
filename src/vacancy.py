class Vacancy:
    def __init__(self, name, firm, salary_from, salary_to, url, area):
        self.name = self.validate_str(name)
        self.firm = self.validate_str(firm)
        self.salary_from = self.validate_number(salary_from)
        self.salary_to = self.validate_number(salary_to)
        self.url = self.validate_str(url)
        self.area = self.validate_str(area)

    @staticmethod
    def validate_str(string):
        """Проверка строкового типа"""
        if isinstance(string, str):
            return string

    @staticmethod
    def validate_number(number):
        """Проверка чилсового типа"""
        if isinstance(number, (int, float)):
            return number

    def __str__(self):
        """Вывод информации о классе для пользователя"""
        return f'Вакансия: {self.name} ' \
               f'Фирма: {self.firm} ' \
               f'Зарпалат от {self.salary_from} до {self.salary_to} ' \
               f'Ссылка: {self.url} ' \
               f'Город: {self.area}'

    def __eq__(self, other):
        """Проверка равенства объектов по минимальной з/п"""
        return self.salary_from == other.salary_from

    def __lt__(self, other):
        """Проверка того, что текущий объект меньше другого объекта по минимальной з/п"""
        return self.salary_from < other.salary_from

    def __le__(self, other):
        """Проверка того, что текущий объект меньше или равен другому объекту по минимальной з/п"""
        return self.salary_from <= other.salary_from

    def __gt__(self, other):
        """Проверка того, что текущий объект больше другого объекта по минимальной з/п"""
        return self.salary_from > other.salary_from

    def __ge__(self, other):
        """Проверка того, что текущий объект больше или равен другому объекту по минимальной з/п"""
        return self.salary_from >= other.salary_from