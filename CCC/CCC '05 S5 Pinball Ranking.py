#Run in pypy2 or TLE ;-;

import sys
n = int(sys.stdin.readline())
alist = []

for x in range(n):
  alist.append(int(sys.stdin.readline()))

swapCount = 0

def mergeSort(alist):
    global swapCount
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        swap = 0
        while i < len(lefthalf) and j < len(righthalf):
            
            if lefthalf[i] > righthalf[j]:
                alist[k]=righthalf[j]
                j=j+1
                swapCount = swapCount + (len(lefthalf) - i)
            else:
                alist[k]=lefthalf[i]
                i=i+1
            k=k+1
            """
            if lefthalf[i] < righthalf[j] or lefthalf[i] == righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
                swapCount = swapCount + (len(lefthalf) - i)
            k=k+1 """
            

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

mergeSort(alist)
print("%.2f" % float((swapCount + n)/float(n)))
