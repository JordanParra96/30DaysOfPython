"""Day 18: 30 Days of python programming"""

import re

# Match example
TXT = "I love to teach python and javaScript"
# It returns an object with span, and match
match = re.match("I love to teach", TXT, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)  # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0 15
substring = TXT[start:end]
print(substring)  # I love to teach

# Search example
SEARCH_TXT = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

# It returns an object with span and match
SEARCH_MATCH = re.search("first", SEARCH_TXT, re.I)
print(SEARCH_MATCH)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
SEARCH_SPAN = SEARCH_MATCH.span()
print(SEARCH_SPAN)  # (100, 105)
# Lets find the start and stop position from the span
start, end = SEARCH_SPAN
print(start, end)  # 100 105
SEARCH_SUBSTRING = SEARCH_TXT[start:end]
print(SEARCH_SUBSTRING)  # first

# Findall example
FINDALL_MATCHES = re.findall("language", SEARCH_TXT, re.I)
print(FINDALL_MATCHES)  # ['language', 'language']

# Replace example
match_replaced = re.sub("Python|python", "JavaScript", SEARCH_TXT, re.I)
print(match_replaced)
# OR
match_replaced = re.sub("[Pp]ython", "JavaScript", SEARCH_TXT, re.I)
print(match_replaced)


SUB_TEXT = """%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?"""

SUB_RESULT = re.sub("%", "", SUB_TEXT)
print(SUB_RESULT)

# Split example
SPLIT_TXT = """I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?"""
print(re.split("\n", SPLIT_TXT))  # splitting using \n - end of line symbol

# Regex pattern example
regex_pattern = r"apple"
PATTERN_TXT = (
    "Apple and banana are fruits."
    "An old cliche says an apple a day a doctor way has been replaced"
    "by a banana a day keeps the doctor far far away. "
)
matches = re.findall(regex_pattern, PATTERN_TXT)
print(matches)  # ['apple']
# To make case insensitive adding flag '
matches = re.findall(regex_pattern, PATTERN_TXT, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r"[Aa]pple"  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, PATTERN_TXT)
print(matches)  # ['Apple', 'apple']

# Square brackets example
regex_pattern = r"[Aa]pple|[Bb]anana"  # this square bracket means either A or a
BRACKETS_TXT = (
    "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced "
    "by a banana a day keeps the doctor far far away."
)
matches = re.findall(regex_pattern, BRACKETS_TXT)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']

# Escape character example
ESCAPE_PATTERN = (
    r"\d+"  # d is a special character which means digits, + mean one or more times
)
ESCAPE_TXT = (
    "This regular expression example was made on December 6,"
    "  2019 and revised on July 8, 2021"
)
ESCAPE_MATCHES = re.findall(ESCAPE_PATTERN, ESCAPE_TXT)
print(ESCAPE_MATCHES)  # ['6', '2019', '8', '2021'] - now, this is better!

# Period example
PERIOD_PATTERN = r"[a].+"  # . any character, + any character one or more times
PERIOD_TXT = """Apple and banana are fruits"""
PERIOD_MATCHES = re.findall(PERIOD_PATTERN, PERIOD_TXT)
print(PERIOD_MATCHES)  # ['and banana are fruits']

# Zero or more times example
ZERO_OR_MORE_PATTERN = r"[a].*"  # . any character, * any character
ZERO_OR_MORE_TXT = """Apple and banana are fruits"""
MATCHES = re.findall(ZERO_OR_MORE_PATTERN, ZERO_OR_MORE_TXT)
print(MATCHES)  # ['and banana are fruits']

# Zero or one time ? example
ZERO_TXT = """I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail."""
ZERO_PATTERN = r"[Ee]-?mail"  # ? means here that '-' is optional
ZERO_MATCHES = re.findall(ZERO_PATTERN, ZERO_TXT)
print(ZERO_MATCHES)  # ['e-mail', 'email', 'Email', 'E-mail']

# Quantifier example
quantifier_txt = (
    "This regular expression example was made on December 6,"
    "  2019 and revised on July 8, 2021"
)
quantifier_pattern = r"\d{4}"  # exactly four times
QUANTIFIER_MATCHES = re.findall(quantifier_pattern, quantifier_txt)
print(QUANTIFIER_MATCHES)  # ['2019', '2021']

quantifier_txt = (
    "This regular expression example was made on December 6,"
    "  2019 and revised on July 8, 2021"
)
quantifier_pattern = r"\d{1,4}"
QUANTIFIER_MATCHES = re.findall(quantifier_pattern, quantifier_txt)
print(QUANTIFIER_MATCHES)  # ['6', '2019', '8', '2021']

# Cart ^ example
CART_TXT = (
    "This regular expression example was made on December 6,  2019 and revis"
    "ed on July 8, 2021"
)
CART_PATTERN = r"^This"  # ^ means start of the string
CART_MATCHES = re.findall(CART_PATTERN, CART_TXT)
print(CART_MATCHES)  # ['This']

# Cart negation example
CART_NEGATION_TXT = (
    "This regular expression example was made on December 6,"
    "  2019 and revised on July 8, 2021"
)
# ^ in set character means negation, not A to Z, not a to z, no space
CART_NEGATION_PATTERN = r"[^A-Za-z ]+"
CART_NEGATION_MATCHES = re.findall(CART_NEGATION_PATTERN, CART_NEGATION_TXT)
print(CART_NEGATION_MATCHES)  # ['6', '2019', '8', '2021']

# Level 1 exercise

PARAGRAPH = (
    "I love teaching. If you do not love teaching what else can you love."
    " I love Python if you do not love something which can give you all the capabilities"
    " to develop an application what else can you love."
)

FRECUENCY_PATTERN = r"\b\w+\b"
FRECUENCY_MATCHES = re.findall(FRECUENCY_PATTERN, PARAGRAPH)
word_frequency = {}
for word in FRECUENCY_MATCHES:
    word_frequency[word] = word_frequency.get(word, 0) + 1
most_frequent_word = max(word_frequency, key=word_frequency.get)
print(
    f"The most frequent word is '{most_frequent_word}' "
    f"with a frequency of {word_frequency[most_frequent_word]}."
)

# Level 1 exercise
points = ["-12", "-4", "-3", "-1", "0", "4", "8"]
furthest_distance = int(max(points, key=int)) - int(min(points, key=int))
print(f"The distance between the two furthest particles is {furthest_distance}.")

# Level 2 exercise - write a pattern which identifies if a string is a valid python variable
VARIABLE_PATTERN = r"^[a-zA-Z_][a-zA-Z0-9_]*$"


def is_valid_variable(variable):
    """Return True if `variable` is a valid Python variable name.

    A valid variable starts with a letter (a-z, A-Z) or underscore, followed
    by letters, digits or underscores.
    """
    return bool(re.match(VARIABLE_PATTERN, variable))


print(is_valid_variable("first_name"))  # True
print(is_valid_variable("first-name"))  # False
print(is_valid_variable("1first_name"))  # False
print(is_valid_variable("firstname"))  # True

# Level 3 exercise
WRONG_SENTENCE = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;.
 There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
 ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s
 mo@tivate yo@u to be a tea@cher!?"""
result = re.sub(r"[^A-Za-z0-9. ]+", "", WRONG_SENTENCE)
print(result)
FREC_PATTERN = r"\b\w+\b"
FREC_MATCHES = re.findall(FREC_PATTERN, result)
word_frequency = {}
for word in FREC_MATCHES:
    word_frequency[word] = word_frequency.get(word, 0) + 1
most_frequent_word = max(word_frequency, key=word_frequency.get)
second_most_frequent_word = sorted(
    word_frequency, key=word_frequency.get, reverse=True
)[1]
third_most_frequent_word = sorted(word_frequency, key=word_frequency.get, reverse=True)[
    2
]
print(
    f"The most frequent word is '{most_frequent_word}' "
    f"with a frequency of {word_frequency[most_frequent_word]}."
)
print(
    f"The second most frequent word is '{second_most_frequent_word}' "
    f"with a frequency of {word_frequency[second_most_frequent_word]}."
)
print(
    f"The third most frequent word is '{third_most_frequent_word}' "
    f"with a frequency of {word_frequency[third_most_frequent_word]}."
)
