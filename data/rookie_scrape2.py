#code to scrape diary entries from rookiemag.com

from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import urllib
import cfscrape
import requests
# import json

# url = "http://www.rookiemag.com/2015/10/october-8-2015/"
# r = urllib.urlopen(url).read()
url = "http://www.rookiemag.com/"


year = [2015] #, 2014, 2013, 2012]
month = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
month_name = ["december", "november", "october", "september", "august", "july", "june", "may",
 "april", "march", "february", "january"]

url_list = [] #create a list to hold all the urls

# iterate through dates and generate urls
for x in year:
	for y in month: #[actual number is y]
		date = str(x) + "/" + str(y) + "/"
		if y == 11 or y == 9 or y == 6 or y == 4:
			for a in range (1,31): #day			
				page_name = month_name[12-y] + "-" + str(a) + "-" + str(x) + "/2/"
				url_list.append(url + str(date) + page_name) 
				
		if y == 2:
			for a in range(1,29):
				date = str(x) + "/" + str(y) + "/"
				page_name = "february" + "-" + str(a) + "-" + str(x) + "/2/"
				# query =  str(date) + page_name
				url_list.append(url + str(date) + page_name)
		else:
			for a in range(1,32):
				date = str(x) + "/" + str(y) + "/"
				page_name = month_name[12-y] + "-" + str(a) + "-" + str(x) + "/2/"
				# query = str(date) + page_name
				url_list.append(url + str(date) + page_name)



#list of urls that we can now parse
for item in url_list:

	scraper = cfscrape.create_scraper() #gets past cloudflare
	html_content = scraper.get(item)

	soup = BeautifulSoup((html_content.content), "html.parser")
	content = soup.find('div', attrs = {'class':'post-content article-content'}) #gets div

	u'\u2019'.encode('utf8') #encode for ASCII characters
	if content is not None: # if page exists, print
		entry = content.text.strip() # strip() is used to remove starting and trailing  
		# print item
		print entry.encode('utf-8') #encode for ASCII characters



# with open("ananda_test.json", "w") as writeJSON:
#     json.dump(entry, writeJSON)