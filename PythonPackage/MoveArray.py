array = [0,1,2,3,4]
array_len = len(array)
value1 = array[0]

for i in range(1, array_len):
    array[i-1] = array[i]

array[4] = value1
for i in array:
 print(i)


