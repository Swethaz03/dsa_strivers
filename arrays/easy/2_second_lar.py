# Approach 1 sorting then printing last two position
def larg2(a):
    a.sort()
    print(a[-2])

list1=[34,78,99,65,88]
larg2(list1)

#Approach 2

def second_largest(array):
    length=len(array)

    largest=array[0]
    secondlarg=-1

    for i in range(1,length):
        if(array[i]>largest):
            largest=array[i]
        
    for i in range(1,length):
        if(array[i]!=largest and array[i]>secondlarg):
            secondlarg=array[i]

    print(largest)
    print(secondlarg)

array1=[3,1,7,8,6,9]
second_largest(array1)

     
def seclar(ar):
    max=ar[0]
    for i in range(1,len(ar)):
        if ar[i]>max:
            max=ar[i]
    secmax=ar[0]
    for i in range(0,len(ar)):
        
        if ar[i]>secmax and ar[i]<max:  # logic 3
            secmax=ar[i]
    print(secmax)
array1=[32,1,7,98,6,99,45]
seclar(array1)