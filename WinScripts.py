# Скрипты для работы с Windows на Python часть 4

# В скриптах используется библиотека pywin32.
# ➡️Установка библиотеки: pip install pywin32

import os
import win32api
import win32con
import win32net
import win32netcon
import ctypes
import win32com.client

# 💻 Выключение компьютера через Python:

os.system("shutdown /s /t 10")  # Выключение через 10 секунд

# 🔄 Перезагрузка компьютера:

os.system("shutdown /r /t 5")  # Перезагрузка через 5 секунд

# 🖥 Смена имени компьютера:
win32api.SetComputerName("NEW-PC-NAME")  # Изменение имени компьютера

# ⚙️ Открытие "Диспетчера задач":

win32api.ShellExecute(0, "open", "taskmgr.exe", None, None, 1)

# 📁 Создание ярлыка на рабочем столе:

# Получаем путь к рабочему столу текущего пользователя

desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Задаём путь, где будет создан ярлык

target_path = os.path.join(desktop, "Блокнот.lnk")

# Создаём объект для работы с ярлыками через Windows Script Host

shell = win32com.client.Dispatch("WScript.Shell")

# Создаем ярлык

target_shortcut = shell.CreateShortcut(target_path)

# Указываем путь к исполняемому файлу блокнота

target_shortcut.TargetPath = "C:\\Windows\\System32\\notepad.exe"

# Сохраняем ярлык

target_shortcut.Save()


# 🔍 Получение списка установленных программ:

# Подключаемся к WMI (Windows Management Instrumentation), чтобы получать системную информацию

wmi = win32com.client.GetObject("winmgmts:\\\\.\\root\\CIMV2")

# Выполняем WMI-запрос для получения списка установленных программ

programs = wmi.ExecQuery("SELECT * FROM Win32_Product")

# Перебираем полученные объекты и выводим названия установленных программ

for program in programs:
    print(program.Name)


# ⚡️ Запуск программы от имени администратора:

# Создаём объект Shell.Application для управления оболочкой Windows

shell = win32com.client.Dispatch("Shell.Application")

# Запускаем Блокнот (notepad.exe) с правами администратора

# Параметры ShellExecute:

# 1. "notepad.exe" – исполняемый файл
# 2. "" – аргументы командной строки (здесь пустая строка)
# 3. "" – рабочая директория (здесь не задана)
# 4. "runas" – запуск от имени администратора
# 5. 1 – окно открывается в нормальном режиме

shell.ShellExecute("notepad.exe", "", "", "runas", 1)

# 🌅 Изменение обоев рабочего стола:

# Указываем путь к изображению, которое будет установлено в качестве обоев рабочего стола

path = "C:\\Path\\To\\Wallpaper.jpg"

# Устанавливаем изображение в качестве обоев рабочего стола с помощью SystemParametersInfoW

# Параметры:

# 1. win32con.SPI_SETDESKWALLPAPER – указывает на смену обоев рабочего стола
# 2. 0 – резервный параметр (не используется)
# 3. path – путь к изображению
# 4. 3 – обновление параметров пользователя (SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)

ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER, 0, path, 3)


# 👥 Получение списка пользователей системы:

server = (
    None  # Указываем, что работаем с локальным компьютером (можно указать имя сервера)
)
level = 0  # Уровень детализации информации о пользователях

# Получаем список пользователей на локальном компьютере

# Параметры:

# 1. server – целевой сервер (None означает локальный)
# 2. level – уровень детализации (0 возвращает только имена пользователей)
# 3. win32netcon.FILTER_NORMAL_ACCOUNT – фильтр, указывающий, что нужны только обычные учетные записи

users, _, _ = win32net.NetUserEnum(server, level, win32netcon.FILTER_NORMAL_ACCOUNT)

# Перебираем полученный список пользователей и выводим их имена

for user in users:
    print(user["name"])

# 🌐 Получение списка сетевых подключений:

wmi = win32com.client.GetObject("winmgmts:\\\\.\\root\\CIMV2")

# Выполняем WMI-запрос для получения списка сетевых адаптеров

# Фильтруем только те адаптеры, у которых есть NetConnectionID (т.е. они активны)

adapters = wmi.ExecQuery(
    "SELECT * FROM Win32_NetworkAdapter WHERE NetConnectionID IS NOT NULL"
)

# Перебираем найденные сетевые адаптеры и выводим их имя подключения и MAC-адрес

for adapter in adapters:
    print(f"{adapter.NetConnectionID} - {adapter.MACAddress}")

# 📁 Определение размера свободного места на диске:

_, total, free = win32api.GetDiskFreeSpaceEx("C:\\")
print(f"Свободное место: {free // (1024**3)} ГБ из {total // (1024**3)} ГБ")

# 🖥 Получение разрешения экрана:
# Получаем ширину экрана в пикселях (индекс 0)

width = win32api.GetSystemMetrics(0)

# Получаем высоту экрана в пикселях (индекс 1)

height = win32api.GetSystemMetrics(1)

# Выводим разрешение экрана в формате "ширина x высота"

print(f"Разрешение экрана: {width}x{height}")


# 🖥 Запрос информации о процессоре:


# Подключаемся к WMI для доступа к системной информации

wmi = win32com.client.GetObject("winmgmts:\\\\.\\root\\CIMV2")

# Выполняем запрос к WMI для получения данных о процессоре

cpu_info = wmi.ExecQuery("SELECT * FROM Win32_Processor")

# Перебираем все процессоры (обычно один на систему)

for cpu in cpu_info:
    # Выводим название процессора, число ядер и максимальную частоту
    print(
        f"Процессор: {cpu.Name}, Ядер: {cpu.NumberOfCores}, Частота: {cpu.MaxClockSpeed} MHz"
    )
