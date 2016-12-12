"""
PRELIMINARY MATERIALS for an AMAZON WISHLIST of the YOUNG GIRL(Credit to Leon Eckert and Matthew Plummer-Fernandez, DECOY AMAZON BROWSING 2015)



Ammend the settings.cfg file to enter your Amazon account email and password
and prefered Amazon domain extension (.com, .co.uk, etc). Also enable wishlist on/off.

Copyright (C) 2015,  Matthew Plummer-Fernandez 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
<http://www.gnu.org/licenses/>
#

"""
import emoji
print (emoji.emojize(':thumbs up:'))

print (emoji.emojize(':information_desk_person:')) + " Preliminary Materials for a Theoretical young_girl Amazon WishList " + (emoji.emojize(':money_with_wings:'))

#  +  laptop flying money
# print x.encode('UTF8','ignore')

import time, random, ConfigParser
from selenium import webdriver
# from random_words import RandomWords
# import noun_extract
from textblob import TextBlob
from bs4 import BeautifulSoup


def randWord():

	nouns = list()
	for line in open("newtextfile.txt", "r"):
		line = line.strip()
		# print line 
		nouns.append(line)

	word = random.choice(nouns)
	return word


def getSigninLink(page):
	links = []
	url = ''
	for link in page.find_all('a'):
		# role = link.get('data-nav-role')
		# if role:
		# 	if role == "signin":
		# 		url = link.get('href')
		# 		print url

		_class = link.get('class')
		if _class:
			if _class == "nav-a nav-a-2":
				url = link.get('href')
				# print url
	return url


def getProductLinks(domain,page):
	links = []
	for link in page.find_all('a'):
		# print "\n---\nlink", link
		url = link.get('href')
		if url:
			# print "\n---\nin if url", url
			if 'https://www.amazon'+domain+'/'in url:
				if '/dp/' in url:
					if '#customerReviews' in url:
						#ignore customer review links
						notinterested = 1
					else:
						links.append(url)
					# links.append(url)

	# print "what i found", links
	return links


def addToWishlist(browser):
	time.sleep(random.uniform(1,2))
	try:
		wishElement = browser.find_element_by_id("add-to-wishlist-button-submit")

		print wishElement
		if wishElement:
			print "[+] the young_girl added item to wishlist "  + (emoji.emojize(':information_desk_person:'))
			wishElement.click()
			print "[+] the young_girl made a wish " + (emoji.emojize(':money_with_wings:'))
		else:
			print "[-] the young_girl doesn't see a wishElement " + (emoji.emojize(':person_frowning:'))
	except:
			print "[-] the young_girl doesn't see a  " + (emoji.emojize(':person_frowning:'))



def BrowseBot(domain, browser, wishlisting):
	visited = {}
	pList = []
	count = 0
	aurl = ""
	while True:
		#sleep to make sure page loads, add random to make it act human.
		time.sleep(random.uniform(2.1,3.9))
		
		if pList: #if there are products, browse them
			productpage = pList.pop()
			try:
				browser.get(productpage)
			except:
				print "[-] the young_girl could not get page " + (emoji.emojize(':person_frowning:'))
			count += 1
			# add to wishlist
			if wishlisting == True:
				addToWishlist(browser)
			else:
				wishing = 0			
		else: #otherwise find products via a new random search
			if len(aurl)>0:
				browser.get(aurl)

			print "[+] the young_girl is searching for something to buy  "  + (emoji.emojize(':eyes:'))
			word = randWord()
			searchElement = browser.find_element_by_id("twotabsearchtextbox")
			time.sleep(random.uniform(0.5,1.4))
			searchElement.clear()

			searchWord = list(word)
			for i in searchWord:
				searchElement.send_keys(i)
				time.sleep(random.uniform(0.5,1.4))
			time.sleep(random.uniform(0.5,1.4))



			aurl = "http://amazon"+domain+"/s/?url=search-alias%3Daps&field-keywords="+word
			# print aurl
			browser.get(aurl)

			# print "@ browser.page_source"
			page = BeautifulSoup(browser.page_source, "lxml")
			products = getProductLinks(domain,page)
			if products:
				for productpage in products:
					if productpage not in visited:
						pList.append(productpage)
						visited[productpage] = 1
				print "before = " + str(len(pList))	
				random.shuffle(pList)
				pList = list(set(pList))[:4]
				print "after = " + str(len(pList))
		#Output 		
		print "[+] the young_girl browsed " +(browser.title).encode('ascii','ignore')+(emoji.emojize(':computer:'))+"\n("\
			+str(count)+"/"+str(len(pList))+") Visited/Queue) " 
					

def Main():
	config = ConfigParser.ConfigParser()
	try:
		config.read('settings.cfg')
		print "[+] the young_girl has read your settings " + (emoji.emojize(':information_desk_person:'))
	except:
		print "[-] The young_girl could not read your settings" + (emoji.emojize(':person_frowning:'))

	configDomain = config.get('amazon','domain')
	configEmail = config.get('amazon','email')
	configPass = config.get('amazon','psswrd')
	configWish = config.getboolean('amazon','wishlist')

	## Initiate browser
	browser = webdriver.Chrome()
	browser.set_window_size(980,1820)
	browser.set_window_position(200,200)
	aurl = 'http://www.amazon'+configDomain
	browser.get(aurl)
	page = BeautifulSoup(browser.page_source, "lxml")
	# signinUrl = getSigninLink(page)
	signinUrl = 'https://www.amazon.com//gp/navigation/redirector.html/ref=sign-in-redirect/157-9481065-2773405?ie=UTF8&associationHandle=usflex&currentPageURL=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&pageType=Gateway&yshURL=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_ya_signin'
	time.sleep(random.uniform(0.5,1.4))
	browser.get(signinUrl)

	emailElement = browser.find_element_by_id("ap_email")
	configEmail2 = list(configEmail)
	for i in configEmail2:
		emailElement.send_keys(i)
		time.sleep(random.uniform(0,0.1))

	time.sleep(random.uniform(0.5,1.4))
	passElement = browser.find_element_by_id("ap_password")
	configEmail2 = list(configPass)
	for i in configEmail2:
		passElement.send_keys(i)
		time.sleep(random.uniform(0,0.1))
	time.sleep(random.uniform(0.5,1.4))
	passElement.submit()

	print "[+] The young_girl has logged in to Amazon.  " + (emoji.emojize(':thumbs up:'))
	
	domain = configDomain
	wishlisting = True
	
	BrowseBot(domain, browser, wishlisting)
	browser.close()

if __name__ == '__main__':
	Main()



