# python3

import sys
import threading


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
    input_type = input("Enter input type (I for keyboard, F for file): ")
    if input_type.upper() == "I":
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parent nodes: ").split()))
    elif input_type.upper() == "F":
        try:
            filename = input("Enter the filename: ")
            folder = './test/'
            with open(folder + filename, 'r') as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
        except FileNotFoundError:
            print("File not found!")
            return
    else:
        print("Invalid input_type!")
        return

    height = compute_height(n, parents)
    print(height)

    print(height)


sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()
