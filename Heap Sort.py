"""
Heap Sort is a popular and efficient sorting algorithm in computer programming.
Heap sort works by visualizing the elements of the array as
 a special kind of complete binary tree called a heap.
"""


def heapify(number_list, length, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # Checking if left child of root exists
    #  and greater than root
    if left < length and number_list[i] < number_list[left]:
        largest = left

    # Checking if right child of root exists and
    # greater than root
    if right < length and number_list[largest] < number_list[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        (number_list[i], number_list[largest]) = (number_list[largest], number_list[i])  # swap
        heapify(number_list, length, largest)  # Heapify the root.


# The main function to do heap sort the list
def heap_sort(number_list):
    length = len(number_list)

    # Build a Max Heap.
    for i in range(length // 2 - 1, -1, -1):
        heapify(number_list, length, i)

    # One by one extract elements
    for i in range(length - 1, 0, -1):
        (number_list[i], number_list[0]) = (number_list[0], number_list[i])  # swap
        heapify(number_list, i, 0)


def main():
    number_list = [3, 1, 9, 1, 5, 7, 2]
    heap_sort(number_list)
    length = len(number_list)
    sorted_list = []
    for i in range(length):
        sorted_list.append(number_list[i])
    print('Heap Sorted list is', sorted_list)


main()
