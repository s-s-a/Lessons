# на версии selectolax 0.4.0 не работает, ругается:
#  No module named 'selectolax.lexbor'; 'selectolax' is not a package
from pprint import pprint

from httpx import Client
# from selectolax.parser import HTMLParser
from selectolax.lexbor import LexborHTMLParser as HTMLParser

URL = "https://habr.com/ru/articles/"
ARTICLES_LIST = ".tm-page__main_has-sidebar.tm-page__main"
ARTICLE_ELEMENT = ".tm-article-snippet.tm-article-snippet"
POST_AUTHOR_ELEMENT = ".tm-user-info__username"
POST_LINK_ELEMENT = ".tm-title__link"
POST_SNIPPET_ELEMENT = ".article-formatted-body.article-formatted-body.article-formatted-body_version-2"


def parse_articles() -> dict[int, dict[str, str]]:
    articles = {}

    response = Client().get(url=URL)

    tree: HTMLParser = HTMLParser(html=response.text)

    articles_list = tree.css_first(ARTICLES_LIST)

    for num, article in enumerate(articles_list.css(ARTICLE_ELEMENT), start=1):
        author = article.css_first(POST_AUTHOR_ELEMENT)
        author_name = author.text()
        author_link = author.attributes.get("href")

        post = article.css_first(POST_LINK_ELEMENT)
        post_title = post.text()
        post_link = post.attributes.get("href")

        post_snippet = article.css_first(POST_SNIPPET_ELEMENT).text()

        articles[num] = {
            "author": author_name,
            "author_link": author_link,
            "post_title": post_title,
            "post_link": post_link,
            "post_snippet": post_snippet,
        }

    return articles


if __name__ == "__main__":
    pprint(parse_articles())
