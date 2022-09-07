# Optimized Bubble sort in Python
""" optimized bubble sort is more efficient as it only executes
the necessary steps and skips those that are not required.
And here is the python program for bubble sort in ascending order."""


def bubble_sort(number_list):
    # loop through each element of number_list
    for i in range(len(number_list)):
        # keep track of swapping
        swapped = 0
        # loop to access each number_list element
        for num in range(0, len(number_list) - i - 1):
            # compare two adjacent elements
            # change > to < to sort in descending order. For now it is ending order
            if number_list[num] > number_list[num+1]:
                # swapping elements if elements
                # are not in the intended order
                number_list[num + 1], number_list[num] = number_list[num], number_list[num+1]
                swapped = 1
        # no swapping means the array is already sorted
        if not swapped == 0:
            break


def main():
    number_list = [3, 1, 9, 1, 5, 7, 2]
    bubble_sort(number_list)
    print("The Sorted list in ascending Order is ", number_list)


main()
