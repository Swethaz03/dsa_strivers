
def duplicate(array):
    set1=set()
    for i in range(0,len(array)):
      set1.add(array[i])
    print(set1)

list=[1,2,2,3,5,8,9]
duplicate(list)


def duplicate1(arr):
    l=1
    for r in range(1,len(arr)):
       if(arr[r]!=arr[r-1]):
          arr[l]=arr[r]
          l+=1
    
    for i in range(0,l):
       print(arr[i],end=" ")
    
list1=[0,0,1,1,2,4,5,6]
duplicate1(list1)         
          


         
       