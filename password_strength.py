import re
import getpass


def load_data(filepath):
    with open(filepath) as data_file:
        return data_file.read()


def password_length_scoring(password):
    if len(password) < 4:
        return 1
    elif len(password) < 12:
        return 2
    else:
        return 3


def password_register_scoring(password):
    if re.findall(r'[A-Z]', password) and re.findall(r'[a-z]', password):
        return 2
    else:
        return 0


def password_figures_and_letters_scoring(password):
    if re.findall(r'[^ \W|\d]', password) and re.findall(r'[\d]', password):
        return 2
    else:
        return 0


def password_special_letters_scoring(password):
    if re.findall(r'\W', password):
        return 2
    else:
        return 0


def password_blacklist_scoring(password, blacklist):
    if password not in re.findall(r'\w+', blacklist):
        return 1
    else:
        return 0


def get_password_strength(password, blacklist):
    password_strength_mark = 0
    password_strength_mark += password_length_scoring(password)
    password_strength_mark += password_register_scoring(password)
    password_strength_mark += password_figures_and_letters_scoring(password)
    password_strength_mark += password_special_letters_scoring(password)
    password_strength_mark += password_blacklist_scoring(password, blacklist)
    return password_strength_mark


if __name__ == '__main__':
    print('Введите пароль для проверки: ')
    password = getpass.getpass()
    blacklist = load_data('blacklist.txt')
    print(get_password_strength(password, blacklist))