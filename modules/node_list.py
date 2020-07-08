#!/usr/bin/env python3 
import random, string

class NodeList:
	""" NodeList : returns input data into CSV, creates nodes and edges tables"""
	nodes_table = []
	edges_table = []
	discovered_websites = []


	@classmethod
	def push(self, node):

		default = {
			'uri' : node.uri,
		}

		if(self._if_exists(node.uri)):
			default['id'] = self._get_node_by_name(node.uri)['id']
		else:
			default['id']  = self._generate_UID()
		
		if(node.misc):
			default['misc'] = node.misc

		self.discovered_websites.append(node.uri)
		self.nodes_table.append(default)

		base_node = self._get_node_by_name(node.uri)

		for edge in node.edges:
			if(self._if_exists(edge) != True):
				_uuid = self._generate_UID()

				self.edges_table.append({
					'source' : base_node['id'],
					'target' : _uuid,
				})
				self.nodes_table.append({
						'uri' : edge,
						'id'  : _uuid
				})
				self.discovered_websites.append(edge)
			else:
				target = self._get_node_by_name(edge)
				self.edges_table.append({
					'source' : base_node['id'],
					'target' : target['id']
				})

	def _generate_UID():
		return ''.join(random.choices(string.digits, k=8))

	@classmethod
	def _if_exists(self, uri):
		for site in self.discovered_websites:
			if(site == uri):
				return True
		return False
	@classmethod
	def _get_node_by_name(self,name):
		for site in self.nodes_table:
			if(site['uri'] == name):
				return site
	
	@classmethod
	def _get_node_by_id(uid):
		for site in self.nodes_table:
			if(site['id'] == uid):
				return site