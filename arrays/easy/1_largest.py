
# sorting then printing the last element
def lar(arr):
    arr.sort()
    print(arr[-1])

list=[9,4,7,89,43,67]
lar(list)

# second approach
def largest(array):
    largest=array[0]
    length=len(array)
    for i in range(1,length):
        if array[i]>largest:
            largest=array[i]
    print(largest)

list=[11,9,8,3,10]
largest(list)



