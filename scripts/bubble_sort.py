import matplotlib.pyplot as plt
import numpy as np
import time

np.random.seed(120)

def bubble(unsorted_array):
    start = time.time()
    for _ in range(len(unsorted_array)-1):
        for number in range(1, len(unsorted_array)):
            if unsorted_array[number-1]>unsorted_array[number]:
                unsorted_array[number-1], unsorted_array[number] = unsorted_array[number], unsorted_array[number-1]
    end = time.time() - start
    return end

time_required = {}
for length in range(10,2000, 10):
    time_required[length] = bubble(np.random.randint(1,1000, length))

plt.plot(time_required.keys(), time_required.values())
plt.xlabel("length of input unsorted array ")
plt.ylabel("Time in seconds")
plt.title("Bubble sort")
plt.show()
