#!/usr/bin/env python3 
import asyncio
from modules.spider import Spider
from modules.node_list import NodeList
from modules.node import Node
from modules.file_manager import FileManager
class Scraper():
	
	options = {
		'source' : '',
		'threading' : False,
		'AllowJS' : False,
		'hyperlinks_selector' : [],
		'other_data' : [],
		'output' : {
			'type' : 'graph'
		}
	}
	nodelist = NodeList()

	@classmethod
	def __init__(self, options={}):

		self.options.update(options)
		self.loop = asyncio.get_event_loop()
		self.filemanager = FileManager(self.options['output'])
		asyncio.run(self.main())
	
	@classmethod
	async def main(self):
		try:
			sites = open(self.options['source'], 'r')
			lines = sites.readlines()
			spid = Spider(self.options)
			for site in lines:
				site = site.rstrip()

				try:
					crawler = spid.crawl(site)
					print(f'Crawling : {site}')
					data = await crawler

					# Améliorable : on peut set la valeur du filtre personnalisé (pas pour les liens), à la valeur assignée en options
					# sinon, on garde la valeur None
					ufilter = self.options['other_data'] if len(self.options['other_data']) > 0 else None
					user_data = spid.filter(data,ufilter)

					hyperlinks = spid.filter(data)

					print(f'Parsing data')

					if(hyperlinks):
						if(ufilter and user_data):
							self.nodelist.push(Node(site, hyperlinks,user_data))
						else:
							self.nodelist.push(Node(site, hyperlinks))
						print(f'Found links in {site}')
					else:
						print(f'No links were found in {site}, continuing crawling')
						continue

					data.close()
				except Exception as e:
					raise e
					print(e)
					print(f"An error occured whilst crawling : {site}")

			await spid.destroySession()

			nodes = self.nodelist.nodes_table
			edges = self.nodelist.edges_table

			self.filemanager.export_to_csv(nodes,edges)

		except Exception as e:
			raise e
			print(f"Input error : no website has been carwled")

VKScraper = Scraper({
	'source':'sites.txt',
	'threading' : True,
	'AllowJS' : True,
	'hyperlinks_selector' : ["aside div#public_links a[href]","div#group_links a[href]"],
	'other_data' : ["span.header_count"],
	'output' : {
		'type' : 'graph',
		'nodes' : ['id','uri','group_members']
	}
})