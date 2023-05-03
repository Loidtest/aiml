graph = [
    [0,4,3,0,0,0,0],
    [0,0,0,0,12,5,0],
    [0,0,0,7,10,0,0],
    [0,0,0,0,2,0,0],
    [0,0,0,0,0,0,5],
    [0,0,0,0,0,0,16],
    [0,0,0,0,0,0,0]
]
h_val = {
    1:12, 
    2:11, 
    3:6, 
    4:14, 
    5:11, 
    6:0
}

parent = {
    0:0,
    1:-1,
    2:-1,
    3:-1,
    4:-1,
    5:-1,
    6:-1
}

bestpath = {
    1:999,
    2:999,
    3:999,
    4:999,
    5:999,
    6:999,
}
o_que = list()
c_que = list()

h_n = 0
g_n = 0
f_n = 0
GS = 0

def find(par,cur):
    if(cur == 0):
        return 0
    tmp = graph[par][cur]
    # print(tmp)
    return tmp + find(parent[par],par)

def print_path(node):
    if(node == 0):
        print("Path : ",0,end=" --> ")
        return
    print_path(parent[node])
    print(node,end=" --> ")

def A_star(start):
    o_que.append(start)
    while(len(o_que) != 0):
        ind = o_que[0]
        for i in range(0,7):
            if(graph[ind][i] != 0):
                par = ind
                ##print(i)
                h_n = h_val[i]
                g_n = find(par,i)
                f_n = g_n + h_n
                if(bestpath[i] > f_n):
                    bestpath[i] = f_n
                    parent[i] = par
                if(h_n == 0):
                    print("--> GOAL STATE REACHED <--\n --> NODE : {} <--\n".format(i))
                    GS = i
                    continue
                o_que.append(i)
        c_que.append(o_que.pop(0))
        # print(o_que,parent,bestpath)
        if(len(o_que) != 0):
            temp = 99999
            for j in range(0,len(o_que)):
                if(bestpath[o_que[j]] < temp):
                    temp = bestpath[o_que[j]]
                    index_val = j
            o_que.insert(0,o_que[index_val])
            o_que.pop(index_val+1)
    print_path(GS)
    print("\nCost to reach the Goal state : {}".format(bestpath[GS]))
    print("o_que",o_que,"\nc_que",c_que)

if __name__ == "__main__":
    A_star(0)