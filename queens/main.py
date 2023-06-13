def can_queens_attack(q1_row, q1_col, q2_row, q2_col):
    # Check if queens are in the same row or column
    if q1_row == q2_row or q1_col == q2_col:
        return True

    # Check if queens are on the same diagonal
    if abs(q1_row - q2_row) == abs(q1_col - q2_col):
        return True

    return False

# Example usage
q1_row = int(input("Enter the row number of queen 1 (0-7): "))
q1_col = int(input("Enter the column number of queen 1 (0-7): "))
q2_row = int(input("Enter the row number of queen 2 (0-7): "))
q2_col = int(input("Enter the column number of queen 2 (0-7): "))

if can_queens_attack(q1_row, q1_col, q2_row, q2_col):
    print("Queens can attack each other!")
else:
    print("Queens cannot attack each other!")
