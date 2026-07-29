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

# Exercise 2


def scrape_uci_datasets_table(page_url):
    """Scrape the UCI ML Repository datasets table and return a list of dataset records."""
    page = requests.get(page_url, timeout=10)
    datasets_soup = BeautifulSoup(page.content, "html.parser")

    header_row = datasets_soup.find("tr", attrs={"bgcolor": "#003366"})
    dataset_table = header_row.find_parent("table")
    rows = dataset_table.find_all("tr", recursive=False)
    headers = [cell.get_text(strip=True) for cell in rows[0].find_all("td")]

    datasets = []
    for row in rows[1:]:
        cells = row.find_all("td", recursive=False)
        name = cells[0].find("b").get_text(strip=True)
        values = [name] + [cell.get_text(strip=True) for cell in cells[1:]]
        datasets.append(dict(zip(headers, values)))

    return datasets


uci_datasets = scrape_uci_datasets_table(
    "http://web.archive.org/web/20210506224749/"
    "http://archive.ics.uci.edu/ml/datasets.php"
    "?format=&task=reg&att=&area=&numAtt=&numIns=&type=&sort=nameUp&view=table"
)

uci_json_path = Path(__file__).parent / "uci_datasets.json"
with open(uci_json_path, "w", encoding="utf-8") as json_file:
    json.dump(uci_datasets, json_file, indent=2, ensure_ascii=False)

print(f"Scraped {len(uci_datasets)} datasets")
print(json.dumps(uci_datasets[:3], indent=2, ensure_ascii=False))

# Exercise 3


def get_cell_text(cell):
    """Return a table cell's text, stripped of footnote markers, using
    an image's alt text when the cell only contains a portrait."""
    for footnote in cell.find_all("sup"):
        footnote.decompose()
    image = cell.find("img")
    if image and image.get("alt"):
        return image["alt"].strip()
    return cell.get_text(" ", strip=True)


def get_table_headers(header_row):
    """Expand header cells by their colspan so they line up with data columns."""
    headers = []
    for header_cell in header_row.find_all("th"):
        for footnote in header_cell.find_all("sup"):
            footnote.decompose()
        label = header_cell.get_text(" ", strip=True)
        headers.extend([label] * int(header_cell.get("colspan", 1)))
    return headers


def flatten_row(row, num_cols, pending):
    """Fill in a table row's values, resolving rowspans carried from previous rows."""
    cells = iter(row.find_all(["td", "th"]))
    current_cell = next(cells, None)
    values = [None] * num_cols
    col = 0
    while col < num_cols:
        if col in pending:
            remaining, text = pending[col]
            values[col] = text
            pending[col] = [remaining - 1, text]
            if pending[col][0] == 0:
                del pending[col]
            col += 1
            continue
        if current_cell is None:
            break
        text = get_cell_text(current_cell)
        colspan = int(current_cell.get("colspan", 1))
        rowspan = int(current_cell.get("rowspan", 1))
        for offset in range(colspan):
            values[col + offset] = text
            if rowspan > 1:
                pending[col + offset] = [rowspan - 1, text]
        col += colspan
        current_cell = next(cells, None)
    return values


def scrape_presidents_table(page_url):
    """Scrape the Wikipedia presidents table into a list of records, one per
    election term, resolving rowspans/colspans by carrying cells forward."""
    # Wikimedia's robot policy rejects requests without an identifying User-Agent.
    request_headers = {
        "User-Agent": "30DaysOfPython-exercise/1.0 (https://github.com/JordanParra96)"
    }
    page = requests.get(page_url, headers=request_headers, timeout=10)
    presidents_soup = BeautifulSoup(page.content, "html.parser")
    presidents_table = presidents_soup.find("table", class_="wikitable")

    rows = presidents_table.find_all("tr")
    column_headers = get_table_headers(rows[0])

    pending = {}  # column index -> [rows remaining, carried-over text]
    presidents = []
    for row in rows[1:]:
        values = flatten_row(row, len(column_headers), pending)
        presidents.append(dict(zip(column_headers, values)))

    return presidents


presidents_data = scrape_presidents_table(
    "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
)

presidents_json_path = Path(__file__).parent / "presidents.json"
with open(presidents_json_path, "w", encoding="utf-8") as json_file:
    json.dump(presidents_data, json_file, indent=2, ensure_ascii=False)

print(f"Scraped {len(presidents_data)} president terms")
print(json.dumps(presidents_data[:2], indent=2, ensure_ascii=False))
