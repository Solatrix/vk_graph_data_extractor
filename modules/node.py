#!/usr/bin/env python3 
from urllib.parse import unquote
class Node:
	""" Node """
	opts = {
		"separator" : ["://","vk.com/away.php?to="],
		"url_decode" : True,
		"allow_params" : False
	}

	@classmethod
	def __init__(self, source, edges=[],misc=None):
		self.uri = self.clean(source)
		self.edges = self.clean(edges)
		self.misc = misc
	
	@classmethod
	def clean(self,links):
		r = []
		if(type(links) == list):
			for link in links:
				if(len(link) > 0):
					for a in link:
						a = a.absolute_links
						hyperlink = ''.join(a)
						hyperlink = self._url_decode(hyperlink)
						hyperlink = self._split_by_301(hyperlink)
						hyperlink = ''.join(hyperlink)
						hyperlink = hyperlink.strip('/')
						hyperlink = hyperlink.rstrip()
						r.append(hyperlink)
			r = self._remove_doubles(r)
			return r

		elif(type(links) == str):
			link = self._url_decode(links)		
			link = self._split_by_301(link)
			link = ''.join(link)
			link = link.strip('/')
			link = link.rstrip()
			return link
		
	def _url_decode(uri):
		return unquote(uri)

	def _remove_doubles(links):
		return list(set(links))

	@classmethod
	def _split_by_301(self,link):
		
		for pattern in self.opts['separator']:
			attempt = link.split(pattern, 1)
			if(len(attempt) > 1):
				link = attempt[1]
		return link