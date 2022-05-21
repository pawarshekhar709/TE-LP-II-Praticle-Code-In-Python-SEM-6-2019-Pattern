graph = {
    "A": ["B","C"],
    "B": ["A","D","E"],
    "C": ["A","F"],
    "D": ["B"],
    "E": ["B","F"],
    "F": ["C","E"]
}
 
def bfs(node, graph):
  queue = []
  queue.append(node)
  visited = set()
  while queue:
    node_value = queue.pop(0)
    if node_value not in visited: 
      print(node_value)
    visited.add(node_value)
    for i in graph[node_value]:
      if i not in visited:
        queue.append(i)
bfs("A", graph)