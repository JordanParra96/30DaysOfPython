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
