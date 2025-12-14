def dfs(node, target_node):
    npaths = 0
    if node in memo:
        return memo[node]
    for neighbor in graph[node]:
        if neighbor==target_node:
            return 1
        elif neighbor=='out':
            return 0
        else:
            npaths += dfs(neighbor, target_node)

    memo[node] = npaths
    return npaths
            
with open('day11_prob1.txt', 'r') as f:
#with open('day11_sample2.txt', 'r') as f:
    rows = f.read().splitlines()

graph = {}

for row in rows:
    node = row.split(':')
    conns = node[1].strip().split(' ')
    graph[node[0]] = conns

n=[]
memo = {}
n.append(dfs('svr', 'fft'))

print('SVR to FFT')
print(n[-1])

memo = {}
n.append(dfs('fft', 'dac'))

print('FFT to DAC')
print(n[-1])

memo = {}
n.append(dfs('dac', 'out'))

print('DAC to OUT')
print(n[-1])



memo = {}
n.append(dfs('svr', 'dac'))

print('SVR to DAC')
print(n[-1])

memo = {}
n.append(dfs('dac', 'fft'))

print('DAC to FFT')
print(n[-1])

memo = {}
n.append(dfs('fft', 'out'))

print('FFT to OUT')
print(n[-1])

print()
print()
print('SVR->DAC->FFT->OUT')
print(n[0]*n[1]*n[2])
print()
print('SVR->FFT->DAC->OUT')
print(n[3]*n[4]*n[5])
