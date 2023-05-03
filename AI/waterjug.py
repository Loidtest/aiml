x = 0
y = 0
j1 = 4
j2 = 3
target = 2

que = list()
visited = list()
path = dict()

def is_visit(x,y):
    if(len(visited) == 0):
        return True
    for i,j in visited:
        if(x == i and y ==j):
            return False
    return True
def chk_condition(x,y):
    #fill by pump
    if(x < j1):
        if(is_visit(x,j2)):
            que.append((x,j2))
            path[(x,j2)] = (x,y)
    if(y < j2):
        if(is_visit(j1,y)):
            que.append((j1,y))
            path[(j1,y)] = (x,y)
    #empty on ground
    if(x > 0):
        if(is_visit(0,y)):
            que.append((0,y))
            path[(0,y)] = (x,y)
    if(y > 0):
        if(is_visit(x,0)):
            que.append((x,0))
            path[(x,0)] = (x,y)
    #transfer x to y
    if(x > 0 and y<j2):
        if(x+y <= j2):
            if(is_visit(0,x+y)):
                que.append((0,x+y))
                path[(0,x+y)] = (x,y)
        else:
            if(is_visit(abs(j2-(x+y)),j2)):
                que.append((abs(j2-(x+y)),j2))
                path[(abs(j2-(x+y)),j2)] = (x,y)
    if(y > 0 and x<j1):
        if(x+y <= j1):
            if(is_visit(x+y,0)):
                que.append((x+y,0))
                path[(x+y,0)] = (x,y)
        else:
            if(is_visit(j1,abs(j1-(x+y)))):
                que.append((j1,abs (j1- (x+y) ) ) )
                path[(j1,abs(j1-(x+y)))] = (x,y)

def print_path(a,b):
        if(a == 0 and b == 0):
            return
        c,d = path[(a,b)]
        print_path(c,d)
        print(c,d)
        
if __name__ == "__main__":
#     print("start")
    que.append((0,0))
    while(len(que) != 0):
        x,y = que[0]
        visited.append(que[0])
        chk_condition(x,y)
        if(target == x or target == y):
            print("done")
            print_path(x,y)
            break
        que.pop(0)
#         print(que)