import networkx as nx
import matplotlib.pyplot as plt #buat visualize graph

#NOMOR 1
def create_graph(edges: list[tuple[int, int]]):
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

#NOMOR 2
def get_degree(G: nx.Graph, node: int) -> int:
    return G.degree[node]

#NOMOR 3
import networkx as nx

def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    visited = set() 
    stack = [start] 
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node) 
            result.append(node)  
            stack.extend(reversed(list(G.neighbors(node))))  

    return result

#NOMOR 4
def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    visited = set()
    queue = [start]
    result = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(G.neighbors(node))

    return result

#NOMOR 5
def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    if source == target:
        return [source]
    
    queue = [(source, [source])]
    visited = set()
    
    while queue:
        node, path = queue.pop(0)
        
        if node == target:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in G.neighbors(node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return []

#NOMOR 6
def visualize_graph(G: nx.Graph) -> None:
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', #ini opsional sihh mau gimana bentukannya 
            node_size=1000, font_size=12, font_weight='bold')
    plt.show()
