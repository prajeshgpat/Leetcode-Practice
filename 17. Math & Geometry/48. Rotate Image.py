def rotate(matrix: list[list[int]]):
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # save the topleft
            topLeft = matrix[top][l + i]

            # move bottom left into top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move top right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # move top left into top right
            matrix[top + i][r] = topLeft
        r -= 1
        l += 1
    return matrix


testInputs = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
    [[11, 7, 18], [2, 14, 4], [19, 6, 13]],
    [[7, 9, 15, 12], [8, 18, 16, 1], [6, 14, 3, 11], [17, 2, 5, 10]],
    [
        [6, 14, 3, 10, 19],
        [8, 5, 17, 16, 12],
        [4, 9, 2, 13, 7],
        [18, 1, 11, 20, 15],
        [7, 16, 14, 12, 10],
    ],
]
for matrix in testInputs:
    print(rotate(matrix))


"""[Python]
assert rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
assert rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]) == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
assert rotate([[11, 7, 18], [2, 14, 4], [19, 6, 13]]) == [[19, 2, 11], [6, 14, 7], [13, 4, 18]]
assert rotate([[7, 9, 15, 12], [8, 18, 16, 1], [6, 14, 3, 11], [17, 2, 5, 10]]) == [[17, 6, 8, 7], [2, 14, 18, 9], [5, 3, 16, 15], [10, 11, 1, 12]]
assert rotate([[6, 14, 3, 10, 19], [8, 5, 17, 16, 12], [4, 9, 2, 13, 7], [18, 1, 11, 20, 15], [7, 16, 14, 12, 10]]) == [[7, 18, 4, 8, 6], [16, 1, 9, 5, 14], [14, 11, 2, 17, 3], [12, 20, 13, 16, 10], [10, 15, 7, 12, 19]]
"""
