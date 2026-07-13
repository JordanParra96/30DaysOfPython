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
