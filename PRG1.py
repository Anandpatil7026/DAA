import time
from numpy.random import randint 
import matplotlib.pyplot as plt
def mergesort(array):
    if len(array)>1:
        r=len(array)//2
        L=array[:r]
        M=array[r:]
        mergesort(L)
        mergesort(M)
        i=j=k=0
        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=M[j]
                i+=1
            k+=1
        while i<len(L):
            array[k]=L[i]
            i+=1
            k+=1
        while j<len(M):
            array[k]=M[j]
            j+=1
            k+=1

def printlist(array):
    for i in range (len(array)):
        print(array[i],end=" ")
    print( )
if __name__=="__main__":
    array=[6,5,12,10,9,1]
    mergesort(array)
print("sorted array is :")
printlist(array)

def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i+1],array[high])=(array[high],array[i+1])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1
def quickSort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quickSort(array,low,pi-1)
        quickSort(array,pi+1,high)
data=[8,7,2,1,0,9,6]
print("Unsorted Array")
print(data)
size=len(data)
quickSort(data,0,size-1)
print('sorted array in ascending order :')
print(data)

def selectionSort(array,size):
    for step in range(size):
        min_idx=step
        for i in range (step+1,size):
            if array[i]<array[min_idx]:
                min_idx=i
        (array[step],array[min_idx])=(array[min_idx],array[step])
data=[-2,45,0,11,-9]
size=len(data)
selectionSort(data,size)
print('sorted array in ascending order: ')
print(data)

def read_Input():
    a=[]
    n=int(input("enter the number of TV channels:"))
    print("enter the number of viewers")
    for i in range (0,n):
        l=int(input())
        a.append(l)
    return a
elements=list()
times=list()
global labeldata
print('1.merge sort 2.quicksort 3. selection sort')
ch=int(input("enter the choice"))
if(ch==1):
    array=read_Input()
    mergesort(array)
    labeldata="mergesort"
    print('sorted array is :')
    print(array)
elif(ch==2):
    array=read_Input()
    size=len(array)
    labeldata="quicksort"
    quickSort(array,0,size-1)
    print('sorted array is :')
    print(array)
if(ch==3):
    array=read_Input()
    size=len(array)
    labeldata="selectionsort"
    selectionSort(array,size)
    print('sorted array is :')
    print(array)
print("******************Running time analysis***************")
for i in range(1,10):
    array=randint(0,1000*i,1000*i)
    print(i)
    start=time.time()
    if ch==1:
        mergesort(array)
    elif ch==2:
        size=len(array)
        quickSort(array,0,size-1)
    else:
        size=len(array)
        selectionSort(array,size)
    end=time.time()
    print("sorted list is ",array)
    print(len(array),"element sorted by ",labeldata)
    elements.append(len(array))
    times.append(end-start)
plt.xlabel('list length')
plt.xlabel('time complexity')
labeldata="sort"
plt.plot(elements,times,label=labeldata)
plt.grid()
plt.legend()
plt.show()
