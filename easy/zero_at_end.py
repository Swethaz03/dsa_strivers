
def zeroend(list1):

  j=-1
  n=len(list1)
  for i in range(0,n):
        if list1[i]==0:
            j=i
            break

  for i in range(j+1,n):
    if list1[i]!=0:
        list1[i],list1[j]=list1[j],list1[i]
        j+=1

  print(list1)

list2=[1,2,0,4,0,6,0]
zeroend(list2)
