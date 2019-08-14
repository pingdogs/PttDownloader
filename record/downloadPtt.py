from .models import *
import requests
from requests_html import HTML
import arrow
from django.db.utils import IntegrityError


def task():
	print('Task Start')
	keywords = KeyWord.objects.all()
	for keyword in keywords:
		pttdownloader = Pttdownloader(key=keyword.name, categories=keyword.categories.all())
		pttdownloader.download()
	print('Task End')




class Pttdownloader:
	def __init__(self, key, categories):
		self.num_of_article = 200
		self.key = key
		self.categories = categories
	def download(self):
		for category in self.categories:
			articles = self.downloadAticles(category)
			for article in articles:
				date = article['date'][4:]
				try:
				    pushes = int(article['pushes'])
				except:
				    if article['pushes'] == '爆':
				    	pushes = 100
				    else:
				    	pushes = -100
				# print(date)
				# date = arrow.get(date, 'MMM D HH:mm:ss YYYY')
				try:
					a = Article(title=article['title'], category=category, date=date, pushes=pushes, author=article['author'], content=article['content'])
					a.save()
				except IntegrityError:
					a = Article.objects.get(title=article['title'], date=date, author=article['author'])
					a.content = article['content']
					a.pushes = pushes
					a.save()

			# filter_articles = self.filter_by_key(articles)
	def downloadAticles(self, category):
		total = 0
		page_url = category.url
		articles = []

		while total < self.num_of_article:
			response = self.fetch(page_url)
			post_entries, controls = self.parse_article_entries(response.text)
			link = controls[1].attrs['href']
			page_url = 'https://www.ptt.cc' + link
			for index, entry in enumerate(post_entries):
				meta = self.parse_article_meta(entry)
				pretty_print(meta['pushes'], meta['title'], meta['date'], meta['author'])
				if 'link' in meta.keys():
					res = self.fetch('https://www.ptt.cc' + meta['link'])
					total += 1
					mt = self.parse_article_content(res.text)
					if not mt:
						continue
					mt['pushes'] = meta['pushes']
					mt['author'] = meta['author']
					mt['title'] = meta['title']
					if self.check_if_contain_key(mt):
						articles.append(mt)
					if not total < self.num_of_article:
						break
		return articles
			   

	def fetch(self, url):
	    response = requests.get(url)
	    response = requests.get(url, cookies={'over18': '1'}) 
	    return response

	def parse_article_meta(self, entry):
		meta = {
	        'title': entry.find('div.title', first=True).text,
	        'pushes': entry.find('div.nrec', first=True).text,
	        'date': entry.find('div.date', first=True).text,
	    }

		try:
			meta['author'] = entry.find('div.author', first=True).text
			meta['link'] = entry.find('div.title > a', first=True).attrs['href']
		except AttributeError:
			pass
		return meta
	def parse_article_entries(self, doc):
		html = HTML(html=doc)

		post_entries = html.find('div.r-ent')
		controls = html.find('.action-bar a.btn.wide')
		return post_entries, controls

	def parse_article_content(self, doc):
		html = HTML(html=doc)
		meta = {}
		try:
			meta['date'] = html.find('span.article-meta-value')[3].text
		except:
			return None
		meta['content'] = html.find('div#main-content', first=True).text
		# print(meta['date'])
		return meta
	def check_if_contain_key(self, entry):
		return self.key in entry['title'] or self.key in entry['content']


widths = [
        (126,    1), (159,    0), (687,     1), (710,   0), (711,   1),
        (727,    0), (733,    1), (879,     0), (1154,  1), (1161,  0),
        (4347,   1), (4447,   2), (7467,    1), (7521,  0), (8369,  1),
        (8426,   0), (9000,   1), (9002,    2), (11021, 1), (12350, 2),
        (12351,  1), (12438,  2), (12442,   0), (19893, 2), (19967, 1),
        (55203,  2), (63743,  1), (64106,   2), (65039, 1), (65059, 0),
        (65131,  2), (65279,  1), (65376,   2), (65500, 1), (65510, 2),
        (120831, 1), (262141, 2), (1114109, 1),
]


def calc_len(string):
    def chr_width(o):
        global widths
        if o == 0xe or o == 0xf:
            return 0
        for num, wid in widths:
            if o <= num:
                return wid
        return 1
    return sum(chr_width(ord(c)) for c in string)


def pretty_print(push, title, date, author):
    pattern = '%3s\t%s%s%s\t%s'
    padding = ' ' * (50 - calc_len(title))
    print(pattern % (push, title, padding, date, author))


