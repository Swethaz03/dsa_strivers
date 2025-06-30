
def sorted(array):
    length=len(array)
    
    if (length==0 or length==1):
        return True


    for i in range(1,length):
        if array[i-1]>array[i]:
          return False
    return True

arr=[3,4,5,6,7,1]
if (sorted(arr)):
    print("yes")
else:
    print("no")

    


