class UnionFind(object):
	def __init__(self):
		self.set = []
		self.representative = dict()

	def connected_components(self, graph):
		for node in graph.nodes:
			self.make_set(node)
		for edge in graph.edges:
			if self.find_set(edge[0]) != self.find_set(edge[1]):
				self.union(self.find_set(edge[0]), self.find_set(edge[1]))

	def make_set(self, node): # crea un nuovo insieme Si
		s = set([node])  # insiemi disgiunti nodi
		if s not in self.set:
			self.set.append(s)  # S = Si U {x}
			self.representative.update({node: s})
		
	def union(self, x, y):
		Sx = set()
		Sy = set()
		for element in self.set:
			if x in element: Sx = element
			if y in element: Sy = element
		tmp = set().union(Sx, Sy)
		if Sx is not None: self.set.remove(Sx)
		if Sy is not None: self.set.remove(Sy)
		self.set.append(tmp)
		self.representative.pop(self.__getrepr__(x))	#update representative
		self.representative.pop(self.__getrepr__(y))
		self.representative.update({x: set(tmp)})
				

	def print_set(self):
		print(self.set)

	def print_representative(self):
		print(self.representative)

	def find_set(self, x): # return representative of set that contains x
		for key in self.representative:
			if x in self.representative[key]:
				return key

	def __getrepr__(self, x):
		for key in self.representative:
			if x in self.representative[key]: return key

