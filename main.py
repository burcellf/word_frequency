
"""
This is a program that finds the most common words used on a website page by:

    1) Collecting data
            - the user supplies a url
            
    2) Cleaning data
            - the programm searches through the site body for text,
            - strips the text of its html formatting,
            - creates individual words via text parsing
            - removes unnecessary words (such as 'and', 'to', 'the', etc),
            
    3) Organizing data
            - counts the occurrence of each word
            - orders words from most frequent to least frequent

    4) Presenting data
            - prints words and their frequency in decending order
            - (optional) only prints words that occured above a given frequency (default = 3)

    5) Saving data
            - (optional) exports ordered list as a .csv file
"""


from bs4 import BeautifulSoup
import requests
import csv

# Enter the url you want to use, and get the .text
source = requests.get('url').text
# Store a reference to the url.text data
soup = BeautifulSoup(source, 'lxml')

# Find the word 'article' in the html code
article = soup.find('article')
# Within 'article', find the following data 
interesting = article.find('div', class_='body-content').text


# Uncomment this section to save the data as a .csv
"""
with open('file_name.csv', 'w', encoding='utf8', newline='') as f:
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

# Create a list to easily organize dictionary data
word_list = []

for i in range(word_dict[max_num] + 1):
    for key, val in word_dict.items():
        if val == i:
            word_list.append([val, key])

# Sort list in reverse order
sorted_word_list = sorted(word_list, reverse=True)


# Uncomment to print the entire list:
"""
print(f'\n\nword_list: {sorted_word_list}\n\n')
"""

# Or

# Only print words that occured more than n times
n = 3

print('\n\n')
print(f'\tFreq  |  Word')
print(f'—' * 30)
for i in range(len(sorted_word_list)):
    if sorted_word_list[i][0] > n:
        if sorted_word_list[i][0] >= 100:
            print(f'\t {sorted_word_list[i][0]}: |  {sorted_word_list[i][1]}')
        elif 10 <= sorted_word_list[i][0] < 100:
            print(f'\t {sorted_word_list[i][0]}:  |  {sorted_word_list[i][1]}')
        else:
            print(f'\t {sorted_word_list[i][0]}:   |  {sorted_word_list[i][1]}')
print('\n')
