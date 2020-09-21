import matplotlib.pyplot as plt
import numpy as np
import time

np.random.seed(120)



# quick sort function
def quick_sort(unsorted_array):
    start = time.time()
    def quick(unsorted_array):
        if len(unsorted_array)>1:
            pivot = unsorted_array.pop(-1)
            left = []
            right = []
            for number in unsorted_array:
                left.append(number) if number <= pivot else right.append(number)
            return quick(left) + [pivot] + quick(right)
        else:
            return unsorted_array
    quick(unsorted_array)
    end = time.time() - start
    return end



#store the time required for the length of the input
time_required = {}
for length in range(10,2000, 10):
    time_required[length] = quick_sort(list(np.random.randint(1,1000, length)))

# ploting the time graph
plt.plot(time_required.keys(), time_required.values())
plt.xlabel("length of input unsorted array ")
plt.ylabel("Time in seconds")
plt.title("quick sort")
plt.show()
