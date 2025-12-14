def dfs(graph, node, target_node, visited, npaths):
    visited = visited + (node,)
    for neighbor in graph[node]:
        if neighbor==target_node:
            npaths = npaths + 1
#        if neighbor!='out' and neighbor not in visited:
        if neighbor!='out':
            visited, npaths = dfs(graph, neighbor, target_node, visited, npaths)
    return visited, npaths
            
with open('day11_prob1.txt', 'r') as f:
#with open('day11_sample.txt', 'r') as f:
    rows = f.read().splitlines()

graph = {}

for row in rows:
    node = row.split(':')
    conns = node[1].strip().split(' ')
    graph[node[0]] = conns

print(graph['you'])

visited = ()
npaths = 0
visited, npaths = dfs(graph, 'you', 'out', visited, npaths)
    
print(npaths)

