def find_peaks(array):
    peaks_indices = []

    if array[0] > array[1]:  # assuming first element is a peak if greater than the second element
        peaks_indices.append(0)

    for i in range(1, len(array)):
        if array[i - 1] < array[i] > array[i + 1]:
            peaks_indices.append(i)

    return print(f"The indices of peaks in the array are {peaks_indices}")


tested_array = []
numbers_count = int(input("Enter how many numbers do you want to test: "))

for i in range(numbers_count):
    number = int(input(f"Enter number {i}: "))
    numbers_count.append(number)
