from playsound import *
from datetime import *

def validate_time(alarm_time: str)-> str|None:

    try:
        return datetime.strptime(alarm_time, '%H:%M:%S').time()
    except ValueError:
        return None


while True:
    alarm_time_str:str = input('Введите время в следущем формате: ЧЧ:ММ:СС')
    alarm_time:time = validate_time(alarm_time_str)
    print('Неверный формат, попробуйте еще раз.' if alarm_time == None else f'Будильник установлен на время {alarm_time}...')

while datetime.now().time() < alarm_time:
    pass

print('Вставай!')
playsound('.mp3')