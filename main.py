import random
import re

interval = [str(x) for x in range(6, 31)]  # Количество символов в пароле.
p_numbers = "0123456789"
p_lowercase = "abcdefghijklmnopqrstuvwxyz"
p_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p_symbol = "!#$%&*?@"
p_phrase = ""  # Фраза придуманная пользователем.


def user_survey(question):  # Проверка ответа на вопрос. Какие символы нужно добавить в пароль.

    while question != "Да" and question != "Нет":
        question = input("Ответ только 'Да' или 'Нет': ")
    return question


numbers = input("Использовать цифры?(Да/Нет): ")
user_survey(numbers)

uppercase_letters = input("Использовать прописные буквы?(Да/Нет): ")
user_survey(uppercase_letters)

lowercase_letters = input("Использовать строчные буквы?(Да/Нет): ")
user_survey(lowercase_letters)

special_symbol = input("Использовать специальные символы?(Да/Нет): ")
user_survey(special_symbol)

while numbers == "Нет" and uppercase_letters == "Нет" and lowercase_letters == "Нет" and special_symbol == "Нет":
    print("Нужно выбрать минимум 1 пункт!!!")
    numbers = input("Использовать цифры?(Да/Нет): ")
    user_survey(numbers)

    uppercase_letters = input("Использовать прописные буквы?(Да/Нет): ")
    user_survey(uppercase_letters)

    lowercase_letters = input("Использовать строчные буква?(Да/Нет): ")
    user_survey(lowercase_letters)

    special_symbol = input("Использовать специальные символы?(Да/Нет): ")
    user_survey(special_symbol)

password_length = input("Длинна пароля(6-30): ")

while password_length.isalpha():
    password_length = input("Нужно ввести число или цифру: ")

while password_length not in interval:
    password_length = input("Ответ в диапазоне 6-30: ")

p_phrase_question = input("Хотите добавить свою фразу в пароль?(Да/Нет): ")
while p_phrase_question != "Да" and p_phrase_question != "Нет":
    p_phrase_question = input("Ответ только 'Да' или 'Нет': ")

if p_phrase_question == "Да":
    p_phrase = input("Ваша фраза для добавления в пароль: ").replace(" ", "")
    while not re.match(r'[a-zA-Z]', p_phrase):
        p_phrase = input('Фраза должна содержать только латинские буквы: ')
    while len(p_phrase) + 1 > int(password_length):
        p_phrase = input("Фраза не может быть больше длинны пароля: ")

number_of_passwords = input("Сколько сгенерированных паролей Вы хотите получить?: ")

while int(number_of_passwords) < 0:
    number_of_passwords = input("Выбор не может быть меньше 1: ")

while number_of_passwords.isalpha():
    number_of_passwords = input("Нужно ввести число или цифру: ")


def gen_password(numbers_id, uppercase_letters_id, lowercase_letters_id, special_symbol_id, password_length_id,
                 number_of_passwords_id):
    for _ in range(int(number_of_passwords_id)):  # Количество паролей.
        password = ""  # Сгенерированный пароль
        change_user = ""  # Выбранный набор элементов пользователем.
        lst_change_user = []
        if numbers_id == "Да":
            change_user += p_numbers
        if uppercase_letters_id == "Да":
            change_user += p_uppercase
        if lowercase_letters_id == "Да":
            change_user += p_lowercase
        if special_symbol_id == "Да":
            change_user += p_symbol

        for i in change_user:
            lst_change_user.append(i)

        password += p_phrase  # добавление фразы пользователя к паролю

        for i in range(int(password_length_id) - len(p_phrase)):
            password += random.choice(lst_change_user)

        file = open("D:\password.txt", "a")
        file.write(f"{password}\n")
        file.close()
        print(f"Ваш пароль: {password}")


gen_password(numbers, uppercase_letters, lowercase_letters, special_symbol, int(password_length),
             int(number_of_passwords))

input("Пароль(и) записан(ы) в файл password.txt на диск D.\nНажмите ENTER для завершения")
