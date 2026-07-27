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

# Exercise 2
CATS_API_URL = "https://api.thecatapi.com/v1/breeds"


def get_cats(cats_url):
    """Download the list of cat breeds from the given API url."""
    cats_response = requests.get(cats_url, timeout=10)
    return cats_response.json()


def get_average_from_range(range_text):
    """Turn a range like '3 - 5' into its average, e.g. 4.0."""
    low, high = range_text.split("-")
    return (float(low) + float(high)) / 2


def get_weights(cats):
    """Return the average metric weight (kg) of every cat breed."""
    weights = []
    for cat in cats:
        weights.append(get_average_from_range(cat["weight"]["metric"]))
    return weights


def get_lifespans(cats):
    """Return the average lifespan (years) of every cat breed."""
    lifespans = []
    for cat in cats:
        lifespans.append(get_average_from_range(cat["life_span"]))
    return lifespans


def calculate_mean(values):
    """Return the average of a list of numbers."""
    return sum(values) / len(values)


def calculate_median(values):
    """Return the middle value of a list of numbers."""
    sorted_values = sorted(values)
    middle = len(sorted_values) // 2
    if len(sorted_values) % 2 == 0:
        return (sorted_values[middle - 1] + sorted_values[middle]) / 2
    return sorted_values[middle]


def calculate_standard_deviation(values):
    """Return the population standard deviation of a list of numbers."""
    mean = calculate_mean(values)
    squared_differences = []
    for value in values:
        squared_differences.append((value - mean) ** 2)
    variance = calculate_mean(squared_differences)
    return variance**0.5


def print_statistics(label, values):
    """Print min, max, mean, median and standard deviation for a list of numbers."""
    print(f"{label}:")
    print(f"  min: {min(values):.2f}")
    print(f"  max: {max(values):.2f}")
    print(f"  mean: {calculate_mean(values):.2f}")
    print(f"  median: {calculate_median(values):.2f}")
    print(f"  standard deviation: {calculate_standard_deviation(values):.2f}")


def build_frequency_table(items):
    """Count how many times each item appears in a list."""
    frequency_table = {}
    for item in items:
        if item in frequency_table:
            frequency_table[item] += 1
        else:
            frequency_table[item] = 1
    return frequency_table


cat_breeds = get_cats(CATS_API_URL)

cat_weights = get_weights(cat_breeds)
cat_lifespans = get_lifespans(cat_breeds)
print_statistics("Weight in kg", cat_weights)
print_statistics("Lifespan in years", cat_lifespans)

country_frequency = build_frequency_table([cat["origin"] for cat in cat_breeds])
breed_frequency = build_frequency_table([cat["name"] for cat in cat_breeds])
print("Country frequency:", country_frequency)
print("Breed frequency:", breed_frequency)

# Exercise 3
COUNTRIES_API_URL = "https://www.apicountries.com/countries"


def get_countries(countries_url):
    """Download the list of countries from the given API url."""
    countries_response = requests.get(countries_url, timeout=10)
    return countries_response.json()


def get_top_n(pairs, amount):
    """Return the `amount` (label, value) pairs with the highest value, highest first."""
    top_pairs = []
    for _ in range(amount):
        best_label = None
        highest_value = 0
        already_picked = [pair[0] for pair in top_pairs]
        for label, value in pairs:
            if label not in already_picked and value > highest_value:
                best_label = label
                highest_value = value
        top_pairs.append((best_label, highest_value))
    return top_pairs


def get_country_areas(countries):
    """Return (name, area) pairs for every country that has a known area."""
    country_areas = []
    for country in countries:
        area = country.get("area")
        if area is not None:
            country_areas.append((country["name"], area))
    return country_areas


def get_all_language_names(countries):
    """Return a flat list with every language spoken, one entry per country."""
    language_names = []
    for country in countries:
        for language in country["languages"]:
            language_names.append(language["name"])
    return language_names


all_countries = get_countries(COUNTRIES_API_URL)

country_areas = get_country_areas(all_countries)
ten_largest_countries = get_top_n(country_areas, 10)
print("10 largest countries:", ten_largest_countries)

all_language_names = get_all_language_names(all_countries)
language_frequency = build_frequency_table(all_language_names)
ten_most_spoken_languages = get_top_n(list(language_frequency.items()), 10)
print("10 most spoken languages:", ten_most_spoken_languages)

total_number_of_languages = len(language_frequency)
print("Total number of languages:", total_number_of_languages)
