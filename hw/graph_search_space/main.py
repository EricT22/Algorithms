from problem_map import Map

def print_adj_list(map: Map):
    g = map.get_adj_list()

    count = 0
    for row in g:
        print(f"Node {count}:")
        for edge in row:
            print(edge, end='\t')

        print()
        count+=1


if __name__ == "__main__":
    wall_coords = [(1, 3), (2, 3), (3, 3)]
    rows = 5
    cols = 7
    start = (2, 1)
    end = (2, 5)
    map = Map(rows, cols, wall_coords)

    print("Depth First Search:")
    map.depth_first_search(start, end)
    print(f'{'=' * 150}')

    print("Breadth First Search:")
    map.breadth_first_search(start, end)
    print(f'{'=' * 150}')

    print("Best First Search (A*):")
    map.astar(start, end)
    print(f'{'=' * 150}')