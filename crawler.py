from urllib.request import urlopen
from bs4 import BeautifulSoup
from my_util import make_dir
import requests
import urllib


def get_content():
	base_url = 'http://dongascience.donga.com/news.php?idx='
	output_dir = 'C:/pro/data/donga/'
	make_dir(output_dir)
	output_file = output_dir + 'donga.txt'
	missed_output_link = output_dir + 'donga_missed.txt'

	for i in range(18445, 30063):
		
		url = base_url + str(i)
		page = urlopen(url)
		page_soup = BeautifulSoup(page, "html.parser")
		article = page_soup.find('div', id='article_body')
		try:
			txt = article.get_text()
		except AttributeError:
			missed_link = url
			if missed_link != '':
				with open(missed_output_link, 'a', encoding='utf-8') as output:
					output.write(missed_link + '\n')
		
		with open(output_file, 'a', encoding='utf-8') as output:
			output.write(txt + '\n')
			if i%100 == 0:
				print("index num {} saved".format(i))
		
def get_luxury():
	name = 'luxury'
	base_url = 'http://luxury.designhouse.co.kr/in_magazine/sub.html?&p_no='
	page_base_url = 'http://luxury.designhouse.co.kr'
	end_page = 533
	output_dir = 'C:/pro/data/{}/'.format(name)
	make_dir(output_dir)
	output_file = output_dir + '{}.txt'.format(name)
	missed_output_link = output_dir + '{}_missed.txt'.format(name)
	for i in range(1, end_page + 1):
		url = base_url + str(i)
		html = urlopen(url)
		soup = BeautifulSoup(html, "html.parser")
		link_data = soup.find_all('a', class_='fst2x')
		total_txt = ''
		missed_link = ''
		for link_datum in link_data:
			link = link_datum["href"]
			page = urlopen(page_base_url + link)
			page_soup = BeautifulSoup(page, "html.parser")
			article = page_soup.find('div', class_='articles')
			try:
				total_txt += article.get_text() + '\n'
			except AttributeError:
				missed_link += link + '\n'
		with open(output_file, 'a', encoding='utf-8') as output:
			output.write(total_txt + '\n')
			print("index num {} saved".format(i))
		if missed_link != '':
			with open(missed_output_link, 'a', encoding='utf-8') as output:
				output.write(missed_link + '\n')



def get_happyful_house():
	name = 'happyful'
	categories = (('00010002', 179), ('00010003', 106), ('00010004', 86), ('00010005', 146), ('00010006', 36))
	base_url = 'http://happy.designhouse.co.kr/magazine/magazine_list/'

	page_base_url = 'http://happy.designhouse.co.kr'
	output_dir = 'C:/pro/data/{}/'.format(name)
	make_dir(output_dir)
	output_file = output_dir + '{}.txt'.format(name)
	missed_output_link = output_dir + '{}_missed.txt'.format(name)
	for category in categories:
		base_category_url = base_url + category[0] + '/0/'
		for i in range(1, category[1] + 1):
			url = base_category_url + str(i)
			html = urlopen(url)
			soup = BeautifulSoup(html, "html.parser")
			link_data = soup.find_all('a', class_='txt')
			total_txt = ''
			missed_link = ''
			for link_datum in link_data:
				link = link_datum["href"]
				page = urlopen(page_base_url + link)
				page_soup = BeautifulSoup(page, "html.parser")
				article = page_soup.find('div', id='view-info')
				try:
					total_txt += article.get_text() + '\n'
				except AttributeError:
					missed_link += link + '\n'
			with open(output_file, 'a', encoding='utf-8') as output:
				output.write(total_txt + '\n')
				print("index num {} saved".format(i))
			if missed_link != '':
				with open(missed_output_link, 'a', encoding='utf-8') as output:
					output.write(missed_link + '\n')



def get_gq():
	name = 'gq'
	categories = (('entertainment', 163), \
		('traveleats', 39)) #('style', 128), ('grooming', 24), ('now', 11), ('cartech', 58)
	base_url = 'http://www.gqkorea.co.kr/category/'

	page_base_url = 'http://happy.designhouse.co.kr'
	output_dir = 'C:/pro/data/{}/'.format(name)
	make_dir(output_dir)
	output_file = output_dir + '{}.txt'.format(name)
	missed_output_link = output_dir + '{}_missed.txt'.format(name)
	for category in categories:
		base_category_url = base_url + category[0] + '/page/'
		for i in range(1, category[1] + 1):
			url = base_category_url + str(i)
			html = urlopen(url)
			soup = BeautifulSoup(html, "html.parser")
			link_data = soup.find_all('h2', class_='entry-title')
			total_txt = ''
			missed_link = ''
			for link_datum in link_data:
				link = link_datum.find('a')["href"]
				#for a in data.find_all('a'):
				#print(a.get('href')) #for getting link
				#print(a.text) #for getting text between the link

				#link = link_datum["href"]
				page = urlopen(link)
				page_soup = BeautifulSoup(page, "html.parser")
				article = page_soup.find('div', class_='post-content')
				try:
					total_txt += article.get_text() + '\n'
				except AttributeError:
					missed_link += link + '\n'
			with open(output_file, 'a', encoding='utf-8') as output:
				output.write(total_txt + '\n')
				print("index num {} saved".format(i))
			if missed_link != '':
				with open(missed_output_link, 'a', encoding='utf-8') as output:
					output.write(missed_link + '\n')




def get_lady_kh():
	headers = {'User-Agent':'Chrome/66.0.3359.181'}

	name = 'lady_kh'
	categories = (('4', 200), ('8', 137), ('9', 152), ('10', 225), ('11', 136), \
		('12', 40), ('13', 53), ('14', 39))
	base_url = 'http://lady.khan.co.kr/subList.html?code='
	output_dir = 'C:/pro/data/{}/'.format(name)
	make_dir(output_dir)
	output_file = output_dir + '{}.txt'.format(name)
	missed_output_link = output_dir + '{}_missed.txt'.format(name)
	for category in categories:
		base_category_url = base_url + category[0] + '&page='
		for i in range(1, category[1] + 1):
			url = base_category_url + str(i)

			res = requests.get(url, headers=headers)
			soup = BeautifulSoup(res.text, "html.parser")
			link_data = soup.find_all('dd', class_='txt')
			total_txt = ''
			missed_link = ''
			for link_datum in link_data:
				link = link_datum.find('a')["href"]
				page = requests.get(link, headers=headers)
				page_soup = BeautifulSoup(page.text, "html.parser")
				article = page_soup.find('div', id='_article')
				try:
					total_txt += article.get_text() + '\n'
				except AttributeError:
					missed_link += link + '\n'
			with open(output_file, 'a', encoding='utf-8') as output:
				output.write(total_txt + '\n')
				print("index num {} saved".format(i))
			if missed_link != '':
				with open(missed_output_link, 'a', encoding='utf-8') as output:
					output.write(missed_link + '\n')



def get_woman_chosun():
	headers = {'User-Agent':'Chrome/66.0.3359.181'}
	#http://woman.chosun.com/client/news/lst.asp?cate=C05&mcate=&ltype=1&cpage=11
	name = 'woman_chosun'
	categories = (('C01', 123), ('C02', 189), ('C03', 66), ('C04', 61), ('C05', 11))
	base_url = 'http://woman.chosun.com/client/news/lst.asp?cate='
	base_page_url = 'http://woman.chosun.com/client/news/'
	output_dir = 'C:/pro/data/{}/'.format(name)
	make_dir(output_dir)
	output_file = output_dir + '{}.txt'.format(name)
	missed_output_link = output_dir + '{}_missed.txt'.format(name)
	for category in categories:
		base_category_url = base_url + category[0] + '&mcate=&ltype=1&cpage='
		for i in range(1, category[1] + 1):
			url = base_category_url + str(i)

			res = requests.get(url, headers=headers)
			soup = BeautifulSoup(res.text, "html.parser")
			link_data = soup.select('td.at a')
			total_txt = ''
			missed_link = ''
			links = []
			for link_datum in link_data:
				link = link_datum.attrs['href']
				links.append(link.strip())
			links = list(set(links))
			for link in links:
				page = requests.get(base_page_url + link, headers=headers)
				page_soup = BeautifulSoup(page.text, "html.parser")
				article = page_soup.find('div', id='articleBody')
				try:
					total_txt += article.get_text() + '\n'
				except AttributeError:
					missed_link += link + '\n'
			with open(output_file, 'a', encoding='utf-8') as output:
				output.write(total_txt + '\n')
				print("index num {} saved".format(i))
			if missed_link != '':
				with open(missed_output_link, 'a', encoding='utf-8') as output:
					output.write(missed_link + '\n')


def get_weekly_khan():
	headers = {'User-Agent':'Chrome/66.0.3359.181'}
	name = 'weekly_khan'
	categories_1 = (('n0002', 211), ('n0001', 126))
	categories_2 = (('113', 409), ('114', 372), ('115', 950), \
		('116', 696), ('117', 137), ('124', 119), ('115', 950))
	categories = (('n0002', 211), ('n0001', 126), ('113', 409), ('114', 372), ('115', 950), \
		('116', 696), ('117', 137), ('124', 119), ('115', 950))
	
	output_dir = 'C:/pro/data/{}/'.format(name)
	make_dir(output_dir)
	output_file = output_dir + '{}.txt'.format(name)
	missed_output_link = output_dir + '{}_missed.txt'.format(name)
	base_page_url = 'http://weekly.khan.co.kr'
	for category in categories:
		if category in categories_1:
			base_url = 'http://weekly.khan.co.kr/khnm.html?mode=serial&s_code='
			base_category_url = base_url + category[0] + '&page='
		else:
			base_url = 'http://weekly.khan.co.kr/khnm.html?mode=list&code='
			base_category_url = base_url + category[0] + '&page='
		for i in range(1, category[1] + 1):
			url = base_category_url + str(i)

			res = requests.get(url, headers=headers)
			soup = BeautifulSoup(res.text, "html.parser")
			link_data = soup.find_all('div', class_='photoArticle dot')
			total_txt = ''
			missed_link = ''
			for link_datum in link_data:
				p = link_datum.find('p')
				link = p.find('a')["href"]
				page = requests.get(base_page_url + link, headers=headers)
				page_soup = BeautifulSoup(page.text, "html.parser")
				article = page_soup.find('div', class_='article_txt')

				try:
					total_txt += article.get_text() + '\n'
				except AttributeError:
					missed_link += link + '\n'
			with open(output_file, 'a', encoding='utf-8') as output:
				output.write(total_txt + '\n')
				print("index num {} saved".format(i))
			if missed_link != '':
				with open(missed_output_link, 'a', encoding='utf-8') as output:
					output.write(missed_link + '\n')



def get_chosun_biz():
	headers = {'User-Agent':'Chrome/66.0.3359.181'}
	name = 'chosun_biz'

	categories = (('8', 7069, 7196), ('6', 1, 2349), ('5', 1, 5573), ('2', 1, 648)) #('7', 7732, 10000), ('4', 1, 2999), 
	base_url = 'http://biz.chosun.com/svc/list_in/list.html?catid='
	base_page_url = 'http://biz.chosun.com'
	output_dir = 'C:/pro/data/{}/'.format(name)
	make_dir(output_dir)
	
	missed_output_link = output_dir + '{}_missed.txt'.format(name)
	for category in categories:
		output_file = output_dir + '{}_{}.txt'.format(name, category[0])
		base_category_url = base_url + category[0] + '&pn='
		for i in range(category[1], category[2] + 1):
			url = base_category_url + str(i)

			res = requests.get(url, headers=headers)
			soup = BeautifulSoup(res.text, "html.parser", from_encoding='utf-8')
			link_data = soup.select('dl.list_item dt a')
			total_txt = ''
			missed_link = ''
			links = []
			for link_datum in link_data:
				link = link_datum.attrs['href']
				links.append(link.strip())
			links = list(set(links))
			for link in links:
				#page = requests.get(base_page_url + link, headers=headers)
				try:

					page = urlopen(base_page_url + link)
					#content = page.read().decode('euc-kr','replace').encode('utf-8','replace')
					content = page.read().decode('utf-8') 
					page_soup = BeautifulSoup(content, "html.parser") #, from_encoding='utf-8'
					article = page_soup.find('div', class_='par')

					#html = urllib2.urlopen(link)
					#content = html.read().decode('euc-kr','replace').encode('utf-8','replace')
					#soup = BeautifulSoup(content)

					#print(article.get_text())
					try:
						total_txt += article.get_text() + '\n'
					except AttributeError:
						missed_link += link + '\n'
				except urllib.error.HTTPError:
					pass
			if total_txt != 0:
				with open(output_file, 'a', encoding='utf-8') as output:
					output.write(total_txt + '\n')
					print("index num {} saved".format(i))
			if missed_link != '':
				with open(missed_output_link, 'a', encoding='utf-8') as output:
					output.write(missed_link + '\n')


if __name__ == '__main__':
	menu_str = '''
	0 동아\n
	1 럭셔리\n
	2 행복이 가득한 집\n
	3 지큐\n
	4 레이디경향\n
	5 여성조선\n
	6 주간경향 \n
	7 조선비즈 \n
	8 agg_unq_numbered_verbs \n
	9 drop_redundant_data_from_final_result \n

	입력: 
	'''
	menu = int(input(menu_str))
	if menu == 0:
		get_content()
	elif menu == 1:
		get_luxury()
	elif menu == 2:
		get_happyful_house()
	elif menu == 3:
		get_gq()
	elif menu == 4:
		get_lady_kh()
	elif menu == 5:
		get_woman_chosun()
	elif menu == 6:
		get_weekly_khan()
	elif menu == 7:
		get_chosun_biz()
		
		
		
		

	
