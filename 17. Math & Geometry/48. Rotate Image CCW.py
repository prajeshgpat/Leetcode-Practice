def rotate_counterclockwise(matrix: list[list[int]]):
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top < bottom:
        for i in range(bottom - top):
            # save the top left
            topLeft = matrix[top][left + i]

            # move top right into top left
            matrix[top][left + i] = matrix[top + i][right]

            # move bottom right into top right
            matrix[top + i][right] = matrix[bottom][right - i]

            # move bottom left into bottom right
            matrix[bottom][right - i] = matrix[bottom - i][left]

            # move top left into bottom left
            matrix[bottom - i][left] = topLeft

        top += 1
        bottom -= 1
        left += 1
        right -= 1

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
    print(rotate_counterclockwise(matrix))


"""[Python]
assert rotate_counterclockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
assert rotate_counterclockwise([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]) == [[11, 10, 7, 16], [9, 8, 6, 12], [1, 4, 3, 14], [5, 2, 13, 15]]
assert rotate_counterclockwise([[11, 7, 18], [2, 14, 4], [19, 6, 13]]) == [[18, 4, 13], [7, 14, 6], [11, 2, 19]]
assert rotate_counterclockwise([[7, 9, 15, 12], [8, 18, 16, 1], [6, 14, 3, 11], [17, 2, 5, 10]]) == [[12, 1, 11, 10], [15, 16, 3, 5], [9, 18, 14, 2], [7, 8, 6, 17]]
assert rotate_counterclockwise([[6, 14, 3, 10, 19], [8, 5, 17, 16, 12], [4, 9, 2, 13, 7], [18, 1, 11, 20, 15], [7, 16, 14, 12, 10]]) == [[19, 12, 7, 15, 10], [10, 16, 13, 20, 12], [3, 17, 2, 11, 14], [14, 5, 9, 1, 16], [6, 8, 4, 18, 7]]
"""
