

"""
This is a program that takes a given url, and returns an
ordered list of words and the frequency they appear.

It can remove common words, low frequency words, and export words to .csv
"""

from bs4 import BeautifulSoup
import requests
import csv

# Go to this url, and get the .text
source = requests.get('https://www.kuow.org/careers/Data-Analyst-Temporary').text
# Store url.text data in this var
soup = BeautifulSoup(source, 'lxml')

# Find the word 'article' in the html code
article = soup.find('article')
# Within 'article', find the following data 
interesting = article.find('div', class_='body-content').text


# Use this if you want to save data as a .csv
"""
with open('job_description.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = csv.writer(f)
"""


# Create dict to store words and their freq in
word_dict = {}

# A list of all words not to be included  
exclusion_list = [
    'and',
    'to',
    'of',
    'the',
    'for',
    'a',
    'will',
    'that',
    'google',
    'you',
    'or',
    'is',
    'with',
    'in',
    'be',
    'this',
    'digital',
    'are',
    'your',
    'kuow',
    'at',
    'as',
    'an',
    'on',
    'covid-19'
]

# A list of all words to be prioritized 
priority_list = [
"""
    'data',
    'reports',
    'reporting',
    'opportunity',
    'requirements',
    'required',
    'api'
"""
]


# Split the text into individual words as strs
# Tally the word counts and store them in word_dict
for str in interesting.split():
    str = str.lower()
    if str not in exclusion_list:
        if str in word_dict:
            word_dict[str] += 1
        else:
            word_dict[str] = 1

# Return the max word count as an int
max_num = max(word_dict, key=word_dict.get)


# Convert to list to order data easily
word_list = []


for i in range(word_dict[max_num] + 1):
    for key, val in word_dict.items():
        if val == i:
            word_list.append([val, key])

# Sort list in reverse order
sorted_word_list = sorted(word_list, reverse=True)


# Print the entire list:
"""
print(f'\n\nword_list: {sorted_word_list}\n\n')
"""

# Or

# Only print words above a specified freq (3)
print('\n\n')
print(f'\tFreq  |  Word')
print(f'—' * 30)
for i in range(len(sorted_word_list)):
    if sorted_word_list[i][0] > 3:
        if sorted_word_list[i][0] >= 100:
            print(f'\t {sorted_word_list[i][0]}: |  {sorted_word_list[i][1]}')
        elif 10 <= sorted_word_list[i][0] < 100:
            print(f'\t {sorted_word_list[i][0]}:  |  {sorted_word_list[i][1]}')
        else:
            print(f'\t {sorted_word_list[i][0]}:   |  {sorted_word_list[i][1]}')
print('\n')
