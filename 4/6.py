def set_ru_language():
    print("Set 'RU' language")

def set_us_language():
    print("Set 'US' language")

def set_pl_language():
    print("Set 'PL' language")

langs = {
    "RU": set_ru_language,
    "US": set_us_language,
    "PL": set_pl_language,
}

def change_language(lang_code):
    if func := langs.get(lang_code):
        func()
    else:
        raise ValueError("The system removal process begins.")

change_language("RU")
change_language("US")
change_language("PL")
change_language("MEOW")
