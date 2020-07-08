import csv
class FileManager:
	""" File Manager """
	output = {
		"type" : "graph",
		"nodes" : ['id','uri'],
		"edges" : ['source','target']
	}

	@classmethod
	def __init__(self,output):
		self.output.update(output)

	@classmethod
	def export_to_csv(self,nodes,edges,format='csv'):

		with open('exports/nodes.csv', "w") as f:
			
			for entry in self.output['nodes']:
				f.write(f'{entry},')
			f.write("\n")

			for node in nodes:
				f.write(f"{node['id']},{node['uri']},")
				if('misc' in node and len(self.output['nodes']) > 2):
					f.write(f"{node['misc'].replace(',','')},")
				else:
					f.write(',')
				f.write("\n")
			f.close()
			print('Nodes written successfuly to exports/nodes.csv')

		with open('exports/edges.csv', "w") as e:
			
			for entry in self.output['edges']:
				e.write(f'{entry},')
			e.write("\n")


			for edge in edges:
				e.write(f"{edge['source']},{edge['target']},\n")
			e.close()
			print('Edges written successfuly to exports/edges.csv')