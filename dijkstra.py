def find_lowest_cost_node(costs):
    """Finding lowest cost for each nodes"""
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:    # cheapest and not processed node
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


graph = {}     # create graph of nodes
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}
# print(graph)

costs = {}  # cost (weight) of edges between nodes
costs["a"] = 6
costs["b"] = 2
costs["fin"] = float("inf")
# print(costs)

parents = {}   # parents of nodes
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
# print(parents)

processed = []   # list of checked nodes
node = find_lowest_cost_node(costs)  # the frirst lowest node
while node is not None:    # check for all nodes
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():   # check all neighbors of node
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:    # check if cost lower than previous
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)    # set node as processed
    node = find_lowest_cost_node(costs)  # find next node

for key, value in parents.items():     # show lowest path
    print(f"Node '{value}' is parent for node '{key}'")
print(f"The minimum cost is {cost}")