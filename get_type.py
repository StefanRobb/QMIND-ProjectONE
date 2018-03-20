import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

def get_type(soup):
    lists = soup.find_all('span', attrs = {'class': 'toggle-similar__title'})
    array = [ ]
    for li in lists:
        type = li.contents[0].strip()
        array.append(type)
    return array

url = 'http://allrecipes.com/recipe/' + '24264/sloppy-joes-ii/'
req = requests.get(url, headers={'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))})
page = req.text
soup = BeautifulSoup(page, 'html.parser')
mealArray = get_type(soup)
print(mealArray)