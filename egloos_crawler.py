import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import re
import shutil
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException

ua = UserAgent()
path = "C:\pro\driver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("user-agent=" + ua.random)
driver = webdriver.Chrome(path, chrome_options=options)

space = re.compile(r'\s{2,}')
line_space = re.compile(r'\n{2,}')
#	('movie', 'http://valley.egloos.com/theme/movie/page/'),
#	('tv', 'http://valley.egloos.com/theme/entertainment/page/'),
egloos_pool = [
	('game', 'http://valley.egloos.com/theme/game/page/'),
	('pokemongo', 'http://valley.egloos.com/theme/pokemongo/page/'),
	('animation', 'http://valley.egloos.com/theme/animation/page/'),
	('comic', 'http://valley.egloos.com/theme/comic/page/'),
	('book', 'http://valley.egloos.com/theme/book/page/'),
	('music', 'http://valley.egloos.com/theme/music/page/'),
	('performance', 'http://valley.egloos.com/theme/performance/page/'),
	('food', 'http://valley.egloos.com/theme/food/page/'),
	('pet', 'http://valley.egloos.com/theme/pet/page/'),
	('travel', 'http://valley.egloos.com/theme/travel/page/'),
	('photo', 'http://valley.egloos.com/theme/photo/page/'),
	('fashion', 'http://valley.egloos.com/theme/fashion/page/'),
	('love', 'http://valley.egloos.com/theme/love/page/'),
	('daily', 'http://valley.egloos.com/theme/daily/page/'),
	('baby', 'http://valley.egloos.com/theme/baby/page/')
	]

def get_egloos_content():
	for url in egloos_pool:
		print(url)
		if url[0] == 'game':
			start = 5886
		else:
			start = 1
		for i in range(start, 10000000000):
			print(i)
			driver.get(url[1]+str(i))
			time.sleep(1)
			try:
				urls = driver.find_elements_by_css_selector('dl.f_clear > dt > a')
			except:
				try:
					urls = driver.find_elements_by_css_selector('dl.f_clear > dt > a')
				except:
					print('end of pages', i)
					break
			url_list = []
			for article_url in urls:
				href = article_url.get_attribute("href")
				if 'egloos' in href:
					url_list.append(href)

			for a_url in url_list:
				#print(a_url)
				driver.get(a_url)
				time.sleep(1)
				missing_content_tag_urls = ''
				content = ''
				try:
					no_article = driver.find_element_by_class_name('box_message')
					print(a_url, 'does not exist')
					break
				except NoSuchElementException:
					try:
						content = driver.find_element_by_class_name('POST_BODY')
					except NoSuchElementException:
						try:
							content = driver.find_element_by_class_name('hentry')
						except NoSuchElementException:
							try:
								content = driver.find_element_by_class_name('content')
							except NoSuchElementException:
								missing_content_tag_urls += a_url + '\n'
								print(a_url, 'content not found')
				if content != '':
					text = content.text
					txt = re.sub(space, ' ', text)
					txt = re.sub(line_space, ' ', txt)
					with open('C:/pro/data/egloos/{}.txt'.format(url[0]), 'a', encoding='utf-8') as output:
						output.write(txt + '\n')
				if missing_content_tag_urls != '':
					with open('C:/pro/data/egloos/missed.txt', 'a', encoding='utf-8') as p:
						p.write(missing_content_tag_urls)

if __name__ == '__main__':
	get_egloos_content()
