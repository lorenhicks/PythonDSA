def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

def radixSortWithBubbleSort(arr):
  max_val = max(arr)
  exp = 1

  while max_val // exp > 0:
    radixList = [[],[],[],[],[],[],[],[],[],[]]

    for num in arr:
      radixIndex = (num // exp) % 10
      radixList[radixIndex].append(num)

    for bucket in radixList:
      bubbleSort(bucket)

    i = 0
    for bucket in radixList:
      for num in bucket:
        arr[i] = num
        i += 1

    exp *= 10

mylist = [170, 45, 75, 90, 802, 24, 2, 66]

radixSortWithBubbleSort(mylist)

print(mylist)