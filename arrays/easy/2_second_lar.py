
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

     


