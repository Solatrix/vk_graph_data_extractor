#!/usr/bin/env python3 

import asyncio
from requests_html import AsyncHTMLSession
import pyppdf.patch_pyppeteer

class Spider():
	"""Spider : crawling every link and returning async data"""
	link = str

	@classmethod
	def __init__(self,opt):
		self.opts = opt
		self.asession = AsyncHTMLSession()

	@classmethod
	async def crawl(self,link):
		self.link = link
		try:
			page = await self.asession.get(self.link,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2810.1 Safari/537.36'},verify=True)
		except Exception as e:
			raise e
			print(e)
		if(self.opts['AllowJS']):
			try:
				await page.html.arender()
				return page
			except Exception as e:
				raise e
		else:
			return page

	# En améliorant l'appel de la méthode avec une seule ligne en opération ternaire
	# on n'a plus besoin d'arrêter le script si user_filter n'est pas nul
	# les opérations peuvent se suivre 
	# vérifier si data garde tout le contenu de la page, même après l'utilisation de find
	@classmethod
	def filter(self, data, user_filter=None):
		r = []
		if(user_filter):
			for ufilter in user_filter:
				temp = data.html.find(ufilter)

				return temp[0].text if len(temp) > 1 else None
		else:
			for filter in self.opts['hyperlinks_selector']:
				r.append(data.html.find(filter))
		return r

	@classmethod
	async def destroySession(self):
		await self.asession.close()