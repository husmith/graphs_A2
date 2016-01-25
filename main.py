import fileinput
"""
Name: Hannah Smith
Date: January 25, 2016
Class: CIS 315 Intermediate Algorithms
"""


class Graph(object):

	def __init__(self, numEdges, size):
		""" Init graph size and an adjacency list representation. The adjacency
		list indexes correspond to the vertices, and each index is initialized
		to contain an empty set.
		:param numEdges: the number of edges in the graph.
		:param size: the size (number of nodes) in the graph.
		"""
		self.size = size
		self.graph = [None]
		for i in range(1,size+1):
			self.graph.insert(i,set())

	def addEdge(self, u, v):
		""" Adds a edge to the adjacency list representation of the graph.
		The vertex v will be added to the set of connected vertices for vertex u.
		:param u: the source vertex of the edge.
		:param v: the destination vertex of the edge.
		"""
		self.graph[u].add(v)

	def displayGraph(self):
		""" Prints graph representation in form V vertex: e1 e2
		where V is the node and e are the connected nodes.
		"""
		for v in range(self.size):
			print(str(v)+" vertex: ",end="")
			for e in self.graph[v]:
				print(str(e),end=" ")
			print("\n")

	def displayGraphInfo(self, number):
		""" Prints the shortest path, longest path, and number of paths in the graph.
		:param number: the number identifying the graph to display.
		"""
		shortest_path = self.shortestPath()
		longest_path = self.longestPath()
		num_paths = self.numPaths()
		print("graph number: "+str(number))
		print("shortest path: "+str(shortest_path))
		print("longest path: "+str(longest_path))
		print("number of paths: "+str(num_paths))

	def shortestPath(self):
		""" Returns the shortest path found from the source node (1) to the nth node.
		:returns: the shortest distance to the last node in the graph.
		"""
		dist = [float('inf')] * (self.size+1)
		dist[1] = 0
		for v in range(1,self.size):
			for u in self.graph[v]:
				if u == None:
					break
				if dist[u] > (dist[v] + 1):
					dist[u] = dist[v] + 1
		return dist[self.size]

	def longestPath(self):
		""" Returns the longest path found from the source node (1) to the nth node.
		:returns: the longest distance from node 1 to the last node (n) in the graph.
		"""
		dist = [-1] * (self.size+1)
		dist[1] = 0
		for v in range(1,self.size):
			for u in self.graph[v]:
				if u == None:
					break
				if dist[u] < (dist[v] + 1):
					dist[u] = dist[v] + 1
		return dist[self.size]

	def numPaths(self):
		""" Finds the total number of paths from the source node (1) to the nth node.
		:returns: the number of unique paths from node 1 to the last node (n) in the graph.
		"""
		numPaths = 0
		paths = [0] * (self.size+1)
		paths[1] = 1
		for v in range(1,self.size):
			for u in self.graph[v]:
				paths[u] += paths[v]
		numPaths = paths[self.size]
		return numPaths



def main():
	# fileinput.input() will read from stdin if no file is found
	with fileinput.input() as f:
		# Read the first line, which gives the number of graphs to follow
		numGraphs = int(f.readline().rstrip('\n'))

		# Initialize each graph
		for g in range(numGraphs):
			gSize = int(f.readline().rstrip('\n'))
			gEdges = int(f.readline().rstrip('\n'))
			graph = Graph(gEdges, gSize)

			# Add the edges read from input to the graph created
			for l in range(gEdges):
				e = f.readline()
				u,v = [int(i) for i in e.split()]
				graph.addEdge(u,v)

			# Display the results from the graph, assigning a number > 0 to the graph
			graph.displayGraphInfo(g+1)
			print("\n")
	fileinput.close()

if __name__ == '__main__':
	main()
