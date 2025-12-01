


def shortest_path(rooms, doors, start, goal):
    """
    Compute one shortest path between start and goal in an undirected graph.

    rooms: list of room name strings.
    doors: list of (a, b) pairs, each pair is an undirected door between rooms a and b.
    start: start room name.
    goal: goal room name.

    Return:
      - list of room names from start to goal (inclusive) for one shortest path,
      - [start] if start == goal,
      - [] if no path exists.
    """

    # Build adjacency map for an undirected graph.
    from collections import deque

    # Quick sanity: if start or goal missing from rooms, no path.
    room_set = set(rooms)
    if start == goal:
      # Only return [start] when the room exists in the map.
      if start in room_set:
        return [start]
      return []

    if start not in room_set or goal not in room_set:
      return []

    adj = {r: [] for r in rooms}
    for a, b in doors:
      # Only add edges for rooms present in the rooms list.
      if a in adj and b in adj:
        adj[a].append(b)
        adj[b].append(a)

    # BFS with parent tracking.
    q = deque([start])
    visited = {start}
    parent = {start: None}

    found = False
    while q:
      cur = q.popleft()
      if cur == goal:
        found = True
        break
      for nb in adj.get(cur, []):
        if nb not in visited:
          visited.add(nb)
          parent[nb] = cur
          q.append(nb)

    if not found:
      return []

    # Reconstruct path from goal to start
    path = []
    node = goal
    while node is not None:
      path.append(node)
      node = parent.get(node)
    path.reverse()
    return path


if __name__ == "__main__":
    # Optional manual test
    rooms = ["Entrance", "Hall", "Gallery", "Cafe"]
    doors = [("Entrance", "Hall"), ("Hall", "Gallery"), ("Gallery", "Cafe")]
    print(shortest_path(rooms, doors, "Entrance", "Cafe"))
