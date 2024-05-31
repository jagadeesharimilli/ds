# Adjacency Matrix
# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     row = [0] * n 
#     # [0, 0, 0, 0, 0]
#     matrix.append(row)
 
# print(matrix)  
# for i in range(m):
#     u, v = map(int, input().split())
#     matrix[u][v] = 1 
#     matrix[v][u] = 1  
 
# print(matrix)
 
 
# Adjacency List Construction 
n, m = map(int, input().split())
adj = [] 
for i in range(n):
    adj.append([])
 
print(adj)
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
print(adj)
