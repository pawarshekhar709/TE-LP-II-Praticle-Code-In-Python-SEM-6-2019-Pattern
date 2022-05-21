graph = {
    "A": ["B","C"],
    "B": ["A","D","E"],
    "C": ["A","F"],
    "D": ["B"],
    "E": ["B","F"],
    "F": ["C","E"]
}
 
def dfs(node, graph):
  stack = []
  visited = set()
  stack.append(node)
  visited.add(node)
  print(node)
 
  while (len(stack)):
    current_node = stack.pop()
    if current_node not in visited: 
      print(current_node)
      visited.add(current_node)
    for i in graph[current_node][::-1]:
      if i not in visited:
        stack.append(i)
 
dfs("A", graph)