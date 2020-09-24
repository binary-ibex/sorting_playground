import matplotlib.pyplot as plt
import numpy as np
import time

np.random.seed(120)

def sort_using_merg(lst):

    start = time.time()

    def merg(left, right):
        result = []
        i, j = 0,0
        while i<len(left) and j<len(right):
            if (left[i] < right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result


    def merg_sort(lst):
        if len(lst)<= 1:
            return lst

        mid = len(lst) // 2

        left = merg_sort(lst[:mid])
        right = merg_sort(lst[mid:])

        return merg(left, right)

        pass
    merg_sort(lst)
    return time.time() - start


time_required = {}
for length in range(10,2000, 100):
    time_required[length] = sort_using_merg(list(np.random.randint(1,1000, length)))

plt.plot(time_required.keys(), time_required.values())
plt.xlabel("length of input unsorted array ")

plt.ylabel("Time in seconds")
plt.title("merg sort")
plt.show()
