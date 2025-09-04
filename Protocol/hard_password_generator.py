# Код для генерации сложных паролей на Python

# Для сокращения ссылок в коде используется модуль secrets, 
# а для копирования сгенерированного пароля в буфер обмена —  pyperclip.

import argparse
import secrets
import string
import pyperclip

AMBIG = set('O0Il1') # Определяем набор символов, которые могут выглядеть похожими (амбивалентные символы).

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('-l', '--length', type=int, default=16,  # Указание длины пароля.
                    help='длина пароля (по умолчанию: 16)')
    ap.add_argument('-d', '--digits', action='store_true',  # Включать ли цифр в пароль.
                    help='включить цифры в пароль')
    ap.add_argument('-s', '--symbols', action='store_true',  # Включать ЛИ символов в пароль.
                    help='включить специальные символы в пароль')
    ap.add_argument('--no-ambig', action='store_true',
                    help='убрать похожие символы (например, O, 0, I, l, 1)')
    args = ap.parse_args()
    
    # Инициализируем список 'alphabet' всеми буквами (строчными и заглавными).
    alphabet = list(string.ascii_letters)
    if args.digits:
        alphabet += list(string.digits)
    if args.symbols:
        alphabet += list('!@#$%^&*()-_=+[]{};:,.<>?')
    if args.no_ambig:
        alphabet = [c for c in alphabet if c not in AMBIG]

    # Генерируем пароль: выбираем случайные символы из 'alphabet' указанное количество раз (args.length)
    # и объединяем их в одну строку.
    pwd = ''.join(secrets.choice(alphabet) for _ in range(args.length))
    pyperclip.copy(pwd) # Копируем сгенерированный пароль в буфер обмена.
    print('Пароль скопирован в буфер: ', pwd)
