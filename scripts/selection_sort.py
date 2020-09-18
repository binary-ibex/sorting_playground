import matplotlib.pyplot as plt
import numpy as np
import time

np.random.seed(120)

def selection(unsorted_array):
    start = time.time()
    for focus_number in range(len(unsorted_array)-1):
        for number in range(focus_number, len(unsorted_array)):
            if unsorted_array[focus_number]>unsorted_array[number]:
                unsorted_array[focus_number], unsorted_array[number] = unsorted_array[number], unsorted_array[focus_number]
    end = time.time() - start
    return end

time_required = {}
for length in range(10,2000, 10):
    time_required[length] = selection(np.random.randint(1,1000, length))

plt.plot(time_required.keys(), time_required.values())
plt.xlabel("length of input unsorted array ")
plt.ylabel("Time in seconds")
plt.title("Selection sort")
plt.show()
