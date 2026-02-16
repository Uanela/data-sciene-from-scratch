# A = [[1, 2, 3],
#      [4, 5, 6]]

# B = [[1, 2],
#      [3, 4],
#      [5, 6]]

# def shape(A):
#     num_rows = len(A)
#     num_cols = len(A[0]) if A else 0
#     return num_rows, num_cols

# def get_row(A, i):
#     return A[i]

# def get_column(A, j):
#     return [A_i[j] for A_i in A]

# def make_matrix(num_rows, num_cols, entry_fn):
#     """returns a num_rows x num_cols matrix whose
#     (i, j)th entry if entry_fn(i, j)"""
#     return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

# def is_diagonal(i, j):
#     """1's on the 'diagonal' , 0's everwhere else"""
#     return 1 if i == j else 0

friends = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
      (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships = [[1 if (x, k) in friends or (k, x) in friends else 0
                for x in range(10)] for k in range(10)]

print(1, 2, friendships[1][2] == 1)
print(3, 2, friendships[3][2] == 1)

