""" Bubble sort is a sorting algorithm that compares two adjacent
 elements and swaps them until they are in the intended order.
 And here is the python program for bubble sort in ascending order."""


# The main function to do bubble sort the list
def bubble_sort(number_list):
    # loop to access each array element
    for looping in range(len(number_list)-1, 0, -1):
        for num in range(looping):
            # compare two adjacent elements
            # change > to < to sort in descending order. For now it is ending order
            if number_list[num] > number_list[num+1]:
                # swapping elements if elements
                # are not in the intended order
                number_list[num + 1], number_list[num] = number_list[num], number_list[num+1]


def main():
    number_list = [3, 1, 9, 1, 5, 7, 2]
    bubble_sort(number_list)
    print("The Sorted list in ascending Order is ", number_list)


main()
