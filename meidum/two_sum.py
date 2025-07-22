"""brute approach"""

# def two_sum(arr,k):
#     sum=0
#     for i in range(0,len(arr)-1):
#         for j in range(i+1,len(arr)):
#             sum=arr[i]+arr[j]
#             if sum==k:
#                 print ([i,j])

# a=[1,6,2,10,3]
# two_sum(a,9)

"""another approach"""
# def two_sum(arr,k):
#     for i in range(0,len(arr)):
#         a=arr[i]
#         b=k-a
#         if b in arr[i+1:]:
#             j=arr.index(b,i+1)
#             print([i,j])
# a=[1,6,2,10,1,3]
# two_sum(a,9)

"""...... using hashing ......."""

def two_sum(arr,k):
    map={}
    for i in range(0,len(arr)):
        b=k-arr[i]
        if arr[i] not in map:
            map[arr[i]]=i
        
        if b in map:
            

a=[1,6,2,10,1,3]
two_sum(a,9)