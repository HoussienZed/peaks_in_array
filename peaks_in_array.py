def find_peaks(array):
    peaks_indices = []

    if array[0] > array[1]:  # assuming first element is a peak if greater than the second element
        peaks_indices.append(0)

    for i in range(1, len(array)):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            peaks_indices.append(i)

    return print(f"The indices of peaks in the array are {peaks_indices}")


tested_array = []
numbers_count = int(input("Enter how many numbers do you want to test: "))

for i in range(1, numbers_count + 1):
    number = int(input(f"Enter number {i}: "))
    tested_array.append(number)

print(f"The entered list of numbers is: {tested_array}")
find_peaks(tested_array)
