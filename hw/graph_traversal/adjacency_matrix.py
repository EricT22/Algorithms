from queue import Queue

class adj_mat():
    def __init__(self, n, directed=False) -> None:
        self.mat = [[0 for x in range(n)] for y in range(n)]
        self.directed = directed


    def add_edge(self, v, w):
        if self.directed:
            self.mat[v - 1][w - 1] = 1
        else:
            self.mat[v - 1][w - 1] = 1
            self.mat[w - 1][v - 1] = 1

    
    def get_mat(self):
        return self.mat


    @staticmethod
    def depth_first(mat, v, visited=None):
        visited = visited if visited is not None else [False for x in range(len(mat))]

        print(f'Visiting node {v}')

        visited[v - 1] = True

        for i in range(len(mat)): # number of nodes
            if mat[v - 1][i] == 1 and not visited[i]:
                adj_mat.depth_first(mat, i + 1, visited)


    @staticmethod
    def breadth_first(mat, v):
        visited = [False for x in range(len(mat))]
        queue = Queue()

        print(f'Visiting node {v}')
        visited[v - 1] = True
        queue.put(v)

        while not queue.empty():
            x = queue.get()

            for w in range(len(mat)): # of nodes
                if mat[x - 1][w] == 1 and not visited[w]:
                    print(f'Visiting node {w + 1}')
                    visited[w] = True
                    queue.put(w + 1)