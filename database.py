import requests
from bs4 import BeautifulSoup

FILENAME = 'words.txt'

url = 'https://www.rockpapershotgun.com/wordle-past-answers'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
# Find element above the wanted list
element = soup.find(string='All Wordle answers')
if element:
    parent = element.find_parent('h2')
    word_list = parent.next_sibling.next_sibling # Get the list (<ul> element)
    with open(FILENAME, 'w') as f:
        for word in word_list:
            f.write(word.text)
else:
    print("Error")

