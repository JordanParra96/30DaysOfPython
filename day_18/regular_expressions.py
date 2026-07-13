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
