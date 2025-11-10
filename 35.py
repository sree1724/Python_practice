arr = [4, 2, 1, 5]
n = len(arr)
for i in range(n):

    for j in range(i+1, n):
        main_index = i

        if arr[j] < arr[main_index]:

            arr[j], arr[main_index] = arr[main_index], arr[j]

        arr[main_index], arr[i] = arr[i], arr[main_index]
print("sorted order", arr)



