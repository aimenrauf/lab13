graph ={
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B'],
'E': ['B', 'F'],
'F': ['C', 'E']
}
# Displaying the graph
for node in graph:
    print(f"{node} -> {graph[node]}")