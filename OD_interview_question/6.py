start, n = input().split()

all_node = {}
nodes = []
for i in range(int(n)):
    start_path , node, end_path = [x for x in input().split()]
    all_node[start_path] = node
    all_node[node] = end_path
    if start_path == start:
        nodes.append(node)

next_node = nodes[0]
for i in range(int(n)):
    i_path = all_node.get(next_node)
    if i_path == '-1':
        break
    else:
        second_node = all_node.get(i_path)
        next_node = second_node
        nodes.append(next_node)

print(nodes)
index = len(nodes) // 2
print(nodes[index])

