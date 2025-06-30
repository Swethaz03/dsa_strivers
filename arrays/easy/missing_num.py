
def missing(arr,n):
    new=[]

    for i in range(1,n+1):
     new.append(i)
    print(new)
    
    n1=len(arr)
    m1=len(new)
    i,j=0,0
    

    while i<n1 and j<m1:
          
          if arr[i]!=new[j]:
             print(new[j])
             j+=1
          else:
              i+=1
              j+=1
             

        

b=[1,2,4,5]
missing(b,5)
          
       
