# Example of a program that scrapes data from a table with sunrise and sunset times for given dates
# the scraping program is parametrized by month and year
# the second part calculates duration of the date using the datetime module

import requests
from datetime import datetime
from bs4 import BeautifulSoup

def scrape_slunce(month, year):
    url = (
        "https://www.in-pocasi.cz/predpoved-pocasi/cz/praha/praha-324/astro/"
        f"?kalendar=slunce&mesic={month}&rok={year}"
    )

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table", class_="table-data")
    if table and table.tbody:
        rows = table.tbody.find_all("tr")
    else:
        rows = []

    return [
        (
            r.find_all("td")[0].text.strip(),
            r.find_all("td")[1].text.strip(),
            r.find_all("td")[2].text.strip(),
        )
        for r in rows
    ]

# strptime = string parse time (parses a string to time object)
def elapsed(entry : tuple[str,str,str], year, month):
    day, start, end = entry
    day = day.split(".")[0]
    t0 = datetime.strptime(f"{year}-{month:02d}-{day} {start}", "%Y-%m-%d %H:%M")
    t1 = datetime.strptime(f"{year}-{month:02d}-{day} {end}",   "%Y-%m-%d %H:%M")
    return str(t1 - t0)

year = 2023
month = 2
data = scrape_slunce(month,year)

DATE = "datum"
VYCHOD = "východ"
ZAPAD = "západ"
DEN = "délka"
print(f"{DATE:^8} | {VYCHOD:^7} | {ZAPAD:^7} | {DEN:^8}")
print(f"{"slunce":-^39}")
for line in data:
    print(f"{line[0]:>8} | {line[1]:^7} | {line[2]:^7} | {elapsed(line,year,month):>8}")