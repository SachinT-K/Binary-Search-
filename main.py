def binarySearch(arr,target):

  left = 0
  right = len(arr)-1

  while(left <= right):
    mid = (left+right)//2

    if(arr[mid]==target):
      return mid

    elif(arr[mid]<target):
      left = mid+1

    elif(arr[mid]>target):
      right = mid-1
  return -1

arr = [2,4,6,8,10,12]
target = 12

result = binarySearch(arr,target)

if(result != -1):
  print("Element is present at index %d" % result)
else:
  print("Element is not present in an array")