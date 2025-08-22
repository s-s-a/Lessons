
import scrapy
import pandas as pd
import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class BlogSpider(scrapy.Spider):
    name = 'lider-vrn'
    start_urls = ['https://lider-vrn.ru/catalog/santekhnika/']

    def __init__(self):
        super().__init__()
        self.products = []
        logging.info("Инициализация паука для сбора данных")

    def parse(self, response):
        try:
            for item_info in response.css('.item_info'):
                title = item_info.css('.item-title').xpath('./a/span/text()').get()
                if title:
                    self.products.append({'Название': title.strip()})

            next_page = response.css('a.flex-next::attr(href)').get()
            if next_page:
                yield response.follow(next_page, self.parse)

        except Exception as e:
            logging.error(f"Ошибка при парсинге: {str(e)}")

    def closed(self, reason):
        try:
            df = pd.DataFrame(self.products)
            if not df.empty:
                df.to_excel('lider_vrn_products.xlsx', index=False)
                logging.info(f"Успешно сохранено {len(df)} товаров в lider_vrn_products.xlsx")
            else:
                logging.warning("Не найдено данных для сохранения")
        except Exception as e:
            logging.error(f"Ошибка при сохранении в Excel: {str(e)}")


def main():
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Конфигурация Scrapy
    settings = get_project_settings()
    settings.update({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'LOG_LEVEL': 'INFO',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 1,
    })

    process = CrawlerProcess(settings)
    process.crawl(BlogSpider)
    process.start()


if __name__ == '__main__':
    main()
