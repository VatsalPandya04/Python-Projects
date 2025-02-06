def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_n_queens_util(board, col, N):
    # base case: If all queens are placed
    if col >= N:
        print_board(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, N) or res
            board[i][col] = 0  # backtrack

    return res

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens_util(board, 0, N):
        print(f"No solution exists for {N}x{N} board.")

if __name__ == "__main__":
    while True:
        print("\n[1] Solve\n[2] Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            N = int(input("Enter value of N: "))
            if N >= 4:
                solve_n_queens(N)
            else:
                print(f"\nN-Queen problem can't be solved for {N}x{N} matrix!")
        elif choice == '2':
            break
        else:
            print("\nEnter a valid choice!")
