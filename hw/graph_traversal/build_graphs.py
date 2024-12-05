from adjacency_matrix import adj_mat
from adjacency_list import adj_list

def build_matricies():
    MA = adj_mat(7)
    MA.add_edge(1, 2)
    MA.add_edge(1, 4)
    MA.add_edge(2, 5)
    MA.add_edge(2, 7)
    MA.add_edge(3, 4)
    MA.add_edge(3, 6)
    MA.add_edge(3, 7)
    MA.add_edge(4, 5)
    MA.add_edge(5, 6)
    MA.add_edge(5, 7)

    MB = adj_mat(7)
    MB.add_edge(1, 4)
    MB.add_edge(1, 5)
    MB.add_edge(2, 3)
    MB.add_edge(2, 4)
    MB.add_edge(3, 4)
    MB.add_edge(4, 7)
    MB.add_edge(5, 6)
    MB.add_edge(6, 7)

    MC = adj_mat(7, directed=True)
    MC.add_edge(1, 2)
    MC.add_edge(1, 4)
    MC.add_edge(1, 5)
    MC.add_edge(2, 3)
    MC.add_edge(2, 4)
    MC.add_edge(2, 7)
    MC.add_edge(3, 4)
    MC.add_edge(4, 6)
    MC.add_edge(4, 7)
    MC.add_edge(5, 4)
    MC.add_edge(6, 5)
    MC.add_edge(7, 6)

    MD = adj_mat(7, directed=True)
    MD.add_edge(1, 2)
    MD.add_edge(1, 4)
    MD.add_edge(1, 5)
    MD.add_edge(2, 3)
    MD.add_edge(3, 7)
    MD.add_edge(4, 2)
    MD.add_edge(4, 3)
    MD.add_edge(4, 6)
    MD.add_edge(4, 7)
    MD.add_edge(5, 4)
    MD.add_edge(6, 7)
    
    return (MA.get_mat(), MB.get_mat(), MC.get_mat(), MD.get_mat())


def build_lists():
    LA = adj_list(7)
    LA.add_edge(1, 2)
    LA.add_edge(1, 4)
    LA.add_edge(2, 5)
    LA.add_edge(2, 7)
    LA.add_edge(3, 4)
    LA.add_edge(3, 6)
    LA.add_edge(3, 7)
    LA.add_edge(4, 5)
    LA.add_edge(5, 6)
    LA.add_edge(5, 7)

    LB = adj_list(7)
    LB.add_edge(1, 4)
    LB.add_edge(1, 5)
    LB.add_edge(2, 3)
    LB.add_edge(2, 4)
    LB.add_edge(3, 4)
    LB.add_edge(4, 7)
    LB.add_edge(5, 6)
    LB.add_edge(6, 7)

    LC = adj_list(7, directed=True)
    LC.add_edge(1, 2)
    LC.add_edge(1, 4)
    LC.add_edge(1, 5)
    LC.add_edge(2, 3)
    LC.add_edge(2, 4)
    LC.add_edge(2, 7)
    LC.add_edge(3, 4)
    LC.add_edge(4, 6)
    LC.add_edge(4, 7)
    LC.add_edge(5, 4)
    LC.add_edge(6, 5)
    LC.add_edge(7, 6)

    LD = adj_list(7, directed=True)
    LD.add_edge(1, 2)
    LD.add_edge(1, 4)
    LD.add_edge(1, 5)
    LD.add_edge(2, 3)
    LD.add_edge(3, 7)
    LD.add_edge(4, 2)
    LD.add_edge(4, 3)
    LD.add_edge(4, 6)
    LD.add_edge(4, 7)
    LD.add_edge(5, 4)
    LD.add_edge(6, 7)
    
    return (LA.get_list(), LB.get_list(), LC.get_list(), LD.get_list())