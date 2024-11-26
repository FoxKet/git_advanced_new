def bubble_sort(array):
    iterations = len(array)-1
    for i in range(iterations):
        for j in range(iterations-i):
            if array[j]> array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]



a =  [1, 4, -3, 0, 10]
print(a)
bubble_sort(a)
print(a)
