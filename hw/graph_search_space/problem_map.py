from edge import Edge
from queue import Queue
from collections import namedtuple

class Map():
    WALL = -1
    
    def __init__(self, rows: int, cols: int, wall_coords:list[tuple[int]]):
        self.rows = rows
        self.cols = cols
        self.costs = [[14, 10, 14], 
                      [10, 00, 10],
                      [14, 10, 14]]
        
        self.wall_coords = wall_coords
        self.map = self._generate_map()
        self.g = self._generate_adjacency_list()


    def _generate_map(self):
        map = [[0 for y in range(self.cols)] for x in range(self.rows)]

        for coord_pair in self.wall_coords:
            x, y = coord_pair
            map[x][y] = Map.WALL

        return map

    
    def _generate_adjacency_list(self):
        g = [[] for x in range(self.rows * self.cols)]

        for i in range(self.rows * self.cols):
            row = i // self.cols
            col = i % self.cols

            if not (row, col) in self.wall_coords:    
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if not (x == 0 and y == 0):
                            try:
                                if row + x < 0 or col + y < 0:
                                    raise IndexError

                                if self.map[row + x][col + y] != Map.WALL:
                                    g[i].append(Edge(self.costs[x + 1][y + 1], (row + x) * self.cols + (col + y)))
                            except IndexError:
                                continue

        return g
    
    
    def depth_first_search(self, cur: tuple[int], target: tuple[int], visited = None, path = None, cost = 0):
        visited = visited if visited is not None else [False for i in range(self.rows * self.cols)]
        path = path if path is not None else []

        path.append(cur)

        x, y = cur
        cur_val = x * self.cols + y 

        visited[cur_val] = True

        if cur == target:
            self._print_path(path, cost)


        for i in range(len(self.g[cur_val])):
            e = self.g[cur_val][i]
            next = e.get_to()

            if not visited[next]:
                cost += e.get_costFrom()
                self.depth_first_search((next // self.cols, next % self.cols), target, visited, path, cost)


    def breadth_first_search(self, cur: tuple[int], target: tuple[int]):
        visited = [False for i in range(self.rows * self.cols)]
        path = []
        cost = 0
        queue = Queue()

        path.append(cur)

        x, y = cur
        cur_val = x * self.cols + y

        visited[cur_val] = True
        queue.put(cur_val)

        if (cur_val // self.cols, cur_val % self.cols) == target:
                self._print_path(path, cost)
                return

        while not queue.empty():
            cur_val = queue.get()
            edges = self.g[cur_val]
            
            for e in edges:
                next = e.get_to()

                if not visited[next]:
                    visited[next] = True
                    path.append((next // self.cols, next % self.cols))
                    cost += e.get_costFrom()
                    queue.put(next)

                    if (next // self.cols, next % self.cols) == target:
                        self._print_path(path, cost)
                        return
                    

    def astar(self, start: tuple[int], target: tuple[int]):
        if (start == target):
            return start

        open_queue = []
        closed_queue = []

        Node = namedtuple('Node',
                        ('cur', 'parent', 'fscore', 'gscore', 'hscore'))

        # while there is a node in the closed list where the parent is the current node:
        #     current node = that node in question
        #     path.append(current node)

        c = Node(start, (-1, -1), 0, 0, 0)
        open_queue.append(c)

        while len(open_queue) != 0:
            # remove node with lowest fscore
            c :Node = min(open_queue, key=lambda node: node.fscore)
            open_queue.remove(c)

            # if c.cur == target:
            #     return self._trace_path(closed_queue, c)

            # add c to closed queue
            closed_queue.append(c)
            
            # traverse through all connections in adjacency list (none of them are walls)
            cur_val = c.cur[0] * self.cols + c.cur[1]

            for i in range(len(self.g[cur_val])):
                next:Edge = self.g[cur_val][i]
                nx, ny = next.get_to() // self.cols, next.get_to() % self.cols

                # gets cost, which is stored in the next variable (of type Edge)
                n_gscore = next.get_costFrom()
                # calculates Manhattan distance
                n_hscore = abs(nx - target[0]) + abs(ny - target[1])
                n_fscore = n_gscore + n_hscore

                # format n to be a Node, set parent to node c 
                n = Node((nx, ny), c.cur, n_fscore, n_gscore, n_hscore)

                # if this node is the target, trace the path
                if n.cur == target:
                    return self._trace_path(closed_queue, n)
                

                # finding out whether or not node is already on the closed queue
                for node in closed_queue:
                    if node.cur == n.cur:
                        node_visited = True
                        break
                else:
                    node_visited = False

                if not node_visited:
                    # if n is on the open queue and its new f score is less than the f score on the open queue, replace it
                    # otherwise append it to the open queue
                    for node in open_queue:
                        if node.cur == n.cur and n.fscore < node.fscore:
                            open_queue.pop(open_queue.index(node))
                            open_queue.append(n)
                            break
                    else:
                        open_queue.append(n)

    
    def _trace_path(self, closed_queue, n):
        path = [n.cur]
        path_cost = n.gscore
        path_complete = False

        while not path_complete:
            for node in closed_queue:
                if node.cur == n.parent:
                    n = node
                    path.append(n.cur)
                    path_cost += n.gscore
                    break
            else:
                path_complete = True
                self._print_path(path[::-1], path_cost)
                return


    def _print_path(self, path: list, cost: int):
        print("PATH:")
        for i in range(len(path)):
            cp = path[i]
            print(f'{cp} -> ' if i != len(path) - 1 else f'{cp}', end="")
        
        print()
        print("COST:")
        print(cost)

    
    def get_adj_list(self):
        return self.g