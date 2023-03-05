# python3

import sys
import threading


                            

def compute_height(n, parents):
    tree = [[] for i in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)


    def height(node):
        if len(tree[node]) == 0:
            return 1
        else:
            return 1 + max([height(child) for child in tree[node]])

    return height(root)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    height = compute_height(n, parents)
    print(height)



sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
