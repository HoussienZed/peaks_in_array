def find_peaks(array):
    peaks_indices = []

    if array[0] > array[1]:  # assuming first element is a peak if greater than the second element
        peaks_indices.append(0)

    for i in range(1, len(array)):
        if array[i - 1] < array[i] > array[i + 1]:
            peaks_indices.append(i)

    return print(f"The indices of peaks in the array are {peaks_indices}")


numbers = list(input("numbers"))
find_peaks(numbers)
