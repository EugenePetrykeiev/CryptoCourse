from task1 import trials_val
from task2 import keys


def bin_search(numbers: list, range: list):
    iter = 0
    i = 0
    print(range)
    for num in numbers:
        print(num)
        if i == 0:
            first = 0
        else:
            first = range[i]
        last = range[i + 1]
        while first < last:
            middle = (first + last) // 2
            iter += 1
            # print(middle)
            if num == middle:
                print("Number:", num)
                print("Iterations:", iter)
                break
            else:
                if num < middle:
                    last = middle
                elif num > middle:
                    first = middle
    i += 1


bin_search(keys[:3], trials_val)
