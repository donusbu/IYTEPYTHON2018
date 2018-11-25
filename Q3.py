array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 4, 5, 2, 324, 6, 35, 344, 6, 34, 324, 4, 4, 5, 4, 7, 568, 78, 6, 4, 3, 343, 4]


def findLength(array):
    count = 0

    for i in array:
        count += 1
    return count

print(findLength(array))