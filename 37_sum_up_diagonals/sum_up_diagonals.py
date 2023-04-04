def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    len_sides = len(matrix)
    sum = 0
    diag1 = [matrix[x][x] for x in range(len_sides)]
    diag2 = [matrix[-(x + 1)][x] for x in range(len_sides)]
    for x in range(len(diag1)):
        sum = sum + diag1[x] + diag2[x] 
    return sum 