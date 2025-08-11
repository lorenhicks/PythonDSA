mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
  insert_index = i
  current_value = mylist[i]
  for j in range(i-1, -1, -1):
     if mylist[j] > current_value:
       mylist[j+1] = mylist[j]
       insert_index = j
     else:
       break
  mylist[insert_index] = current_value

print(mylist)