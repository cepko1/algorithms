"""There are list of states and list of covered stations.
Need to make Greedy algorithm for select pool of stations for cover all states"""
states_needet = set(["mt", 'wa', "or", "id", "nv", "ut", "ca", "az"])
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
final_stations = set()

while states_needet:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needet & states_for_station    # intersection of sets
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needet -= states_covered

print(final_stations)
