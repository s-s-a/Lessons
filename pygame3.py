# Прокачиваем игру на Python c уворачиванием от предметов
# https://thecode.media/prokachivaem-igru-na-python-c-uvorachivaniem-ot-predmetov/

# импортируем зависимости и дополнительные модули
import pygame
from sys import exit
import time

# включаем модуль pygame
pygame.init()

# объявляем ширину и высоту экрана
width = 800
height = 400
# создаём экран игры
screen = pygame.display.set_mode((width, height))
# устанавливаем количество кадров в секунду
fps = 60
# создаём объект таймера
clock = pygame.time.Clock()

# добавляем счётчики для подсчёта времени в игре — это будут наши очки
start_time = 0
final_score = 0

# загружаем в переменные картинки из папки с нашим файлом
back_main_screen = pygame.image.load("code_game_back.jpg").convert()
back = pygame.image.load("code_game_back_floor.jpg").convert()
hero = pygame.image.load("detective.png").convert_alpha()
pot = pygame.image.load("teapot.png").convert_alpha()
candle = pygame.image.load("candlestick.png").convert_alpha()
box = pygame.image.load("wooden_box.png").convert_alpha()

# даём название окну игры
pygame.display.set_caption("Detective CODE Game")

# объявляем переменную-флаг для цикла игры
game = False

# создаём объекты текста: в первой строчке задаём настройки шрифта,
# во второй сам текст и его цвет, в третьей — помещаем текст
# в прямоугольную рамку и размещаем на заданных координатах

# текст с названием игры
text_font = pygame.font.Font("prstartk.ttf", 15)
text_surface = text_font.render("Detective CODE Game", False, "White")
text_name_rect = text_surface.get_rect(center=(400, 30))

# текст с сообщением о столкновении
text_font_collide = pygame.font.Font("prstartk.ttf", 50)
text_collide = text_font_collide.render("CoLLiDE!!", False, "Red")
text_collide_rect = text_collide.get_rect(center=(400, 200))

# текст главного меню
text_font_new_game = pygame.font.Font("prstartk.ttf", 20)
text_newgame_str1 = text_font_new_game.render("If you want to start,", False, "Green")
text_newgame_rect1 = text_newgame_str1.get_rect(center=(400, 325))
text_newgame_str2 = text_font_new_game.render("press space", False, "Green")
text_newgame_rect2 = text_newgame_str2.get_rect(center=(400, 350))

# текст для подсчёта очков
text_font_score = pygame.font.Font("prstartk.ttf", 15)
# текст для вывода очков при окончании игры
text_ts_font = pygame.font.Font("prstartk.ttf", 20)


# функция подсчёта очков
def display_score():
    # получаем время текущей игры: от общего времени в игре мы
    # отнимаем время, сыгранное за время запуска скрипта
    current_time = pygame.time.get_ticks() - start_time
    # создаём объект текста количества очков — сыгранное время
    score_surface = text_font_score.render(f"{current_time}", False, "Purple")
    # помещаем текст с количеством очков в прямоугольник
    score_rect = score_surface.get_rect(bottomright=(795, 395))
    # размещаем прямоугольник на поверхности
    screen.blit(score_surface, score_rect)


# Функция для сброса начальных параметров
def reset_game():
    # делаем видимыми переменные: объекты всех видимых моделей,
    # отметки о движении предметов и главный флаг запущенной игры
    global hero_rect, pot_rect, candle_rect, box_rect, pot_flag, box_flag, game

    # объявляем начальные координаты для всех объектов
    hero_x_pos = 75
    hero_y_pos = 180
    candle_x_pos = 900
    candle_y_pos = 70
    box_x_pos = 900
    box_y_pos = 200
    pot_x_pos = 900
    pot_y_pos = 345

    # создаём рамки прямоугольников
    hero_rect = hero.get_rect(center=(hero_x_pos, hero_y_pos))
    pot_rect = pot.get_rect(center=(pot_x_pos, pot_y_pos))
    candle_rect = candle.get_rect(center=(candle_x_pos, candle_y_pos))
    box_rect = box.get_rect(center=(box_x_pos, box_y_pos))

    # сбрасываем флаги и состояние игры
    pot_flag = False
    box_flag = False


# запускаем функцию начального состояния игры
reset_game()

# запускаем бесконечный цикл
while True:
    # получаем список возможных действий игрока
    for event in pygame.event.get():
        # если пользователь нажал на крестик закрытия окна
        if event.type == pygame.QUIT:
            # выключаем цикл
            pygame.quit()
            # добавляем корректное завершение работы
            exit()

        # если флаг игры неактивен (игра окончена), при этом нажата клавиша пробела:
        if not game and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # то сбрасываем состояние игры до начального состояния...
            reset_game()
            # устанавливаем флаг игры на активный (запущена)...
            game = True
            # и получаем общее отыгранное время
            start_time = pygame.time.get_ticks()

    # если флаг игры активен (запущена)
    if game:
        # получаем список всех зажатых клавиш
        keys = pygame.key.get_pressed()
        # если зажата клавиша вверх, двигаем игрока вверх
        if keys[pygame.K_UP]:
            hero_rect.top -= 5
            # если модель игрока достигла верхней границы, останавливаем движение
            if hero_rect.top <= 0:
                hero_rect.top = 0
        # если зажата клавиша вниз, двигаем игрока вниз
        if keys[pygame.K_DOWN]:
            hero_rect.top += 5
            # если модель игрока достигла нижней границы, останавливаем движение
            if hero_rect.bottom >= 400:
                hero_rect.bottom = 400

        # размещаем все поверхности на главном экране
        screen.blit(back, (0, 0))
        screen.blit(hero, hero_rect)
        screen.blit(candle, candle_rect)
        screen.blit(box, box_rect)
        screen.blit(pot, pot_rect)
        back.blit(text_surface, text_name_rect)

        # запускаем движение всех предметов
        candle_rect.left -= 4
        # когда подсвечник пересёк половину экрана,
        # меняем сигнальную переменную для чайника и начинаем его движение
        if candle_rect.left <= 400:
            pot_flag = True
        if pot_flag:
            pot_rect.left -= 4

        # когда чайник пересёк половину экрана,
        # меняем сигнальную переменную для ящика и начинаем его движение
        if pot_rect.left <= 400:
            box_flag = True
        if box_flag:
            box_rect.left -= 4

        # обнуляем начальные координаты, когда правая грань
        # скрылась за границей экрана
        if candle_rect.right <= 0:
            candle_rect.left = 800
        if pot_rect.right <= 0:
            pot_rect.left = 800
        if box_rect.right <= 0:
            box_rect.left = 1000

        # если модель игрока столкнулась с одним из предметов...
        if (
            hero_rect.colliderect(candle_rect)
            or hero_rect.colliderect(pot_rect)
            or hero_rect.colliderect(box_rect)
        ):

            # то выводим сообщение о столкновении
            screen.blit(text_collide, text_collide_rect)
            # вычисляем общее время последней игры в секундах
            final_score = (pygame.time.get_ticks() - start_time) // 1000
            # создаём объект текста с выводом количества очков
            text_ts_text = text_ts_font.render(
                f"Total time: {final_score} sec", False, "White"
            )
            # помещаем текст в прямоугольник
            text_ts_rect = text_ts_text.get_rect(center=(400, 250))
            # размещаем прямоугольник текста на главном экране
            screen.blit(text_ts_text, text_ts_rect)

            # обновляем экран, чтобы появилось сообщение
            # об окончании игры после столкновения
            pygame.display.flip()
            # делаем паузу в 3 секунды
            time.sleep(3)
            # переставляем флаг игры в неактивный (окончена)
            game = False

        # выводим на экран финальные очки
        display_score()

    # если флаг игры не активен (окончена):
    else:
        # выводим на экран фон главного окна игры
        screen.blit(back_main_screen, (0, 0))
        # и чёрную плашку-прямоугольник, поверх которой разместим текст
        pygame.draw.rect(back_main_screen, "Black", (100, 300, 600, 80))
        # выводим на экран две строки текста с предложением начать игру
        screen.blit(text_newgame_str1, text_newgame_rect1)
        screen.blit(text_newgame_str2, text_newgame_rect2)

    # обновляем экран игры
    pygame.display.update()
    # добавляем к таймеру количество fps для частоты обновления основного цикла
    clock.tick(fps)
