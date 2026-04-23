"""
Date : 22-04-26
Desc : Number of times 'a' appears in a string using enumerate
"""

str='casablanca'

count = 0
for index, char in enumerate(str):
    if char == 'a':
        count += 1

print("Count of 'a' : ", count)
