import yagooglesearch
import csv
from random import randint
from time import sleep

# query = "site:github.com"
query_array = [
    "производство пластиковых карт",
    "печать пластиковых карт",
    "изготовить пластиковые карты",
    "напечатать пластиковые карты",
    "сделать пластиковые карты",
    "производство дисконтных карт",
    "печать дисконтных карт",
    "изготовить дисконтных карты",
    "напечатать дисконтных карты",
    "сделать дисконтных карты",
]

for query in query_array:
    client = yagooglesearch.SearchClient(
        query,
        tbs="li:1",
        num=30,
        max_search_result_urls_to_return=30,
        http_429_cool_off_time_in_minutes=45,
        http_429_cool_off_factor=1.5,
        # proxy="socks5h://127.0.0.1:9050",
        verbosity=5,
        verbose_output=True,  # False (only URLs) or True (rank, title, description, and URL)
    )
    client.assign_random_user_agent()

    urls = client.search()
    len(urls)

    with open(f"{query}.csv","w", newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';', dialect='excel')
        for url in urls:
            print(url["title"])
            csv_writer.writerow([
                url["rank"],
                url["title"],
                url["url"],
            ])

    sleep(randint(2,9))