from adjacency_matrix import adj_mat
from adjacency_list import adj_list
from build_graphs import *


if __name__ == "__main__":
    ma, mb, mc, md = build_matricies()
    la, lb, lc, ld = build_lists()
    starting_node = 1

    print("ADJACENCY MATRIX DEPTH FIRST")
    print(f'{"*" * 20}\nA)\n')
    adj_mat.depth_first(ma, starting_node)
    print(f'{"-" * 20}\nB)\n')
    adj_mat.depth_first(mb, starting_node)
    print(f'{"-" * 20}\nC)\n')
    adj_mat.depth_first(mc, starting_node)
    print(f'{"-" * 20}\nD)\n')
    adj_mat.depth_first(md, starting_node)
    print(f'{"-" * 20}')


    print("ADJACENCY LIST DEPTH FIRST")
    print(f'{"*" * 20}\nA)\n')
    adj_list.depth_first(la, starting_node)
    print(f'{"-" * 20}\nB)\n')
    adj_list.depth_first(lb, starting_node)
    print(f'{"-" * 20}\nC)\n')
    adj_list.depth_first(lc, starting_node)
    print(f'{"-" * 20}\nD)\n')
    adj_list.depth_first(ld, starting_node)
    print(f'{"-" * 20}')


    print("ADJACENCY MATRIX BREADTH FIRST")
    print(f'{"*" * 20}\nA)\n')
    adj_mat.breadth_first(ma, starting_node)
    print(f'{"-" * 20}\nB)\n')
    adj_mat.breadth_first(mb, starting_node)
    print(f'{"-" * 20}\nC)\n')
    adj_mat.breadth_first(mc, starting_node)
    print(f'{"-" * 20}\nD)\n')
    adj_mat.breadth_first(md, starting_node)
    print(f'{"-" * 20}')


    print("ADJACENCY LIST BREADTH FIRST")
    print(f'{"*" * 20}\nA)\n')
    adj_list.breadth_first(la, starting_node)
    print(f'{"-" * 20}\nB)\n')
    adj_list.breadth_first(lb, starting_node)
    print(f'{"-" * 20}\nC)\n')
    adj_list.breadth_first(lc, starting_node)
    print(f'{"-" * 20}\nD)\n')
    adj_list.breadth_first(ld, starting_node)
    print(f'{"-" * 20}')