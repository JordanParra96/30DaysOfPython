"""Day 22: 30 Days of python programming"""

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
