# """naive approach"""
# array1=[0,1,1,2,3,4]
# array2=[3,4,5,6,7]
# n1=len(array1)
# n2=len(array2)
# set1=set()
# for i in range(n1):
#     set1.add(array1[i])

# for i in range(n2):
#     set1.add(array2[i])

# print(set1)
# union=[]

# for num in set1:
#     union.append(num)

# union.sort()
# print(union)


"""optimal approach -two pointer approaach"""

def unions(arr1, arr2):
    leng1 = len(arr1)
    leng2 = len(arr2)
    union1 = []
    i = 0
    j = 0

    while i < leng1 and j < leng2:

        if i > 0 and arr1[i - 1] == arr1[i]:
            i += 1
            continue
        if j > 0 and arr2[j - 1] == arr2[j]:
            j += 1
            continue

        if arr1[i] < arr2[j]:
            union1.append(arr1[i])
            i += 1  # ✅ Fix
        elif arr2[j] < arr1[i]:
            union1.append(arr2[j])
            j += 1  # ✅ Fix
        else:
            union1.append(arr1[i])
            i += 1
            j += 1

    while i < leng1:
        if i > 0 and arr1[i - 1] == arr1[i]:
            i += 1
            continue
        union1.append(arr1[i])
        i += 1

    while j < leng2:
        if j > 0 and arr2[j - 1] == arr2[j]:
            j += 1
            continue
        union1.append(arr2[j])
        j += 1

    print(union1)

# Test
ar1 = [0, 2, 3, 3, 4, 5]
ar2 = [3, 5, 6, 7, 8]
unions(ar1, ar2)

