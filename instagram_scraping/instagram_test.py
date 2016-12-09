from bs4 import BeautifulSoup
import selenium.webdriver as webdriver

url = 'http://instagram.com/lilmiquela/'
driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")

for x in soup.findAll('li', {'class':'photo'}):
    print x