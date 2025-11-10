arr = [4, 2, 1, 5, 8, 9]

n = len(arr)
print("Original Arrayis: ", arr)
for i in range(n):

    for j in range(0, n - i - 1):

        if arr[j] > arr[j+1]:
            
            arr[j], arr[j+1] = arr[j+1], arr[j]

            print("sorted array is: ", arr) 