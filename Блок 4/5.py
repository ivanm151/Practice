def find_route(graph, start, end, way):
    """Поиск всех путей"""
    way = way + [start]
    if start == end:
        return [way]
    route = []
    for point in graph[start]:
        ways = find_route(graph, point, end, way)
        route.extend(ways)
    return route


graph1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start1 = 'A'
end1 = 'F'
way1 = []
print(*find_route(graph1, start1, end1, way1), sep="; ")
