import networkx as nx

G = nx.Graph()

# Додаємо ваги до ребер
weights = {
    ("Akademmistechko", "Zhytomyrska"): 3, ("Zhytomyrska", "Sviatoshyn"): 2,
    ("Sviatoshyn", "Nyvky"): 1, ("Nyvky", "Beresteiska"): 2,
    ("Beresteiska", "Shuliavska"): 2, ("Shuliavska", "Politekhnichnyi Instytut"): 1,
    ("Politekhnichnyi Instytut", "Vokzalna"): 2, ("Vokzalna", "Universytet"): 1,
    ("Universytet", "Teatralna"): 2, ("Teatralna", "Khreshchatyk"): 1,
    ("Khreshchatyk", "Arsenalna"): 2, ("Arsenalna", "Dnipro"): 2,
    ("Dnipro", "Hidropark"): 1, ("Hidropark", "Livoberezhna"): 1,
    ("Livoberezhna", "Darnytsia"): 2, ("Darnytsia", "Chernihivska"): 3,
    ("Chernihivska", "Lisova"): 2
}

# Додаємо ваги до ребер
for (u, v), weight in weights.items():
    G.add_edge(u, v, weight=weight)

# Алгоритм Дейкстри
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = priority_queue.pop(0)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))
    
    return distances

# Знаходимо найкоротші шляхи від початкової станції
start_station_dijkstra = "Akademmistechko"
shortest_paths = dijkstra(G, start_station_dijkstra)

print("Найкоротші шляхи від", start_station_dijkstra)
for station, distance in shortest_paths.items():
    print(f"До {station}: {distance}")
