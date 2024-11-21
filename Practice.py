graph = {
    1: {2: 2, 3: 1, 4: 3},
    2: {5: 2, 6: 3},
    3: {5: 6, 6: 7},
    4: {5: 6, 6: 8, 7: 9},
    5: {8: 6},
    6: {8: 4},
    7: {8: 5},
    8: {}
}

def multiStage(n):
    
    for i in range(n-1,0,-1):
        min_cost=float("inf")
        for k in graph[i]:
            if graph[i][k]+cost[k]<min_cost:
                min_cost=graph[i][k]+cost[k]
                vertex[i]=k
        cost[i]=min_cost
        
def print_optimal(start,destination):
    path=[start]
    print(f"the optimal cost from {start} to {destination} is: {cost[start]}")
    while start<destination:
        path.append(vertex[start])
        start=vertex[start]
    return path

destination=max(graph)
cost=[float("inf")]*(destination+1)
cost[destination]=0
vertex=[0]*(destination*+1)
start=int(input("enter the starting node: "))
multiStage(destination)
optimal_path=" ==> ".join(map(str,print_optimal(start,destination)))
print(optimal_path)
