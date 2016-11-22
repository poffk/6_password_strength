import re


def load_data(filepath):
    with open(filepath) as data_file:
        return data_file.read()


def get_password_strength(password, blacklist):
    password_strength_mark = 0
    #количество символов (<4-1b, <12-2b, >12-3b)
    if len(password) < 4:
        password_strength_mark = password_strength_mark + 1
    elif len(password) < 12:
        password_strength_mark = password_strength_mark + 2
    else:
        password_strength_mark = password_strength_mark + 3
    #верхний и нижний регистр 2b
    if re.findall(r'[A-Z]', password) and re.findall(r'[a-z]', password):
        password_strength_mark = password_strength_mark + 2
    #есть и буквы цифры 2b
    if re.findall(r'[^ \W|\d]', password) and re.findall(r'[\d]', password):
        password_strength_mark = password_strength_mark + 2
    #специальные символы 2b
    if re.findall(r'\W', password):
        password_strength_mark = password_strength_mark + 2
    #blacklist 1b
    if password not in re.findall(r'\w+', blacklist):
        password_strength_mark = password_strength_mark + 1
    return password_strength_mark


if __name__ == '__main__':
    password = input('Введите пароль для проверки: ')
    blacklist = load_data('blacklist.txt')
    print(get_password_strength(password, blacklist))