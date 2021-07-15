# problem: https://codeforces.com/problemset/problem/1130/C

from queue import PriorityQueue

# complexity:
# -time O(ElogK) - > Elog(K^2) where K is a number of vertices from one of the connected components
# -space O(V^2*E)


def neighbours(n, actual):
    position = []
    positions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for x, y in positions:
        new_x = actual//n + x
        new_y = actual % n + y
        # condition: is in the array
        if new_x >= 0 and new_x < n and new_y >= 0 and new_y < n:
            position.append((new_x, new_y))

    return position


def distance(a, b, n):
    ax, ay = a // n, a % n
    bx, by = b // n, b % n
    return int((ax-bx)**2 + (ay-by)**2)


# - to memorize, if is needed tunel between two fields- firstly I'll run DFS alg. to find all connected components

def DFS_group(array, n, group_connected_components, group_number, actual):
    group_connected_components[actual] = group_number
    for new_x, new_y in neighbours(n, actual):
        # condition: is in the array and coord is not a water and also wasn't visited before
        if new_x >= 0 and new_x < n and new_y >= 0 and new_y < n and int(array[new_x][new_y]) == 0 and group_connected_components[new_x*n+new_y % n] is None:
            DFS_group(array, n, group_connected_components,
                      group_number, new_x*n+new_y % n)


# if elements are in same connected commponents => cost of edge is 0, otherwise cost of tunel from exercise formula
def new_tunels(groups, group_a_b, tunels, n, actual, index):
    for coord in range(index, len(group_a_b)):
        # same connected components <=> endge weight 0
        coord = group_a_b[coord]
        if groups[coord] == groups[actual]:
            tunels[actual].append((coord, 0))
            tunels[coord].append((actual, 0))
        else:
            d = distance(actual, coord, n)
            tunels[actual].append((coord, d))
            tunels[coord].append((actual, d))


# Edge relaxing in Dijkstra algorithm
def relax(distances, u, v, w):
    if distances[v] > distances[u]+w:
        distances[v] = distances[u]+w
        return True
    else:
        return False


# Dijkstra algorithm to find best connection
def Dijkstra_distance(graph, n, b, e):
    distances = [float("inf")]*n
    distances[b] = 0
    p_queue = PriorityQueue()
    for v, w in graph[b]:
        # tuples in priority queue: (edge weight, first end of edge, second end of edge)
        p_queue.put((w, b, v))
    while not p_queue.empty():
        w, u, v = p_queue.get()
        if relax(distances, u, v, w):
            # adding edges connected to ending vertex of relaxed edge
            for i, w in graph[v]:
                if i != u:
                    p_queue.put((w, v, i))
    return distances[e]


def connect():
    n = int(input())
    begining = [int(el) for el in input().split()]
    b = (begining[0]-1)*n+begining[1]-1
    end = [int(el) for el in input().split()]
    e = (end[0]-1)*n+ end[1]-1
    array = [input() for _ in range(n)]

    # numbering groups of connected components
    groups = [None] * (n**2)
    group_number = -1
    for i in range(n**2):
        if groups[i] == None and int(array[i//n][i % n]) != 1:
            group_number += 1
            DFS_group(array, n, groups, group_number, i)

    # now program memorized connected components -> between vertices of the same group edge weight == 0
    # if vertices are in the same connected component group, distance between is equal 0
    if groups[e] == groups[b]:
        return 0

    # need to filter only elements which became into one of two groups vertices:
    # -connected components with begining vertex
    # -connected components with ending vertex
    group_a_b = []
    for i in range(n**2):
        if groups[i] == groups[b] or groups[i] == groups[e]:
            group_a_b.append(i)

    # creating connections only between every vertices from connecting components of starting point and CC to every vertex in end of connecting components
    graph = [list() for _ in range(n**2)]
    for index, actual in enumerate(group_a_b):
        new_tunels(groups, group_a_b, graph, n, actual, index)
    return Dijkstra_distance(graph, n**2, b, e)


print(connect())

