'''params arr: arraylist'''
### bubble sort
def bubble_sort(arr):
    length = len(arr)
    for i in range(0,length):
        for j in range(0,length-1):
            if arr[j]>a[j+1]:
                temp = arr[j+1]
                arr[j+1]=arr[j]
                arr[j] = temp
    return arr

### selection sort
def selection_sort(arr):
    length=len(arr)
    for i in range(0,length):
        minindex = i
        for j in range(i+1, length):
            if a[j] < a[minindex]:
                minindex = j
       
    temp = a[i]
    a[i] = a[minindex]
    a[minindex] = temp
    return arr

def quicksort(arr):
    left = 0
    right = len(arr)
    if left >right:
        return "error"
    temp = a[left]  #保存基准数
    i = left
    j = right
    while (i!=j):
        if (arr[i] < temp) and (i<j) :           
            i=i+1
        if (arr[j] > temp) and (i<j):
            j=j-1
        arr[i], arr[j]= arr[j], arr[i]

    arr[left] = arr[i]
    arr[i] = temp

    quicksort(arr,left, i-1)
    quicksort(arr,i+1, right)

    return arr



a =[0,13,4,14,8,10]
print("排序前：", a)
print("冒泡排序：", bubble_sort(a))
print("选择排序：", selection_sort(a))
print("快速排序：", quicksort(a))
    