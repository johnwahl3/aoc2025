def dfs(graph, node, target_node, paths):
    for neighbor in graph[node]:
        paths[-1].append(neighbor)
        if neighbor==target_node:
            #print(paths[-1])
            paths.append([node for node in paths[-1]])
            paths[-1].pop()
        if neighbor!='out':
            paths = dfs(graph, neighbor, target_node, paths)

    if paths[-1]:
        paths[-1].pop()
    return paths
            
with open('day11_prob1.txt', 'r') as f:
#with open('day11_sample2.txt', 'r') as f:
    rows = f.read().splitlines()

graph = {}

for row in rows:
    node = row.split(':')
    conns = node[1].strip().split(' ')
    graph[node[0]] = conns

paths = [[]]
paths = dfs(graph, 'svr', 'out', paths)

nboth = 0
for path in paths[:-1]:
    if 'fft' in path and 'dac' in path:
        nboth = nboth + 1

#for path in paths[:-1]:
#    print(path)

print(len(paths)-1)
print(nboth)

