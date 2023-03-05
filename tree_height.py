# python3

import sys
import threading


def read_input():
    while True:
        inputtype = input("input I for keyboard and F for file:")
        if inputtype.upper() == "I":
            n = int(input())
            parents = list(map(int, input().split()))
            break  
        elif inputtype.upper() == "F":
            while True:
                filename = input("input filename without the letter a:")
                if 'a' in filename.lower():
                    print("try again, filename contains the letter a:")
                else:
                    try:
                        with open(f"inputs/{filename}") as f:
                            n = int(f.readline().strip())
                            parents = list(map(int, f.readline().strip().split()))
                            break
                    except FileNotFoundError:
                        print("File not found")
                        continue
                    except:
                        print("Invalid file format")
                        continue
                    break
        else:
            print("Invalid input type")
    return n, parents
                            

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
    n, parents = read_input()
    height = compute_height(n, parents)
    print(height)



sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
