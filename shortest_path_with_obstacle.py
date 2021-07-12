# constructing graph and running BFS algorithm
from queue import Queue

# complexity:
# -time O(k*N^2) -> K*4*N^2, where K is number of tests, and N size of test matrix linearization to create graph and running than BFS algorithm
# -space O(N^2)


def BFS_matrix_adjacency(graph,n,A):
    times = [float("inf")]*(n*n)
    time = 0
    times[A] = time
    queue = Queue()
    queue.put(A)
    while not queue.empty():
        time += 1
        next_queue = Queue()
        while not queue.empty():
            actual = queue.get()
            for neighbour in graph[actual]:
                neighbour = neighbour[0]*n+neighbour[1]%n
                if times[neighbour] == float("inf"):
                    times[neighbour] = time
                    next_queue.put(neighbour)
        queue = next_queue
    return times


def connections(actual,n):
    # every vertex can have maximum 4 neighbours
    positions = [(-1,0),(0,1),(1,0),(0,-1)]
    neighbours = []
    for x,y in positions:
        new_x = actual[0]+x
        new_y = actual[1]+y
        if new_x >= 0 and new_x < n and new_y >= 0 and new_y < n:
            neighbours.append((new_x,new_y))
    return neighbours


def construct_graph(size,F):
    # linearization of coordinates to construct the graph
    graph = [connections((i//size,i%size),size) if i//size != F[0] or i%size != F[1] else [] for i in range(size*size)]
    return graph


def shortest_path():
    # empty space in console
    print("")
    A = tuple(map(int,input().split(" ")))
    B = tuple(map(int,input().split(" ")))
    F = tuple(map(int,input().split(" ")))
    size = max(max(A),max(B),max(F))
    A = A[0]-1,A[1]-1
    B = B[0]-1,B[1]-1
    F = F[0]-1,F[1]-1
    # constructing graph
    graph = construct_graph(size,F)

    times = BFS_matrix_adjacency(graph,size,A[0]*size+A[1])
    return times[B[0]*size+B[1]%size]


def shortest_path_with_obstacle():
    tests = int(input())
    answers = []
    for _ in range(tests):
        answers.append(shortest_path())

    for answer in answers:
        print(answer)


shortest_path_with_obstacle()

