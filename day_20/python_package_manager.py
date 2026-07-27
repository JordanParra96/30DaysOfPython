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

# Exercise 1
ROMEO_AND_JULIET_URL = "https://www.gutenberg.org/cache/epub/1112/pg1112.txt"


def get_text_from_url(book_url):
    """Download the text found at the given url."""
    text_response = requests.get(book_url, timeout=10)
    return text_response.text


def get_clean_words(text):
    """Split text into lowercase words, keeping only letters in each word."""
    clean_words = []
    for word in text.lower().split():
        clean_word = ""
        for character in word:
            if character.isalpha():
                clean_word += character
        if clean_word != "":
            clean_words.append(clean_word)
    return clean_words


def count_word_frequency(words):
    """Count how many times each word appears in a list of words."""
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency


def get_most_common_words(word_frequency, amount):
    """Return the `amount` most frequent (word, count) pairs, highest first."""
    most_common_words = []
    for _ in range(amount):
        most_frequent_word = None
        highest_count = 0
        already_picked = [pair[0] for pair in most_common_words]
        for word, count in word_frequency.items():
            if word not in already_picked and count > highest_count:
                most_frequent_word = word
                highest_count = count
        most_common_words.append((most_frequent_word, highest_count))
    return most_common_words


romeo_and_juliet = get_text_from_url(ROMEO_AND_JULIET_URL)
words_in_book = get_clean_words(romeo_and_juliet)
word_frequency_in_book = count_word_frequency(words_in_book)
top_10_words = get_most_common_words(word_frequency_in_book, 10)

print(top_10_words)
