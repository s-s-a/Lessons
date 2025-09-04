import calendar
import matplotlib.pyplot as plt
from datetime import datetime


def draw_beautiful_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    # Увеличиваем размер фигуры
    fig, ax = plt.subplots(figsize=(10, 8))
    # Заголовок
    ax.set_title(f"{calendar.month_name[month]} {year}", fontsize=20, pad=20)

    # Заголовки дней недели
    weekdays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

    # Создаём таблицу
    table = ax.table(cellText=cal,
                     colLabels=weekdays,
                     loc='center',
                     cellLoc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(14)  # Размер шрифта для дней

    # Настраиваем ячейки
    for (i, j), cell in table._cells.items():
        cell.set_height(0.1)  # Высота ячейки
        cell.set_edgecolor('black')  # Цвет границы ячейки
        cell.set_linewidth(1)  # Толщина границы

        # Цвет для заголовков дней недели
        if i == 0:
            cell.set_facecolor('#ADD8E6')  # Светло-синий для заголовков
            cell.set_fontsize(16)
            cell.set_text_props(weight='bold')  # Жирный шрифт для заголовков
        else:
            day_value = cal[i - 1][j]
            if day_value != 0:  # Пропускаем пустые ячейки (дни из других месяцев)
                # Выделение выходных дней
                if j >= 5:  # Суббота и Воскресенье
                    cell.set_facecolor('#FFDDC1')  # Светло-оранжевый для выходных
                else:
                    cell.set_facecolor('#F0F8FF')  # Светло-голубой для будней

                # Выделение текущего дня
                now = datetime.now()
                if year == now.year and month == now.month and day_value == now.day:
                    cell.set_facecolor('#FF6347')  # Ярко-красный для текущего дня
                    cell.set_text_props(color='white', weight='bold')  # Белый жирный текст

    ax.axis('off')  # Убираем оси

    plt.savefig(f"calendar_{year}_{month}.png", bbox_inches='tight', dpi=300)
    print(f"Календарь сохранён.")


if __name__ == "__main__":
    # Запрос данных у пользователя
    y = int(input("Введите год: "))
    m = int(input("Введите номер месяца (1-12): "))
    draw_beautiful_calendar(y, m)