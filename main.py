from src.utils import user_interaction_hh, user_interaction_sj


def user_interaction():
    """Взаимодействие программы с пользователем"""
    while True:
        platform = input('Введите нужную цифру для выбора платформы:\n'
                         '1-Head Hunter; 2-SuperJob\n')

        if platform == '1':
            user_interaction_hh()

        elif platform == '2':
            user_interaction_sj()

        else:
            print('Неверно выбрана платформа.')
            break

        user_choice_2 = input('\nХотите продолжить поиск вакансий?\n'
                              'Введите нужную цифру\n'
                              '1-Да; 2-Нет\n')
        if user_choice_2 == '1':
            pass
        else:
            print('До свидания!')
            break


if __name__ == '__main__':
    user_interaction()
