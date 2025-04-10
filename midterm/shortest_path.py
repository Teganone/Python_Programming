from collections import deque


def make_graph(route_dic):
    graph = {}
    for key, value in route_dic.items():
        graph[key] = []
        prev_key = str(int(key) - 1)
        if prev_key in route_dic and route_dic[prev_key]['line'] == value['line']:
            graph[key] += [prev_key]
        next_key = str(int(key) + 1)
        if next_key in route_dic and route_dic[next_key]['line'] == value['line']:
            graph[key] += [next_key]
        graph[key] += value['transfer_list']
    return graph


def bfs(graph, start, end):
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        station = path[-1]
        # print(f"当前站点: {station}")
        # print(f"当前path: {path}")
        if station == end:
            return path
        for neighbor in graph[station]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                # print("new_path",new_path)
                queue.append(new_path)
    return None

    