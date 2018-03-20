import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

def get_nutri(soup):
    nutri_type = ['calories', 'fatContent', 'carbohydrateContent', 'proteinContent', 'cholesterolContent', 'sodiumContent']
    nutri_quantity = ['', ' g fat', ' g carbohydrates', ' g protein', ' mg cholestrol', ' mg sodium']
    array = []
    for i, nutri in enumerate(nutri_type):
        tag = soup.find('span', attrs = {'itemprop': nutri})
        if nutri == 'calories':
            s = (tag.contents[0]).rstrip(";")
            array.append(s)
        else:
            s = tag.contents[0] + nutri_quantity[i]
            array.append(s)
    return array

url = 'http://allrecipes.com/recipe/' + '23263'
req = requests.get(url, headers={'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))})
page = req.text
soup = BeautifulSoup(page, 'html.parser')
mealNutri = get_nutri(soup)
print(mealNutri)
