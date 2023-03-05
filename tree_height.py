# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    tree = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)
    def dfs(node):
        max_height = 0
        for child in tree[node]:
            height = 1 + dfs(child)
            max_height = max(max_height, height)
        return max_height
         
    return dfs(root)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    
    height = compute_height(n, parents)
    
    print(height)


sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
main()

