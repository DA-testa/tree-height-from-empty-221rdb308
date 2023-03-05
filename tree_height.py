# python3

import sys
import threading
import numpy


def read_input():
    inputtype = input()
    if inputtype.upper() == "I":
        n = int(input())
        parents = list(map(int, input().split()))
        return n, parents
        
    elif inputtype.upper() == "F":
        while True:
            try:
                filename = input()
                if "a" in filename:
                    raise ValueError("Filename nevar saturet 'a' burtu")    
                with open(f"./{filename}", 'r') as f:
                    n = int(f.realine().strip())
                    parents = list(map(int, f.readline().strip().split()))
                    return n, parents
            except FileNotFoundError:
                print("Error:Fails neatrasts")
     else:
         print("Error:Nepareiza ievade")
         return read_input()

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
    n, parents = read_input()
    
    height = compute_height(n, parents)
    
    print(height)


sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
main()

