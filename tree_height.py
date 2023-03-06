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
    else:
        filename = input("Enter the filename: ")
        if 'a' in filename or 'A' in filename:
            print("Filename must not contain a letter!")
            return
        folder = './test/'
        try:
            with open(folder + filename, 'r') as test:
                n = int(test.readline())
                parents = list(map(int, test.readline().strip().split()))
        except FileNotFoundError:
            print("File not found!")
            return

    
    try:
        height = compute_height(n, parents)
        print(height)
    except ValueError as e:
        print("Error:", str(e))
        return
    




sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()
