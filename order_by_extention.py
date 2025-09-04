<<<<<<< HEAD
# Êîä äëÿ óïîðÿäî÷èâàíèÿ ôàéëîâ ïî äèðåêòîðèÿì â çàâèñèìîñòè îò èõ ðàñøèðåíèÿ íà Python
from pathlib import Path


# Ñîçäàåì ïàïêè äëÿ êàæäîãî ðàñøèðåíèÿ ôàéëà
def create_folders(folder_path):
    # Ïîëó÷àåì ñïèñîê âñåõ ôàéëîâ â ïàïêå
    files = folder_path.iterdir()

    # Ïðîõîäèìñÿ ïî êàæäîìó ôàéëó è ñîçäàåì ïàïêè ïî ðàñøèðåíèÿì
=======
# ÐšÐ¾Ð´ Ð´Ð»Ñ ÑƒÐ¿Ð¾Ñ€ÑÐ´Ð¾Ñ‡Ð¸Ð²Ð°Ð½Ð¸Ñ Ñ„Ð°Ð¹Ð»Ð¾Ð² Ð¿Ð¾ Ð´Ð¸Ñ€ÐµÐºÑ‚Ð¾Ñ€Ð¸ÑÐ¼ Ð² Ð·Ð°Ð²Ð¸ÑÐ¸Ð¼Ð¾ÑÑ‚Ð¸ Ð¾Ñ‚ Ð¸Ñ… Ñ€Ð°ÑÑˆÐ¸Ñ€ÐµÐ½Ð¸Ñ Ð½Ð° Python
from pathlib import Path


# Ð¡Ð¾Ð·Ð´Ð°ÐµÐ¼ Ð¿Ð°Ð¿ÐºÐ¸ Ð´Ð»Ñ ÐºÐ°Ð¶Ð´Ð¾Ð³Ð¾ Ñ€Ð°ÑÑˆÐ¸Ñ€ÐµÐ½Ð¸Ñ Ñ„Ð°Ð¹Ð»Ð°
def create_folders(folder_path):
    # ÐŸÐ¾Ð»ÑƒÑ‡Ð°ÐµÐ¼ ÑÐ¿Ð¸ÑÐ¾Ðº Ð²ÑÐµÑ… Ñ„Ð°Ð¹Ð»Ð¾Ð² Ð² Ð¿Ð°Ð¿ÐºÐµ
    files = folder_path.iterdir()

    # ÐŸÑ€Ð¾Ñ…Ð¾Ð´Ð¸Ð¼ÑÑ Ð¿Ð¾ ÐºÐ°Ð¶Ð´Ð¾Ð¼Ñƒ Ñ„Ð°Ð¹Ð»Ñƒ Ð¸ ÑÐ¾Ð·Ð´Ð°ÐµÐ¼ Ð¿Ð°Ð¿ÐºÐ¸ Ð¿Ð¾ Ñ€Ð°ÑÑˆÐ¸Ñ€ÐµÐ½Ð¸ÑÐ¼
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
    for file in files:
        if file.is_file():
            file_extension = file.suffix
            folder_name = file_extension[1:]
            folder_path_new = folder_path / folder_name

<<<<<<< HEAD
            # Ïðîâåðÿåì, ñóùåñòâóåò ëè ïàïêà äëÿ äàííîãî ðàñøèðåíèÿ
=======
            # ÐŸÑ€Ð¾Ð²ÐµÑ€ÑÐµÐ¼, ÑÑƒÑ‰ÐµÑÑ‚Ð²ÑƒÐµÑ‚ Ð»Ð¸ Ð¿Ð°Ð¿ÐºÐ° Ð´Ð»Ñ Ð´Ð°Ð½Ð½Ð¾Ð³Ð¾ Ñ€Ð°ÑÑˆÐ¸Ñ€ÐµÐ½Ð¸Ñ
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
            if not folder_path_new.exists():
                folder_path_new.mkdir(parents=True)


<<<<<<< HEAD
# Ïåðåìåùàåì ôàéëû â ñîîòâåòñòâóþùèå ïàïêè
def move_files(folder_path):
    create_folders(folder_path)
    # Ïîëó÷àåì ñïèñîê âñåõ ôàéëîâ â ïàïêå
    files = folder_path.iterdir()

    # Ïðîõîäèìñÿ ïî êàæäîìó ôàéëó è ïåðåìåùàåì åãî â ñîîòâåòñòâóþùóþ ïàïêó
=======
# ÐŸÐµÑ€ÐµÐ¼ÐµÑ‰Ð°ÐµÐ¼ Ñ„Ð°Ð¹Ð»Ñ‹ Ð² ÑÐ¾Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÑƒÑŽÑ‰Ð¸Ðµ Ð¿Ð°Ð¿ÐºÐ¸
def move_files(folder_path):
    create_folders(folder_path)
    # ÐŸÐ¾Ð»ÑƒÑ‡Ð°ÐµÐ¼ ÑÐ¿Ð¸ÑÐ¾Ðº Ð²ÑÐµÑ… Ñ„Ð°Ð¹Ð»Ð¾Ð² Ð² Ð¿Ð°Ð¿ÐºÐµ
    files = folder_path.iterdir()

    # ÐŸÑ€Ð¾Ñ…Ð¾Ð´Ð¸Ð¼ÑÑ Ð¿Ð¾ ÐºÐ°Ð¶Ð´Ð¾Ð¼Ñƒ Ñ„Ð°Ð¹Ð»Ñƒ Ð¸ Ð¿ÐµÑ€ÐµÐ¼ÐµÑ‰Ð°ÐµÐ¼ ÐµÐ³Ð¾ Ð² ÑÐ¾Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÑƒÑŽÑ‰ÑƒÑŽ Ð¿Ð°Ð¿ÐºÑƒ
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
    for file in files:
        if file.is_file():
            file_extension = file.suffix
            folder_name = file_extension[1:]
            folder_path_new = folder_path / folder_name
            file_path_new = folder_path_new / file.name

<<<<<<< HEAD
            # Ïåðåìåùàåì ôàéë â ñîîòâåòñòâóþùóþ ïàïêó
=======
            # ÐŸÐµÑ€ÐµÐ¼ÐµÑ‰Ð°ÐµÐ¼ Ñ„Ð°Ð¹Ð» Ð² ÑÐ¾Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÑƒÑŽÑ‰ÑƒÑŽ Ð¿Ð°Ð¿ÐºÑƒ
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
            file.rename(file_path_new)


move_files(Path(r'C:\Users\admin\pythonProject\files'))
