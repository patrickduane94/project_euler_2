
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
    min_path_sums = []  # store the minimum path sums for all starting points

    def compute_path(start_row):
        # initialize dp table by copying matrix values
        dp_table = [row[:] for row in matrix]

        # traverse columns left-to-right
        for j in range(1, cols):
            # left-to-right move
            for i in range(rows):
                dp_table[i][j] += dp_table[i][j - 1]

            # propagate values downward (top-down pass)
            for i in range(1, rows):
                dp_table[i][j] = min(dp_table[i][j], dp_table[i - 1][j] + matrix[i][j])

            # propagate values upward (bottom-up pass)
            for i in range(rows - 2, -1, -1):
                dp_table[i][j] = min(dp_table[i][j], dp_table[i + 1][j] + matrix[i][j])

        # return minimum value in the last column
        return min(dp_table[i][-1] for i in range(rows))

    # iterate over all starting rows in the first column
    for start_row in range(rows):
        min_path_sums.append(compute_path(start_row))

    # return the smallest minimum path sum
    return min(min_path_sums)


print(min_path_sum())
