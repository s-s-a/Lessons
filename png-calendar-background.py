import calendar
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
from datetime import datetime
from PIL import Image


def draw_beautiful_calendar(year, month, background_image_path=None):
    cal = calendar.monthcalendar(year, month)
    fig, ax = plt.subplots(figsize=(12, 10), dpi=300)
    title = ax.set_title(f"{calendar.month_name[month]} {year}", fontsize=38, pad=20, color='black')

    # Добавляем белую обводку к тексту
    title.set_path_effects([
        path_effects.Stroke(linewidth=3, foreground='white'),  # Толщина и цвет обводки
        path_effects.Normal()
    ])

    # Добавляем фоновое изображение, если путь указан
    if background_image_path:
        try:
            img = Image.open(background_image_path)

            # Масштабируем изображение до размера всей фигуры
            fig_width, fig_height = fig.get_size_inches()
            dpi = fig.get_dpi()
            width_px, height_px = int(fig_width * dpi), int(fig_height * dpi)
            img = img.resize((width_px, height_px))
            fig.figimage(img, xo=0, yo=0, zorder=-1)
        except FileNotFoundError:
            print(f"Ошибка: Файл изображения не найден по пути: {background_image_path}")
        except Exception as e:
            print(f"Произошла ошибка при загрузке изображения: {e}")

    # Заголовки дней недели
    day_names = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

    # Создаем таблицу
    table = ax.table(cellText=cal,
                     colLabels=day_names,
                     loc='center',
                     cellLoc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(16)

    for (i, j), cell in table._cells.items():
        cell.set_height(0.12)
        cell.set_edgecolor('black')
        cell.set_linewidth(1.5)
        cell.set_alpha(0.8)

        if i == 0:
            cell.set_facecolor('#87CEEB')
            cell.set_fontsize(18)
            cell.set_text_props(weight='bold', color='white')
        else:
            day_value = cal[i - 1][j]
            if day_value != 0:
                if j >= 5:
                    cell.set_facecolor('#FFB6C1')
                else:
                    cell.set_facecolor('#E0FFFF')

                now = datetime.now()
                if year == now.year and month == now.month and day_value == now.day:
                    cell.set_facecolor('#FF4500')
                    cell.set_text_props(color='white', weight='bold')

    ax.axis('off')

    # Сохраняем без обрезки, с прозрачным фоном
    plt.savefig(f"calendar_{year}_{month}.png", dpi=300, facecolor='none')
    print(f"Календарь сохранён.")


# Запрос данных
y = int(input("Введите год: "))
m = int(input("Введите номер месяца (1-12): "))
bg_path = input("Введите путь к фоновому изображению (или нажмите Enter, чтобы пропустить): ")

if bg_path:
    draw_beautiful_calendar(y, m, background_image_path=bg_path)
else:
    draw_beautiful_calendar(y, m)
