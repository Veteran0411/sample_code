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


#in the indexes we are storing where it has to traverse next / what is cost till destination 
# Initialize the cost to reach the destination node (8) to 0

def multistage(n):
    
    # filling up the table to get answer, from destination based on index and index is same as element, from second last node
    for i in range(n - 1, 0, -1):
        min_cost = float("inf")
        
        #traversing the keys in graph
        for k in graph[i]:
            # i is start node k is dest/intermediate node (eg: when i=7 and k traverses  graph keys graph[7][8]=5)
            if graph[i][k] + cost[k] < min_cost:
                min_cost = graph[i][k] + cost[k]
                vertex[i] = k
        cost[i] = min_cost

def print_optimal_path(start,destination):
    path=[start]
    print(f"cost to reach final node from {start} to {destination} is: {cost[start]} ")
    while start<destination:
        path.append(vertex[start])
        start=vertex[start]
    return path

destination=max(graph.keys())

#cost is used to store the cost till the destination node
cost = [float("inf")] * (destination+1) # destination+1 because node is from 1-8 , so 8th node is 9th element in list.
cost[destination] = 0

#vertex is used to get the next node it should traverse, (values are stored in respected index)
vertex = [0] * (destination+1)
multistage(destination)

source_node=int(input("enter the source node: "))
optimal_path=(" -> ".join(map(str,print_optimal_path(source_node,destination))))
print(optimal_path)
print(cost)
# graph={
#     1:{2:9,3:7,4:3,5:11},
#     2:{6:4,7:2,8:1},
#     3:{6:2,7:7},
#     4:{8:11},
#     5:{8:8,7:11},
#     6:{9:6,10:5},
#     7:{10:3,9:6},
#     8:{11:6,10:5},
#     9:{12:4},
#     10:{12:2},
#     11:{12:5},
#     12:{},
# }