
def largest(array):
    largest=array[0]
    length=len(array)
    for i in range(1,length-1):
        if array[i]>largest:
            largest=array[i]
    print(largest)

list=[3,9,8,3,4]
largest(list)
