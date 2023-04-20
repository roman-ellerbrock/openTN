import openTN

def test_graph():
    # Create a tree with 3 nodes.
    graph = openTN.Graph()
    root_node = openTN.Node(None)
    graph.add_node(root_node)
    node_1 = openTN.Node(None)
    graph.add_node(node_1)
    node_2 = openTN.Node(None)
    graph.add_node(node_2)
    graph.add_edge(openTN.Edge(root_node, node_1))
    graph.add_edge(openTN.Edge(root_node, node_2))
    
    # Check that all nodes are present.
    assert graph.get_node_by_id(0) == root_node
    assert graph.get_node_by_id(1) == node_1
    assert graph.get_node_by_id(2) == node_2
    
    # Check that all edges are present.
    assert graph.get_edge_by_id(0).node_1 == root_node
    assert graph.get_edge_by_id(0).node_2 == node_1
    assert graph.get_edge_by_id(1).node_1 == root_node
    assert graph.get_edge_by_id(1).node_2 == node_2


def test_generate_tree():
    # Create a tree with 3 nodes.
    graph = openTN.generate_balanced_tree(3)

    # Check that all nodes are present.
    assert graph.get_node_by_id(0) is not None
    assert graph.get_node_by_id(1) is not None
    assert graph.get_node_by_id(2) is not None

    root = graph.get_node_by_id(0)
    node_0 = graph.get_node_by_id(1)
    node_1 = graph.get_node_by_id(2)

    # Check that all edges are present.
    assert graph.get_edge_by_id(0).node_1 == root
    assert graph.get_edge_by_id(0).node_2 == node_0
    assert graph.get_edge_by_id(1).node_1 == root
    assert graph.get_edge_by_id(1).node_2 == node_1


def test_generate_maximally_unbalanced_tree():
    # Generate a maximally unbalanced tree with 4 nodes.
    graph = openTN.generate_maximally_unbalanced_tree(4)

    # Check that all nodes are present.
    assert graph.get_node_by_id(0) is not None
    assert graph.get_node_by_id(1) is not None
    assert graph.get_node_by_id(2) is not None

    # Check that all edges are present.
    assert graph.get_edge_by_id(0) is not None
    assert graph.get_edge_by_id(1) is not None
    assert graph.get_edge_by_id(2) is not None

    # Check the tree structure.
    assert graph.get_neighbors(0) == [graph.get_node_by_id(1)]
    assert graph.get_neighbors(1) == [graph.get_node_by_id(2)]
    assert graph.get_neighbors(2) == [graph.get_node_by_id(3)]
    assert graph.get_neighbors(3) == []