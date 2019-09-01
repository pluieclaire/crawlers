import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import re
import shutil
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException

ua = UserAgent()
#browser = webdriver.Chrome('BrowserDriverPath')
#1차 크롤링: 2017년도부터 2019년 2월 12일까기 등록된 글
path = "C:\pro\driver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('headless')
#options.add_argument("disable-gpu")
options.add_argument("user-agent=" + ua.random)
driver = webdriver.Chrome(path, chrome_options=options)

space = re.compile(r'\s{2,}')
line_space = re.compile(r'\n{2,}')
#non_korean = re.compile(r'[^가-힣]')

directory = "./data/brunch/"
file_names = os.listdir(directory)
print(file_names)
for name in file_names:
	if name == 'brunch_urls' or name == 'done' or name == 'txt_files':
		pass
	else:
		data = pd.read_csv("./data/brunch/{}".format(name), names=["urls"], sep=",", dtype='object')
		for url in data['urls']:
			driver.get(url)
			time.sleep(1)
			#print(url)
			state = True
			while state:
				try:
					txt = driver.find_element_by_class_name("wrap_body")
				except NoSuchElementException:
					state = True
					try:
						alert_str = driver.find_element_by_class_name("alert-title")
						state = False
						print(url)
					except NoSuchElementException:
						state = True
				finally:
					state = False
			try:
				txt = txt.text
			except AttributeError:
				print(url)
			finally:
				txt = re.sub(space, ' ', txt)
				txt = re.sub(line_space, ' ', txt)
				with open('./data/brunch/txt_files/{}.txt'.format(name), 'a', encoding='utf-8') as output:
					output.write(txt + '\n')
		shutil.move("./data/brunch/{}".format(name), "./data/brunch/done/{}".format(name))