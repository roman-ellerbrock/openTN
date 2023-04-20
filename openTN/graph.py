class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.children = []
        self.parents = []

class Edge:
    def __init__(self, node_1, node_2):
        self.node_1 = node_1
        self.node_2 = node_2

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.next_node_id = 0
        self.next_edge_id = 0

    def add_node(self, node):
        node.id = self.next_node_id
        self.next_node_id += 1
        self.nodes.append(node)
        return node.id

    def add_edge(self, edge):
        edge.id = self.next_edge_id
        self.next_edge_id += 1
        self.edges.append(edge)

        edge.node_1.children.append(edge.node_2)
        edge.node_2.parents.append(edge.node_1)

        return edge.id

    def get_children(self, node_id):
        node = self.get_node_by_id(node_id)
        return node.children

    def get_parents(self, node_id):
        node = self.get_node_by_id(node_id)
        return node.parents

    def get_neighbors(self, node_id):
        neighbors = []
        for edge in self.edges:
            if edge.node_1.id == node_id:
                neighbors.append(edge.node_2)
            elif edge.node_2.id == node_id:
                neighbors.append(edge.node_1)
        return neighbors

    def get_node_by_id(self, node_id):
        if node_id >= len(self.nodes):
            raise ValueError(f"No node found with id {node_id}")
        return self.nodes[node_id]

    def get_edge_by_id(self, edge_id):
        if edge_id >= len(self.edges):
            raise ValueError(f"No edge found with id {edge_id}")
        return self.edges[edge_id]


def generate_balanced_tree(n):
    """
    Generates a close-to-balanced tree with n nodes using the Graph class.

    Args:
        n (int): Number of nodes in the tree.

    Returns:
        Graph: A close-to-balanced tree with n nodes.
    """

    # Create an empty graph.
    graph = Graph()

    # Add the root node.
    root = Node(0)
    graph.add_node(root)

    # Add the child nodes.
    for i in range(1, n):
        parent_id = ((i - 1) // 2)
        parent = graph.get_node_by_id(parent_id)
        child = Node(i)
        graph.add_node(child)
        graph.add_edge(Edge(parent, child))

    return graph

def generate_maximally_unbalanced_tree(n):
    graph = Graph()
    root = Node(0)
    graph.add_node(root)
    for i in range(1, n):
        parent = graph.get_node_by_id(i // 2)
        node = Node(i)
        graph.add_node(node)
        edge = Edge(parent, node)
        graph.add_edge(edge)
    return graph

def bottom_up_traversal(self, start_id):
    node = self.get_node_by_id(start_id)
    while node.parent is not None:
        yield node
        node = self.get_node_by_id(node.parent)
    yield node

