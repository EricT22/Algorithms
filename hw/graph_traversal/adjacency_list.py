from queue import Queue

class adj_list():
    def __init__(self, n, directed=False) -> None:
        self.list = [[] for x in range(n)]
        self.directed = directed


    def add_edge(self, v, w):
        if self.directed:
            self.list[v - 1].append(w)
        else:
            self.list[v - 1].append(w)
            self.list[w - 1].append(v)

    
    def get_list(self):
        return self.list


    @staticmethod
    def depth_first(list, v, visited=None):
        visited = visited if visited is not None else [False for x in range(len(list))]

        print(f'Visiting node {v}')

        visited[v - 1] = True

        for i in range(len(list[v - 1])): # number of nodes connected to current node
            if not visited[list[v - 1][i] - 1]:
                adj_list.depth_first(list, list[v - 1][i], visited)


    @staticmethod
    def breadth_first(list, v):
        visited = [False for x in range(len(list))]
        queue = Queue()

        print(f'Visiting node {v}')
        visited[v - 1] = True
        queue.put(v)

        while not queue.empty():
            x = queue.get()

            for i in range(len(list[x - 1])):
                w = list[x - 1][i]

                if not visited[w - 1]:
                    print(f'Visiting node {w}')
                    visited[w - 1] = True
                    queue.put(w)