from collections import deque


def search(name):
    search_queue = deque()  # make emty queue
    search_queue += graph[name]
    searched = []  # list of searched elements to avoid double check
    while search_queue:
        person = search_queue.popleft()
        if person in searched:    # if not person in searched : check is seller and append to searched
            continue
        if person_is_seller(person):
            print(person.capitalize() + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return False


def person_is_seller(name):
    """Check is name a mango seller"""
    return 'm' in name


graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search("you")
