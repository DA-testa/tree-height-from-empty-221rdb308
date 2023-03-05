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
         
       return height(root)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    
    height = compute_height(n, parents)
    
    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()

