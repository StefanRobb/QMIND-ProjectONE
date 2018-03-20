import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

def get_review(soup):
    lists = soup.findAll('div', attrs = {'class': 'review-container clearfix'})
    array = []
    for li in lists:
        tag = li.find('p', attrs = {'itemprop': 'reviewBody'})
        array.append(tag.contents[0])
    return array

url = 'http://allrecipes.com/recipe/' + '15991'
req = requests.get(url, headers={'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))})
page = req.text
soup = BeautifulSoup(page, 'html.parser')
recipe_review = get_review(soup)
print(recipe_review)