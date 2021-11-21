def bubblesort(arr):
    n = len(arr)
 
    for i in range(n-1):
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
 
 students = {
    31: 'Torben', 
    4: 'Tamara', 
    19: 'Theodor', 
    8: 'Tina', 
    11: 'Toni'
}

only_keys = list(students.keys())
print(only_keys)
bubblesort(only_keys)

for key in only_keys:
    print(students[key])
