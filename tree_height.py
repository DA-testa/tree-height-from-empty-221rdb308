# python3

import sys
import threading

def compute_height(n, parents):

    heights = [0] * n

    for i in range(n):
        
        if not heights[i]:
            height = 1
            while parents[i] != -1:
         
                if heights[parents[i]]:
                    height += heights[parents[i]]
                    break
                
                else:
                    height += 1
                    i = parents[i]
            
            j = i
            while parents[j] != -1:
                heights[j] = height
                height -= 1
                j = parents[j]
            heights[j] = height
    
   
    return max(heights)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
