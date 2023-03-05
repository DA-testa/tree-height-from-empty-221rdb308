# python3

import sys
import threading


def read_input():
    while True:
        inputtype = input("input I for keyboard and F for file:")
        if inputtype.upper() == "I":
            n = int(input())
            parents = list(map(int, input()))
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
                 continue:
             except:
                 print("Invalid file format")
                 continue
                 break
           else:
             print("Invalid input type")
             return n, parents

                                


def compute_height(n, parents):
    # Write this function
    tree = [[] for i in range (n)]
    for i in range(n):
        parent=parents[i]
        if parent == -1:
        c = i
        else:
            tree[parent].append(i)
    # Your code here
    
def height(node):
    if len(tree[node]) == 0:
        return 1
    else:
        return 1 + max([height(child) for child in tree[node]])
    return height(c)

def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
     n, parents = read_input()
     height = compute_height(n, parents)
     print(height)
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
   

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
