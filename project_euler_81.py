
def read_matrix():
    with open("matrix.txt", "r") as f:
        lines = f.readlines()

    matrix = []
    for rows in lines:
        row = [int(float(x)) for x in rows.replace(',', ' ').split()]
        matrix.append(row)

    return matrix


def min_path_sum():
    matrix = read_matrix()

    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                # first row: can only come from the left
                matrix[i][j] += matrix[i][j - 1]
            elif j == 0:
                # first column: can only come from above
                matrix[i][j] += matrix[i - 1][j]
            else:
                # general case: take the minimum from above or left
                matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    # end position contains minimum sum
    return matrix[79][79]


print(min_path_sum())
