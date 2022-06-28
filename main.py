import os
import requests
from bs4 import BeautifulSoup

def get_all_pages():
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
	}

	r = requests.get(url='https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/', headers=headers)

	if not os.path.exists('data'):
		os.mkdir('data')

	with open('data/page_1.html', 'w') as file:
		file.write(r.text)


def main():
	get_all_pages()

if __name__ == '__main__':
	main()