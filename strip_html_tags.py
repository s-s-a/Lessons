# Код для очистки текста от html-тегов на Python

# Для удаления html-тегов в коде используется библиотека beautifulsoup4.


from bs4 import BeautifulSoup


def strip_html_tags(html_content: str) -> str:
    """
    Удаляет все HTML-теги из строки и возвращает чистый текст.

    Args:
        html_content (str): Строка, содержащая HTML-разметку.

    Returns:
        str: Текст без HTML-тегов.
    """
    if not html_content:
        return ""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text(separator=' ', strip=True)
    except Exception as e:
        print(f"Ошибка при очистке HTML: {e}")
        return html_content


if __name__ == "__main__":
    html_example = "<p>Это <b>пример</b> текста с <i>HTML</i> тегами.</p>"
    clean_text = strip_html_tags(html_example)
    print(f"Исходный HTML: '{html_example}'")
    print(f"Чистый текст: '{clean_text}'")
