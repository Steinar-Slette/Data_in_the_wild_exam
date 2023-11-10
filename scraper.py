import os
from time import sleep
from random import randint
from newspaper import Config
from newspaper import Source
import newspaper

# Delete this stuff to clear cache
# /private/var/folders/sh/fjb1r_5j6gxcy4lzfcc4_4zr0000gn/T/.newspaper_scraper


config = Config()
config.request_timeout = 10


# def forget_articles(url):
#     domain = url.replace("https://", "http://").replace("http://", "").split("/")[0]
#     d_pth = os.path.join(newspaper.settings.MEMO_DIR, domain + ".txt")
#     print(d_pth)
#     if os.path.exists(d_pth):
#         os.remove(d_pth)


# oldUrl = "http://web.archive.org/web/20231009112318/https://news.sky.com/"
# forget_articles(oldUrl)

cnbc_wayback_archive = Source(
    url="http://web.archive.org/web/20221109120216/http://news.sky.com/",
    config=config,
    memoize_articles=False,
    language="en",
    number_threads=20,
    thread_timeout_seconds=2,
)


cnbc_wayback_archive.build()
print(cnbc_wayback_archive.size())
for article in cnbc_wayback_archive.articles:
    article.download()
    article.parse()
    article_meta_data = article.meta_data

    print(article.publish_date)
    print(article.title)

    article_description = "".join(
        {value for (key, value) in article_meta_data.items() if key == "description"}
    )
    print(article_description)

    article_keywords = {
        value for (key, value) in article_meta_data.items() if key == "keywords"
    }
    print(list(article_keywords))

    print(article.url)

    # this sleep timer is helping with some timeout issues
    # that happened when querying
    sleep(randint(1, 5))
