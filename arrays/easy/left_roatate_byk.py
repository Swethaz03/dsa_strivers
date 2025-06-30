
def rotatek(list,k):
  
  temp=[]
  length=len(list)
  k=k%length
  for i in range(0,k):
        temp.append(list[i])

  for i in range(k,length):  # 2 to 5 iterate
    list[i-k]=list[i]

  for i in range(length-k,length):
    list[i]=temp[i-(length-k)] 
  print(list)  
     
""" 4th=0th, 5th =1st 6th =2nd="""
"""  4-4=0    5-4=1    6-4=2"""
"""  i-len-k   i-len-k  i-len-k """
 


list2=[1,2,3,4,5,6]
rotatek(list2,2)    
    



#       k     n-1   n elements
""" 0 1 2 3 4 5  position"""
  # 1 2 3 4 5 6  elements k=2
  # 3 4 5 6 1 2


