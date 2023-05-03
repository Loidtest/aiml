def dfs(start, target, jug1, jug2):
    stack = [(start, set())]
    
    while stack:
        (curr_jug1, curr_jug2), visited = stack.pop()
        
        if (curr_jug1, curr_jug2) in visited:
            continue
        visited.add((curr_jug1, curr_jug2))
        
        if curr_jug1 == target or curr_jug2 == target:
            return True
        
        stack.append(((jug1, curr_jug2), visited.copy()))
        stack.append(((curr_jug1, jug2), visited.copy()))
        stack.append(((0, curr_jug2), visited.copy()))
        stack.append(((curr_jug1, 0), visited.copy()))
        stack.append(((min(curr_jug1+curr_jug2, jug1), max(0, curr_jug1+curr_jug2-jug1)), visited.copy()))
        stack.append(((max(0,curr_jug1+curr_jug2-jug2), min(curr_jug1+curr_jug2, jug2)), visited.copy()))
        
    return False

def water_jug(jug1_cap, jug2_cap, target):
    start_point = (0,0)
    target_point = (target, 0)
    
    if dfs(start_point, target, jug1_cap, jug2_cap):
        print(f"Target achieved {target_point}")
    else:
        print("Target not achieved")

water_jug(4,3,2)
        
