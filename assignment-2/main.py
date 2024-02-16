import random 
import time 
import matplotlib.pyplot as plt
def generator(output_file):
    with open(output_file, 'w') as file:
        for i in range(10000):
            file.write(str(random.randint(1, 10000)) + '\n')

def take_numbers(file):
    with open(file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def bubblesort(arr):
    n =len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def counting_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]


def time_finder(arr, sort_type):
    import time
    start = time.time()
    sort_type(arr)
    end = time.time()
    return end - start

def savefile(arr, file):
    with open(file, 'w') as file:
        for i in arr:
            file.write(str(i) + '\n')

if __name__ == "__main__":
    file1="file1.txt"
    file2="file2.txt"
    generator(file1)
    generator(file2)
    print(f"Random numbers generated successfully and saved to {file1} and {file2}")
    number1=take_numbers(file1)
    number2=take_numbers(file2)
    print(f"Time taken by bubblesort for file1.txt is {time_finder(number1, bubblesort)} seconds ")
    print(f"Time taken by bubblesort for file2.txt is {time_finder(number2, bubblesort)} seconds")
    print(f"Time taken by insertionsort for file1.txt is {time_finder(number1, insertionsort)} seconds")
    print(f"Time taken by insertionsort for file2.txt is {time_finder(number2, insertionsort)} seconds")
    print(f"Time taken by selectionsort for file1.txt is {time_finder(number1, selection)} seconds")
    print(f"Time taken by selectionsort for file2.txt is {time_finder(number2, selection)} seconds")
    print(f"Time taken by mergesort for file1.txt is {time_finder(number1, mergesort)} seconds")
    print(f"Time taken by mergesort for file2.txt is {time_finder(number2, mergesort)} seconds")
    print(f"Time taken by heapsort for file1.txt is {time_finder(number1, heapsort)} seconds")
    print(f"Time taken by heapsort for file2.txt is {time_finder(number2, heapsort)} seconds")
    print(f"Time taken by counting_sort for file1.txt is {time_finder(number1, counting_sort)} seconds")
    print(f"Time taken by counting_sort for file2.txt is {time_finder(number2, counting_sort)} seconds")
    
    time=[]
    time.append(time_finder(number1, bubblesort))
    time.append(time_finder(number1, insertionsort))
    time.append(time_finder(number1, selection))
    time.append(time_finder(number1, mergesort))
    time.append(time_finder(number1, heapsort))
    time.append(time_finder(number1, counting_sort))
    print(f"The sorting algorithm that takes the least time is {['bubblesort', 'insertionsort', 'selectionsort'][time.index(min(time))]}")
    print(f"implementing {['bubblesort', 'insertionsort', 'selectionsort'][time.index(min(time))]} on both the files and saving it to file3.txt and file4.txt")
    if time.index(min(time))==0:
        bubblesort(number1)
        bubblesort(number2)
    elif time.index(min(time))==1:
        insertionsort(number1)
        insertionsort(number2)
    elif time.index(min(time))==2:
        selection(number1)
        selection(number2)
    elif time.index(min(time))==3:
        mergesort(number1)
        mergesort(number2)
    elif time.index(min(time))==4:
        heapsort(number1)
        heapsort(number2)
    else :
        counting_sort(number1)
        counting_sort(number2)
    savefile(number1, "file3.txt")
    savefile(number2, "file4.txt")
    print("Files saved successfully")

    print(f"Time taken by bubblesort for file3.txt is {time_finder(number1, bubblesort)} seconds ")
    print(f"Time taken by bubblesort for file4.txt is {time_finder(number2, bubblesort)} seconds")
    print(f"Time taken by insertionsort for file3.txt is {time_finder(number1, insertionsort)} seconds")
    print(f"Time taken by insertionsort for file4.txt is {time_finder(number2, insertionsort)} seconds")
    print(f"Time taken by selectionsort for file3.txt is {time_finder(number1, selection)} seconds")
    print(f"Time taken by selectionsort for file4.txt is {time_finder(number2, selection)} seconds")
    print(f"Time taken by mergesort for file3.txt is {time_finder(number1, mergesort)} seconds")
    print(f"Time taken by mergesort for file4.txt is {time_finder(number2, mergesort)} seconds")
    print(f"Time taken by heapsort for file3.txt is {time_finder(number1, heapsort)} seconds")
    print(f"Time taken by heapsort for file4.txt is {time_finder(number2, heapsort)} seconds")
    print(f"Time taken by counting_sort for file3.txt is {time_finder(number1, counting_sort)} seconds")
    print(f"Time taken by counting_sort for file4.txt is {time_finder(number2, counting_sort)} seconds")
    

    time1=[]
    time1.append(time_finder(number1, bubblesort))
    time1.append(time_finder(number1, insertionsort))
    time1.append(time_finder(number1, selection))
    time1.append(time_finder(number1, mergesort))
    time1.append(time_finder(number1, heapsort))
    time1.append(time_finder(number1, counting_sort))
    plt.plot(['bubblesort', 'insertionsort', 'selectionsort' , 'mergesort' , 'heapsort' , 'counting_sort'], time, label="Time for unsorted array")
    plt.plot(['bubblesort', 'insertionsort', 'selectionsort' , 'mergesort' ,  'heapsort' , 'counting_sort'], time1, label="Time for sorted array")
    plt.legend()
    plt.savefig('graph.png')
    plt.show()