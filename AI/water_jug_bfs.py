from collections import deque

def bfs(start, target, jug1, jug2):
    queue = deque([(start, set())])
    
    while queue:
        (curr_jug1, curr_jug2), visited = queue.popleft()
        
        if (curr_jug1, curr_jug2) in visited:
            continue
        visited.add((curr_jug1, curr_jug2))
        
        if curr_jug1 == target or curr_jug2 == target:
            return True
        
        queue.append(((jug1, curr_jug2), visited.copy()))
        queue.append(((curr_jug1, jug2), visited.copy()))
        queue.append(((0, curr_jug2), visited.copy()))
        queue.append(((curr_jug1, 0), visited.copy()))
        queue.append(((min(curr_jug1+curr_jug2, jug1), max(0, curr_jug1+curr_jug2-jug1)), visited.copy()))
        queue.append(((max(0,curr_jug1+curr_jug2-jug2), min(curr_jug1+curr_jug2, jug2)), visited.copy()))
        
    return False

def water_jug(jug1_cap, jug2_cap, target):
    start_point = (0, 0)
    
    if bfs(start_point, target, jug1_cap, jug2_cap):
        print(f"Target achieved ({target}, 0)")
    else:
        print("Target not achieved")

water_jug(4, 3, 2)