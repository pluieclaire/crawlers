from urllib.request import urlopen
from bs4 import BeautifulSoup
from my_util import make_dir

base_url = 'https://www.sciencetimes.co.kr/?cat=35&post_type=news&paged='
output_dir = 'C:/pro/data/stimes/'
make_dir(output_dir)
output_file = output_dir + 'stimes_1173.txt'
missed_output_link = output_dir + 'stimes_missed.txt'

def get_stimes_content():
	for i in range(1173, 2209):
		url = base_url + str(i)
		html = urlopen(url)
		soup = BeautifulSoup(html, "html.parser")
		link_data = soup.find_all('a', class_='main-headline')
		total_txt = ''
		missed_link = ''
		for link_datum in link_data:
			link = link_datum["href"]
			page = urlopen(link)
			page_soup = BeautifulSoup(page, "html.parser")
			article = page_soup.find('div', class_='resize')
			try:
				total_txt = total_txt + article.get_text() + '\n'
			except AttributeError:
				missed_link = missed_link + link + '\n'
		with open(output_file, 'a', encoding='utf-8') as output:
			output.write(total_txt + '\n')
			print("index num {} saved".format(i))
		if missed_link != '':
			with open(missed_output_link, 'a', encoding='utf-8') as output:
				output.write(missed_link + '\n')



if __name__ == '__main__':
	get_stimes_content()
