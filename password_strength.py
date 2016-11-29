import re
import getpass


def load_data(filepath):
    with open(filepath) as data_file:
        return data_file.read()


def password_length_check_and_rate(password):
    if len(password) < 4:
        return 1
    elif len(password) < 12:
        return 2
    else:
        return 3


def password_register_check(password):
    return re.findall(r'[A-Z]', password) and re.findall(r'[a-z]', password)


def password_register_rate(password, password_strength_mark):
    if password_register_check(password):
        password_strength_mark += 2
    return password_strength_mark


def password_figures_and_letters_check(password):
    return re.findall(r'[^ \W|\d]', password) and re.findall(r'[\d]', password)


def password_figures_and_letters_rate(password, password_strength_mark):
    if password_figures_and_letters_check(password):
        password_strength_mark += 2
    return password_strength_mark


def password_special_letters_check(password):
    return re.findall(r'\W', password)


def password_special_letters_rate(password, password_strength_mark):
    if password_special_letters_check(password):
        password_strength_mark += 2
    return password_strength_mark


def password_blacklist_check(password, blacklist):
    return password not in re.findall(r'\w+', blacklist)


def password_blacklist_rate(password, blacklist, password_strength_mark):
    if password_blacklist_check(password, blacklist):
        password_strength_mark += 1
    return password_strength_mark


def get_password_strength(password, blacklist):
    password_strength_mark = 0
    password_strength_mark = password_length_check_and_rate(password)
    password_strength_mark = password_register_rate(password, password_strength_mark)
    password_strength_mark = password_figures_and_letters_rate(password, password_strength_mark)
    password_strength_mark = password_special_letters_rate(password, password_strength_mark)
    password_strength_mark = password_blacklist_rate(password, blacklist, password_strength_mark)
    return password_strength_mark


if __name__ == '__main__':
    print('Введите пароль для проверки: ')
    password = getpass.getpass()
    blacklist = load_data(input('Введите путь до черного списка паролей: '))
    print('Оценка Вашего пароля: {}'.format(get_password_strength(password, blacklist)))