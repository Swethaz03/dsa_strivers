
def linearsearch(array1,num):
    n=len(array1)
    flag=0
    for i in range(0,n):
        if(array1[i]==num):
            flag=1
            break

    if flag==1:
        print("the num is found at index",i)
    else:
       print("not found")

array2=[1,2,3,4,6]
linearsearch(array2,5)
            

