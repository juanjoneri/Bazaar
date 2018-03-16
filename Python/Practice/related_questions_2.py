from sys import stdin

class Graph:
    def __init__(self, nodes, weights):
        self.nodes = set(nodes)
        self.g = {n: (w, []) for n, w in zip(nodes, weights)}
        self.known_depths = dict()

    def add_edge(self, n1, n2):
        self.children(n1).append(n2)
        self.children(n2).append(n1)

    def children(self, node):
        return self.g[node][1]

    def weight(self, node):
        return self.g[node][0]

    def depth(self, start_node, visited=[]):
        meta = (start_node, tuple(sorted(visited)))
        if meta not in self.known_depths:
            visited.append(start_node)
            max_depth = 0
            for child in self.children(start_node):
                if child not in visited:
                    max_depth = max(max_depth, self.depth(child, visited))
            visited.pop()        
            self.known_depths[meta] = self.weight(start_node) + max_depth
        
        return self.known_depths[meta]

    def __str__(self):
        return str(self.g)

if __name__ == '__main__':
    # Number of questions
    N = int(stdin.readline())
    questions = set(range(1, N+1))
    # Time to read each question
    times = list(map(int, stdin.readline().split()))
    # Make  list of question where the index in the list matchese the index of the question
    
    graph = Graph(questions, times)
    for line in stdin:
        q1, q2 = tuple(map(int, line.split()))
        graph.add_edge(q1, q2)

    depths = [(q, graph.depth(q)) for q in graph.nodes]
    print(min(depths, key=lambda x: x[1])[0])