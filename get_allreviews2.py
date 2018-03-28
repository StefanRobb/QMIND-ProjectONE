from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from user_agent import generate_user_agent

def get_allreviews(url):
    driver = webdriver.Chrome(executable_path = r'C:\Users\stefa\Desktop\Second Year\QMIND\QMIND Data\ProjectOne\Selenium\ChromeDriver\ChromeDriver.exe')
    driver.get(url)
    reviewTabs = driver.find_element_by_xpath("//*[@id='reviews']/a")
    reviewTabs.click()
    review_array = []
    for i in range(1, get_numreviews(url) + 1):
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        review_array.append(get_review(soup))
        next = driver.find_element_by_xpath("//*[@id='BI_loadReview2_right']")
        next.click()
    return review_array

def get_review(soup):
    review = soup.find('p', attrs = {'ng-bind': 'review.text'})
    return review.contents[0]

def get_numreviews(url):
    req = requests.get(url, headers={'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))})
    page = req.text
    soup = BeautifulSoup(page, 'html.parser')
    number = soup.find('span', attrs = {'class': 'recipe-reviews__header--count'})
    return int(number.contents[0])

url = 'http://allrecipes.com/recipe/' + '23275'
reviews = get_allreviews(url)
print(reviews)
print(len(reviews))