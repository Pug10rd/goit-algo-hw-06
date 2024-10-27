import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = [
    "Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska", 
    "Shuliavska", "Politekhnichnyi Instytut", "Vokzalna", "Universytet", 
    "Teatralna", "Khreshchatyk", "Arsenalna", "Dnipro", "Hidropark", 
    "Livoberezhna", "Darnytsia", "Chernihivska", "Lisova", "Boryspilska", 
    "Klovska", "Poshtova Ploshcha", "Kontraktova Ploshcha", "Taras Shevchenko", 
    "Zoloti Vorota", "Palats Sportu", "Olimpiiska", "Lva Tolstoho", 
    "Ploshcha Lva Tolstoho", "Vystavkovyi Tsentr", "Bereznyaki", 
    "Cherkasy", "Bilychi", "Podil", "Obolon", "Minska", 
    "Heroiv Dnipra", "Sviatoshyn", "Zhytomyrska"
]

G.add_nodes_from(stations)

edges = [
    ("Akademmistechko", "Zhytomyrska"), ("Zhytomyrska", "Sviatoshyn"), 
    ("Sviatoshyn", "Nyvky"), ("Nyvky", "Beresteiska"), ("Beresteiska", "Shuliavska"), 
    ("Shuliavska", "Politekhnichnyi Instytut"), ("Politekhnichnyi Instytut", "Vokzalna"), 
    ("Vokzalna", "Universytet"), ("Universytet", "Teatralna"), 
    ("Teatralna", "Khreshchatyk"), ("Khreshchatyk", "Arsenalna"), 
    ("Arsenalna", "Dnipro"), ("Dnipro", "Hidropark"), 
    ("Hidropark", "Livoberezhna"), ("Livoberezhna", "Darnytsia"), 
    ("Darnytsia", "Chernihivska"), ("Chernihivska", "Lisova"),
    ("Lisova", "Boryspilska"), ("Boryspilska", "Klovska"),
    ("Klovska", "Poshtova Ploshcha"), ("Poshtova Ploshcha", "Kontraktova Ploshcha"),
    ("Kontraktova Ploshcha", "Taras Shevchenko"), ("Taras Shevchenko", "Zoloti Vorota"),
    ("Zoloti Vorota", "Palats Sportu"), ("Palats Sportu", "Olimpiiska"),
    ("Olimpiiska", "Lva Tolstoho"), ("Lva Tolstoho", "Ploshcha Lva Tolstoho"),
    ("Ploshcha Lva Tolstoho", "Vystavkovyi Tsentr"), ("Vystavkovyi Tsentr", "Bereznyaki"),
    ("Bereznyaki", "Cherkasy"), ("Cherkasy", "Bilychi"),
    ("Bilychi", "Podil"), ("Podil", "Obolon"), ("Obolon", "Minska"),
    ("Minska", "Heroiv Dnipra"), ("Heroiv Dnipra", "Sviatoshyn")
]

# Додаємо ребра до графа
G.add_edges_from(edges)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph.neighbors(vertex)) - visited)
    return visited

# Тестуємо DFS та BFS
start_station = "Akademmistechko"
dfs_path = dfs(G, start_station)
bfs_path = bfs(G, start_station)

print("Шлях DFS: \n", dfs_path)
print("Шлях BFS: \n", bfs_path)


# Візуалізуємо граф
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Фіксована позиція для візуалізації
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')
plt.title("Граф Київського метрополітену")
plt.show()

# Аналіз графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
degree_sequence = [G.degree(node) for node in G.nodes()]
print("Ступінь вершин:", degree_sequence)