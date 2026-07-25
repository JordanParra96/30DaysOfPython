"""Day 20: 30 Days of python programming"""

# Example importing a module
import webbrowser  # web browser module to open websites
import requests  # importing the request module

# list of urls: python
url_lists = [
    "http://www.python.org",
    "https://www.linkedin.com/in/asabeneh/",
    "https://github.com/Asabeneh",
    "https://twitter.com/Asabeneh",
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)

# Example importing requests module

URL = "https://www.w3.org/TR/PNG/iso_8859-1.txt"  # text from a website

response = requests.get(URL, timeout=10)  # opening a network and fetching a data
print(response)
print(response.status_code)  # status code, success:200
print(response.headers)  # headers information
print(response.text)  # gives all the text from the page

API_URL = "https://www.apicountries.com/countries"  # countries api
api_response = requests.get(
    API_URL, timeout=10
)  # opening a network and fetching a data
print(api_response)  # esponse object
print(api_response.status_code)  # status code, success:200
countries = api_response.json()
print(
    countries[:1]
)  # we sliced only the first country, remove the slicing to see all countries
