import matplotlib.pyplot as plt
import numpy as np
import time

np.random.seed(120)



# insertion sort function
def insertion_sort(unsorted_array):
    start = time.time()
    for number_index in range(1, len(unsorted_array)):
        i = number_index
        while ((unsorted_array[i] < unsorted_array[i-1]) and i>0):
            unsorted_array[i], unsorted_array[i-1] = unsorted_array[i-1], unsorted_array[i]
            i -= 1
    end = time.time() - start
    return end



#store the time required for the length of the input
time_required = {}
for length in range(10,2000, 10):
    time_required[length] = insertion_sort(np.random.randint(1,1000, length))

# ploting the time graph
plt.plot(time_required.keys(), time_required.values())
plt.xlabel("length of input unsorted array ")
plt.ylabel("Time in seconds")
plt.title("Insertion sort")
plt.show()
