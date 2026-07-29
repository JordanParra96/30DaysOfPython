"""Day 22: 30 Days of python programming"""

import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup

URL = "https://www.scrapethissite.com/pages/forms/"

response = requests.get(URL, timeout=10)
content = response.content  # we get all the content from the website
soup = BeautifulSoup(
    content, "html.parser"
)  # beautiful soup will give a chance to parse
print(soup.title)  # <title>Forms | Scrape This Site ...</title>
print(soup.title.get_text())  # Forms | Scrape This Site ...
print(soup.body)  # gives the whole page on the website
print(response.status_code)

tables = soup.find_all("table", {"class": "table"})
# We are targeting the table with class attribute with the value of "table"
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0]  # the result is a list, we are taking out data from it
for th in table.find("tr").find_all("th"):
    print(th.text.strip())

# Level 1, exercise 1
# Scrape https://www.bu.edu/president/boston-university-facts-stats/
# and store the data as a JSON file.


def extract_stats(container):
    """Extract label/value pairs from a stat container.

    Handles both markups used on the page: "bu-stat-single" articles
    (title + prefix/value/suffix spans) and "li" items (label + figure spans).
    """
    stats = {}

    for stat in container.find_all("article", class_="bu-stat-single"):
        label = stat.find(class_="bu-stat-title").get_text(strip=True)
        value = stat.find(class_="bu-stat-value-container")
        stats[label] = "".join(value.stripped_strings)

    for item in container.find_all("li"):
        label = item.find(class_="stat-label").get_text(strip=True)
        value = item.find(class_="stat-figure")
        stats[label] = "".join(value.stripped_strings)

    return stats


def scrape_facts_and_stats(page_url):
    """Scrape the BU facts & stats page and return the data grouped by section."""
    page = requests.get(page_url, timeout=10)
    facts_soup = BeautifulSoup(page.content, "html.parser")

    stats_by_group = {}
    for group_title in facts_soup.find_all("h4", class_="stat-group-title"):
        group_name = group_title.get_text(strip=True)
        container = group_title.find_next_sibling()
        stats_by_group[group_name] = extract_stats(container)

    return stats_by_group


facts_and_stats = scrape_facts_and_stats(
    "https://www.bu.edu/president/boston-university-facts-stats/"
)

json_path = Path(__file__).parent / "bu_facts_and_stats.json"
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(facts_and_stats, json_file, indent=2, ensure_ascii=False)

print(json.dumps(facts_and_stats, indent=2, ensure_ascii=False))
