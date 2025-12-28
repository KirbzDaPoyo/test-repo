board_2D = [[0 for col in range(4)] for row in range(4)]

def board_reset():
    """
	Resets the chess board to its initial state of emptiness.
	"""

    for row in range(len(board_2D)):
        for col in range(len(board_2D[row])):
            board_2D[row][col] = 0

def find_next_location(starting_position):
    """
    Finds the next available board position starting from the input starting_position.
    Returns the available position number or -1 if there's no available position.
    """

    position = starting_position
    while position < len(board_2D) * len(board_2D):
        # Here, the row index is calculated as integer division by 4, which gives the correct row index for a 4-column board.
        # On the other hand, the column index is calculated as the remainder when divided by 4.
        row = position // len(board_2D)
        col = position % len(board_2D[row])
        if board_2D[row][col] == 0:
            return position
        position += 1

    return -1

def place_queen(queen_number, starting_position=None):
    """
    Places a queen of the input queen_number on the next available board position starting from the input starting_position.
    If no starting_position is provided, starts from position 0.
    Then, calls set_conflict_locations to updates the board.
    Returns the next position index, or -1 if no position is available.
    """

    if starting_position is None:
        starting_position = 0

    position = find_next_location(starting_position)

    if position == -1:
        return -1

    # These are calculated the same as in find_next_location.
    row = position // len(board_2D)
    col = position % len(board_2D[row])

    board_2D[row][col] = "Q" + str(queen_number)
    set_conflict_locations(queen_number, row, col)
    return position + 1

def set_conflict_locations(queen_number, queen_row, queen_col):
    """
    Marks conflict positions on the board for the queen of input queen_number placed at input row queen_row and input column queen_col.
    """
    
    queens = []
    for i in range(len(board_2D)):
        queens.append("Q" + str(i + 1))

    # Update conflicts in the same row
    for col in range(len(board_2D)):
        if board_2D[queen_row][col] not in queens:
            # Note: Only overwrite IF cell is empty OR current queen has lower number than existing conflict marker
            # This ensures the "lowest queen number" rule is maintained for overlapping conflict zones
            if board_2D[queen_row][col] == 0 or queen_number < board_2D[queen_row][col]:
                board_2D[queen_row][col] = queen_number

    # Update conflicts in the same column
    for row in range(len(board_2D)):
        if board_2D[row][queen_col] not in queens:
            if board_2D[row][queen_col] == 0 or queen_number < board_2D[row][queen_col]:
                board_2D[row][queen_col] = queen_number

    # Update conflicts in top-left to bottom-right diagonal
    # We do this by calculating the top-leftmost cell of the diagonal that passes through (queen_row, queen_col).
    row = queen_row - min(queen_row, queen_col)
    col = queen_col - min(queen_row, queen_col)
    while row < len(board_2D) and col < len(board_2D):
        if board_2D[row][col] not in queens:
            if board_2D[row][col] == 0 or queen_number < board_2D[row][col]:
                board_2D[row][col] = queen_number
        row += 1
        col += 1

    # Update conflicts in top-right to bottom-left diagonal
    # We do this by calculating the top-rightmost cell of the diagonal that passes through (queen_row, queen_col).
    # Is this confusing enough yet?
    row = queen_row - min(queen_row, len(board_2D) - 1 - queen_col)
    col = queen_col + min(queen_row, len(board_2D) - 1 - queen_col)
    while row < len(board_2D) and col >= 0:
        if board_2D[row][col] not in queens:
            if board_2D[row][col] == 0 or queen_number < board_2D[row][col]:
                board_2D[row][col] = queen_number
        row += 1
        col -= 1 

def dead_end():
    """
    Resets the board and re-places all previously placed queens.
    """

    board_reset()

def display_board():
    """
    Displays the current state of the chess board, in the form of four strings, each representing a row of the board.
    """

    for row in range(len(board_2D)):
        board_row = ""
        for col in range(len(board_2D[row])):
            cell = board_2D[row][col]
            board_row += str(cell) + "  "
        print(board_row)
    print()

def main():
    """
    Here we've got out main function to solve the 4-Queens problem. Here's how it works!
    1. Initialize variables to track the number of queens placed and their positions.
    2. While fewer than 4 queens are placed:
    3. Attempt to place the next queen using the place_queen function.
    4. If placement fails (returns -1), reset the board and adjust positions to try new placements.
    5. If placement succeeds, update the positions for the next queen and repeat from step 2.
    6. Once all 4 queens are placed, display the final board and print a success message.
    Most of the stuff happens in other functions anyway.
    """

    queens_placed = 0
    queen_positions = [0 for i in range(len(board_2D))]
    display_board()

    while queens_placed < len(queen_positions):
        result = place_queen(queens_placed + 1, queen_positions[queens_placed])
        display_board()

        if result == -1:
            # When stuck, reset completely and move Q1 to next position, which guarantees all possibilities are explored.
            queens_placed = 0
            queen_positions[0] += 1

            # Then, sync all queen starting positions to Q1's new position so that we don't re-explore dead branches of the search tree
            for i in range(1, len(queen_positions)):
                queen_positions[i] = queen_positions[0]
            dead_end()
        else:
            # When a queen is successfully placed, set all subsequent queens to start searching from the position
            # right after the current placement; we can maximize efficiency by skipping already-occupied positions.
            for i in range(queens_placed + 1, len(queen_positions)):
                queen_positions[i] = result
            queens_placed += 1

    display_board()
    print("We did it!")

main()