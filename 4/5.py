
def set_ru_language():
    print("Set 'RU' language")

def set_us_language():
    print("Set 'US' language")

def set_pl_language():
    print("Set 'PL' language")

def change_language(lang_code):
    if lang_code == "RU":
        set_ru_language()
    elif lang_code == "US":
        set_us_language()
    elif lang_code == "PL":
        set_pl_language()
    else:
        raise ValueError("The system removal process begins.")

change_language("RU")
change_language("US")
change_language("PL")
change_language("MEOW")
