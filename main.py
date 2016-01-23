

def read_file(filename):
	with open(filename) as f:
		numGraphs = int(f.readline().rstrip('\n'))
		print(numGraphs)
		for g in range(numGraphs):
			graphSize = int(f.readline().rstrip('\n'))
			numEdges = int(f.readline().rstrip('\n'))
			graph = Graph(numEdges, graphSize)

			for l in range(numEdges):
				e = f.readline()
				u,v = [int(i) for i in e.split()]
				graph.addEdge(u,v)
			graph.displayGraph()
			graph.shortestPath()



class Graph(object):

	def __init__(self, numEdges, size):
		self.size = size
		self.edges = [None]
		for i in range(1,size+1):
			self.edges.insert(i,{None})

	def addEdge(self, u, v):
		self.edges[u].add(v)

	def displayGraph(self):
		for e in self.edges:
			print(str(e)+": ")

	def shortestPath(self):
		dist = [float('inf')] * (self.size+1)
		dist[1] = 0
		for v in range(1,self.size):
			print(v)
		print(str(dist))

	def longestPath(self):
		pass

	def numPaths(self):
		pass

def main():
	read_file("inSmall.txt")

if __name__ == '__main__':
	main()
