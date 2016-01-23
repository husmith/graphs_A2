import fileinput

class Graph(object):

	def __init__(self, numEdges, size):
		self.size = size
		self.edges = [None]
		for i in range(1,size+1):
			self.edges.insert(i,set())

	def addEdge(self, u, v):
		self.edges[u].add(v)

	def displayGraph(self):
		for v in range(self.size):
			print(str(v)+" vertex: ",end="")
			for e in self.edges[v]:
				print(str(e),end=" ")
			print("\n")

	def displayGraphInfo(self, number):
		shortest_path = self.shortestPath()
		longest_path = self.longestPath()
		num_paths = self.numPaths()
		print("graph number: "+str(number))
		print("shortest path: "+str(shortest_path))
		print("longest path: "+str(longest_path))
		print("number of paths: "+str(num_paths))

	def shortestPath(self):
		dist = [float('inf')] * (self.size+1)
		dist[1] = 0
		for v in range(1,self.size):
			for u in self.edges[v]:
				if u == None:
					break
				if dist[u] > (dist[v] + 1):
					dist[u] = dist[v] + 1
		return dist[self.size]

	def longestPath(self):
		dist = [-1] * (self.size+1)
		dist[1] = 0
		for v in range(1,self.size):
			for u in self.edges[v]:
				if u == None:
					break
				if dist[u] < (dist[v] + 1):
					dist[u] = dist[v] + 1
		return dist[self.size]

	def numPaths(self):
		numPaths = 0
		paths = [0] * (self.size+1)
		paths[1] = 1
		for v in range(1,self.size):
			for u in self.edges[v]:
				paths[u] += paths[v]
		numPaths = paths[self.size]
		return numPaths



def main():

	with fileinput.input() as f:
		numGraphs = int(f.readline().rstrip('\n'))

		for g in range(numGraphs):
			gSize = int(f.readline().rstrip('\n'))
			gEdges = int(f.readline().rstrip('\n'))
			graph = Graph(gEdges, gSize)

			for l in range(gEdges):
				e = f.readline()
				u,v = [int(i) for i in e.split()]
				graph.addEdge(u,v)

			graph.displayGraphInfo(g+1)
			print("\n")
	fileinput.close()

if __name__ == '__main__':
	main()
