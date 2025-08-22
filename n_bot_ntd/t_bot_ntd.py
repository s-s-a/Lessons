"""
Телеграмм бот для поиска файлов на яндекс диске по ключевым словам и загрузки их на сервер
"""
### https://habr.com/ru/articles/720130/
#  pip install aiogram
#  pip install yadisk

import os
import sqlite3 as sl
from datetime import datetime

import yadisk
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import cfg_token

bot = Bot(token=cfg_token.telebot_token)
dp = Dispatcher(bot)

ENCODING = 'utf-8'
DOWNLOAD_DIR = '/DownloadBot'
DEFAULT_SEARCH_DIR = 'GOST'  # папка по умолчанию стартовая для поиска

# токен яндекс диска
y = yadisk.YaDisk(token=cfg_token.ya_dsk_token)

# загружаемый файл должен содержать в своем имени
format_name_files = ['гост', 'gost', 'sp', 'сп', 'vsn', 'всн', 'sto', 'сто', 'rd', 'рд', 'серия']

# загружаемый файл должен иметь расширение
format_ext_files = ['.pdf', '.doc', '.docx', '.rtf', '.djvu']
search_dir = DEFAULT_SEARCH_DIR  # папка по умолчанию стартовая для поиска


def sget_base_bot(user_id, name_dir) -> str:
    """
    Работа с БД
    :param user_id:
    :param name_dir:
    :return:
    """
    con = sl.connect('databasebot.db')
    cur = con.cursor()
    ret_val = ''
    with con:
        cur.execute("CREATE TABLE IF NOT EXISTS user_seadir(id INTEGER NOT NULL PRIMARY KEY, seadir TEXT)")
    with con:
        cur.execute(f"SELECT seadir FROM user_seadir WHERE id = {user_id}")
        dat = cur.fetchone()
        if name_dir == '':  # блок запроса установленной папки
            if dat is not None:
                ret_val = dat[0]
            else:
                ret_val = DEFAULT_SEARCH_DIR
                cur.execute('INSERT INTO user_seadir (id, seadir) values(?, ?)', (user_id, DEFAULT_SEARCH_DIR))
        else:  # блок установки папки поиска
            if dat is None:
                cur.execute('INSERT INTO user_seadir (id, seadir) values(?, ?)', (user_id, name_dir))
            else:
                cur.execute('UPDATE user_seadir SET seadir = ? WHERE id = ?', (name_dir, user_id))
            ret_val = name_dir
    cur.close()
    con.close()
    return ret_val


# ----------------записать данные в рапорт---------------
def report_to_txt(str15):
    """
    Отчет в текстовый файл
    :param str15:
    """
    try:
        with open('Report.txt', 'a', encoding=ENCODING) as file4:
            file4.write(str15)
    except Exception as e:
        print(f'Ошибка: {e}')


# --------------- bot command user begin ----------------------------------------

@dp.message_handler(commands=['start', 'старт'])  ## команда /start
async def process_start_command(message: types.Message):
    """
    Команда /start
    :param message:
    """
    await bot.send_message(message.from_user.id, "Прива! Я бот-помощник! Ищу НТД и выдаю их Вам")
    await bot.send_message(message.from_user.id, "Работаю, правда, только в рабочее время в основном")
    await bot.send_message(message.from_user.id, "Имейте ввиду - я различаю большие и малые буквы. А НТД загружаю по 1шт за раз")
    await bot.send_message(message.from_user.id, "Также можно мне прислать файл НТД, которого у меня нет и я его добавлю")
    await bot.send_message(message.from_user.id, "Дополнительную информацию можно получить по команде /help")
    await bot.send_message(message.from_user.id, f"Текущая папка для поиска НТД: {sget_base_bot(message.from_user.id,'GOST')}. Её можно переключить командой (см. /help)")
    await bot.send_message(message.from_user.id, "Введите запрос на НТД (можно только номер или часть наименования):")


@dp.message_handler(commands=['help', 'хелп'])  ## команда /help
async def process_help_command(message: types.Message):
    """
    Команда /help
    :param message:
    """
    # тут не высттавляем папку поиска, берем ее из базы
    await bot.send_message(message.from_user.id,
                           "Введите запрос на НТД (можно только номер или часть наименования) и отправьте мне, а я поищу где-то и если найду, то отправлю Вам файл, по 1шт за раз.")
    await bot.send_message(message.from_user.id,
                           "Еще мне можно прислать то чего нет пока у меня, после проверки добавлю к себе и тогда оно будет:).")
    await bot.send_message(message.from_user.id, "Доступны команды: /start (или /старт) - инфа при старте бота")
    await bot.send_message(message.from_user.id, "/about (или /абут) - инфа о боте и разработчике")
    await bot.send_message(message.from_user.id,
                           "/status (или /статус) - выдает ответ о работе. Если ответа нет - не в сети")
    await bot.send_message(message.from_user.id,
                           "/sms MESSAGE (или /смс <текст сообщения>) — отправить любое сообщение MESSAGE разработчику бота.")
    await bot.send_message(message.from_user.id,
                           "/gost , /sp , /vsn, /sto, /rd (или русскими буквами)- Установка папки для поиска по виду НТД.")
    await bot.send_message(message.from_user.id,
                           f"Сейчас в папке поиска: {sget_base_bot(message.from_user.id, '')}")


@dp.message_handler(commands=['GOST', 'gost', 'ГОСТ', 'гост'])  ## команда /GOST
async def process_gost_command(message: types.Message):
    """
    Команда /GOST
    :param message:
    """
    await bot.send_message(message.from_user.id,
                           f"Установлена текущая папка для поиска НТД: {sget_base_bot(message.from_user.id, DEFAULT_SEARCH_DIR)}")


@dp.message_handler(commands=['SP', 'sp', 'СП', 'сп'])  ## команда /SP
async def process_sp_command(message: types.Message):
    """
    Команда /SP
    :param message:
    """
    await bot.send_message(message.from_user.id,
                           f"Установлена текущая папка для поиска НТД: {sget_base_bot(message.from_user.id, 'SP')}")


@dp.message_handler(commands=['RD', 'rd', 'РД', 'рд'])  ## команда /RD
async def process_rd_command(message: types.Message):
    """
    Команда /RD
    :param message:
    """
    await bot.send_message(message.from_user.id,
                           f"Установлена текущая папка для поиска НТД: {sget_base_bot(message.from_user.id, 'RD')}")


@dp.message_handler(commands=['VSN', 'vsn', 'ВСН', 'всн'])  ## команда /VSN
async def process_vsn_command(message: types.Message):
    """
    Команда /VSN
    :param message:
    """
    await bot.send_message(message.from_user.id,
                           f"Установлена текущая папка для поиска НТД: {sget_base_bot(message.from_user.id, 'VSN')}")


@dp.message_handler(commands=['STO', 'sto', 'СТО', 'сто'])  ## команда /STO
async def process_sto_command(message: types.Message):
    """
    Команда /STO
    :param message:
    """
    await bot.send_message(message.from_user.id,
                           f"Установлена текущая папка для поиска НТД: {sget_base_bot(message.from_user.id, 'STO')}")


@dp.message_handler(commands=['Serii', 'SERII', 'serii', 'Серии', 'СЕРИИ', 'серии', 'Серия', 'СЕРИЯ', 'серия'])  ## команда /SERII
async def process_serii_command(message: types.Message):
    """
    Команда /SERII
    :param message:
    """
    await bot.send_message(message.from_user.id,
                           f"Установлена текущая папка для поиска НТД: {sget_base_bot(message.from_user.id, 'Serii')}")


@dp.message_handler(commands=['about', 'абут', 'разработчик'])  ## команда /about
async def process_about_command(message: types.Message):
    """
    Команда /about
    :param message:
    """
    await bot.send_message(message.from_user.id,
                           "Разработчик revalpam@ya.ru. Бот создан для оперативного получения документации в лично-производственных целях.")


@dp.message_handler(commands=['status', 'статус'])  ## команда /status
async def process_status_command(message: types.Message):
    """
    Команда /status
    :param message:
    """
    await bot.send_message(message.from_user.id, "Работаю. Тут я. А шо такое? Вводите запрос и тисните Ентер:)")
    await bot.send_message(message.from_user.id,
                           f"Текущая папка для поиска НТД: {sget_base_bot(message.from_user.id, '')}")


@dp.message_handler(commands=['sms', 'смс'])  ## команда /sms сообщение разработчику
async def process_sms_command(message: types.Message):
    """
    Команда /sms сообщение разработчику
    :param message:
    """
    report_to_txt(f'\nПользователь id {message.from_user.id} отправил сообщение: {message.text}')
    await bot.send_message(message.from_user.id, "Сообщение разработчику отправлено")


# --------------- bot command user end ------------------------------------------

# --------------- service command admin begin -----------------------------------
# выгружает файл отчета в облако и удаляет!!! его с диска
@dp.message_handler(commands=['rep123456789'])  ## команда /rep отчет
async def process_rep_command(message: types.Message):
    """
    Команда /rep отчет
    :param message:
    """
    try:
        # путь к загружаемым в облако файлам от пользователей
        src = '/ReportBot'
        if not y.is_dir(src):
            y.mkdir(src)
        destin_file = f'{src}/Report-{datetime.now().strftime("%d.%m.%Y-%H.%M.%S")}.txt'
        if y.is_file(destin_file):
            y.remove(destin_file, permanently=True)
        # грузим в облако файлы
        if os.path.exists('Report.txt'):
            y.upload('Report.txt', destin_file)
            os.remove('Report.txt')
        await bot.send_message(message.from_user.id, "Отчёт обработан")
    except Exception as e:
        print(f'Ошибка: {e}')


# показывает файл отчета с диска
@dp.message_handler(commands=['view-rep123456789'])  ## команда показать отчет
async def process_view_report_command(message: types.Message):
    """
    Команда показать отчет
    :param message:
    """
    try:
        if os.path.exists('Report.txt'):
            with open('Report.txt', encoding=ENCODING) as f5:
                ch_file = len(f5.read())
            if ch_file < 2400:
                with open('Report.txt', 'r', encoding=ENCODING) as f5:
                    await bot.send_message(message.from_user.id, f5.read())
            else:
                await bot.send_message(message.from_user.id,
                                       "Отчёт слишком большой. Лучше смотреть в облаке после команды /rep")
        else:
            await bot.send_message(message.from_user.id, "Отчёт не создавался пока")
    except Exception as e:
        print(f'Ошибка: {e}')


##@dp.message_handler(commands=['stop']) ## команда /stop  работает криво - много ошибок иде показывает
##async def process_stop_command(message: types.Message):
##    await bot.send_message(message.from_user.id, "Останавливаюсь.")
##    sys.exit()
# --------------- service command admin end -------------------------------------

@dp.message_handler(content_types=['text'])  ## получаем сообщение от юзера
async def get_text_messages(message: types.Message):
    """
    Получаем сообщение от юзера
    :param message:
    """
    search_dir = sget_base_bot(message.from_user.id, '')
    report_to_txt(f'\nПользователь id {message.from_user.id} сделал запрос на поиск в папке {search_dir}: {message.text}')
    await bot.send_message(message.from_user.id, f'Запускаю процесс поиска в папке {search_dir} : {message.text}')
    if y.check_token():
        if not y.is_dir('/' + search_dir):
            await bot.send_message(message.from_user.id, f'Папка {search_dir} не обнаружена. Что-то поломалось. Извините.')
        else:
            Spis = []
            for item in y.listdir(search_dir):
                if message.text in item['name']:
                    if len(Spis) < 7:
                        await bot.send_message(message.from_user.id, f'Обнаружен документ: {item["name"]}')
                    Spis.append(item['name'])
            if len(Spis) == 0:
                await bot.send_message(message.from_user.id,
                                       f'Извините, пока такого документа в папке {search_dir} не нашлось.')
                await bot.send_message(message.from_user.id,
                                       'Но если Вы мне его сюда скинете, после проверки я его добавлю.')
            if len(Spis) == 1:
                # ------------даем ссылку на файл-------------------
                y.publish('/' + search_dir + '/' + Spis[0])  # делаем публичный файл
                # шлем ссылку
                await bot.send_message(message.from_user.id, y.get_meta(f'/{search_dir}/{Spis[0]}').public_url)
            if len(Spis) > 1:
                await bot.send_message(message.from_user.id,
                                       f'Найдено документов: {len(Spis)}. Уточните запрос:')
    else:
        await bot.send_message(message.from_user.id,
                               'Извините по каким-то причинам диск не доступен. Попробуйте в другой раз')


@dp.message_handler(content_types=['document'])  # получаем файл от юзера
async def handle_file(message):
    """
    Получаем файл от юзера
    :param message:
    """
    try:
        # если файл такой как надо, то качаем
        str_nam_file = str(message.document.file_name).lower() ## переводим в нижний регистр для избавления от регистрозависимости
        len_str_nf = len(str_nam_file)
        if (str_nam_file.endswith(tuple(format_name_files), 0, len_str_nf)
                and str_nam_file.endswith(tuple(format_ext_files), 0, len_str_nf)):
            file_id = message.document.file_id
            file = await bot.get_file(file_id)
            file_path = file.file_path
            # ------------Вариант загрузки файлов в яндекс-облако------------
            # путь к загружаемым в облако файлам от пользователей
            if not y.is_dir(DOWNLOAD_DIR):
                y.mkdir(DOWNLOAD_DIR)
            src = f'{DOWNLOAD_DIR}/{message.document.file_name}'
            print(src)
            # грузим в облако файл от пользователя
            if y.is_file(src):  # если такой файл есть то яндя даст ошибку, поэтому: вот
                src = f'{DOWNLOAD_DIR}/Double-{datetime.now().strftime("%d.%m.%Y-%H.%M.%S")}-{message.document.file_name}'
            y.upload(await bot.download_file(file_path), src)
            await bot.send_message(message.from_user.id, 'Загрузил. Спасибо. После проверки добавлю в свою базу:)')
            # сделать запись после загрузки в файл Report.txt
            report_to_txt(f'\nПользователь id {message.from_user.id} прислал файл: {message.document.file_name}')
        else:
            await bot.send_message(message.from_user.id,
                                   'Простите, но присланный Вами файл не содержит в имени тип НТД (ГОСТ, СП, ВСН и т.д.) и/или не подходит по формату, нужен .pdf или .doc')
    except Exception as e:
        print(f'Ошибка: {e}')
        await bot.send_message(message.from_user.id,
                               f'Я наверное не смогу загрузить, что-то сломалось и выдает ошибку: {e}')


if __name__ == '__main__':
    executor.start_polling(dp)

##  executor.start_polling(dp, skip_updates=True)
##Параметр skip_updates=True позволяет пропустить накопившиеся входящие сообщения, если они нам не важны
