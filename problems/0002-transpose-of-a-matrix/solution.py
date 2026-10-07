def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    result = []

    for col in range(len(a[0])):
        new_row = []

        for row in range(len(a)):
            new_row.append(a[row][col])

        result.append(new_row)

    return result