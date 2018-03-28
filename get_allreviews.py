from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup

def extend_page(url):
    driver = webdriver.Chrome(executable_path = r'C:\Users\stefa\Desktop\Second Year\QMIND\QMIND Data\ProjectOne\Selenium\ChromeDriver\ChromeDriver.exe')
    driver.get(url)
    for i in range(1,8):
        if i == 1:
            try:
                moreReviews = driver.find_element_by_xpath("//*[@id='reviews']/div[7]/div")
                moreReviews.click()
                driver.implicitly_wait(2)
            except WebDriverException:
                print("Error")
                break
        else:
            try:
                istr = str(i)
                moreReviews2 = driver.find_element_by_xpath("//*[@id='reviews']/div[7]/div[" + istr + "]")
                moreReviews2.click()
                driver.implicitly_wait(2)
            except WebDriverException:
                print("All reviews shown")
                break
    page = driver.page_source
    return page

def get_review(soup):
    lists = soup.findAll('div', attrs = {'class': 'review-container clearfix'})
    lists2 = soup.findAll('div', attrs = {'class': 'review-container clearfix ng-scope'})
    array = []
    for li in lists:
        tag = li.find('p', attrs = {'itemprop': 'reviewBody'})
        array.append(tag.contents[0])
    for li in lists2:
        tag = li.find('p', attrs = {'itemprop': 'reviewBody'})
        array.append(tag.contents[0])
    array = array[2:len(array)]
    return array

url = 'http://allrecipes.com/recipe/' + '15991'
page = extend_page(url)
soup = BeautifulSoup(page, 'html.parser')
reviews = get_review(soup)
print(reviews)
print(len(reviews))