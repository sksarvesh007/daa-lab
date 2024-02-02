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
    time=[]
    time.append(time_finder(number1, bubblesort))
    time.append(time_finder(number1, insertionsort))
    time.append(time_finder(number1, selection))
    print(f"The sorting algorithm that takes the least time is {['bubblesort', 'insertionsort', 'selectionsort'][time.index(min(time))]}")
    print(f"implementing {['bubblesort', 'insertionsort', 'selectionsort'][time.index(min(time))]} on both the files and saving it to file3.txt and file4.txt")
    if time.index(min(time))==0:
        bubblesort(number1)
        bubblesort(number2)
    elif time.index(min(time))==1:
        insertionsort(number1)
        insertionsort(number2)
    else:
        selection(number1)
        selection(number2)
    savefile(number1, "file3.txt")
    savefile(number2, "file4.txt")
    print("Files saved successfully")

    print(f"Time taken by bubblesort for file3.txt is {time_finder(number1, bubblesort)} seconds ")
    print(f"Time taken by bubblesort for file4.txt is {time_finder(number2, bubblesort)} seconds")
    print(f"Time taken by insertionsort for file3.txt is {time_finder(number1, insertionsort)} seconds")
    print(f"Time taken by insertionsort for file4.txt is {time_finder(number2, insertionsort)} seconds")
    print(f"Time taken by selectionsort for file3.txt is {time_finder(number1, selection)} seconds")
    print(f"Time taken by selectionsort for file4.txt is {time_finder(number2, selection)} seconds")

    time1=[]
    time1.append(time_finder(number1, bubblesort))
    time1.append(time_finder(number1, insertionsort))
    time1.append(time_finder(number1, selection))
    plt.plot(['bubblesort', 'insertionsort', 'selectionsort'], time, label="Time for unsorted array")
    plt.plot(['bubblesort', 'insertionsort', 'selectionsort'], time1, label="Time for sorted array")
    plt.legend()
    plt.savefig('graph.png')
    plt.show()