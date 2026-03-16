from itertools import combinations

def is_valid_square(square):
    """
    This function checks if a list of four points represents a valid square on an 8x8 game board.

    Args:
        points: A list containing four points, each point represented as a list of two integers (row, column).

    Returns:
        True if the points form a valid square, False otherwise.
    """

    # Check for unique points
    if len(square) != 4:
        return False
    
    # Sort points by row and then column
    square = sorted(square)
    
    for point in range(1, len(square)):
        curr_point = square[point]
        prev_point = square[point-1]
        
        if curr_point[0] == prev_point[0] and curr_point[1] == prev_point[1]:
            return False
    
    # Check side length consistency
    # point 2 - point 1
    side1 = ((square[1][0] - square[0][0]) ** 2) + ((square[1][1] - square[0][1]) ** 2) ** 0.5
    # point 4 - point 3
    side2 = ((square[3][0] - square[2][0]) ** 2)  +((square[3][1] - square[2][1]) ** 2) ** 0.5
    # point 3 - point 1
    side3 = ((square[2][0] - square[0][0]) ** 2) + ((square[2][1] - square[0][1]) ** 2) ** 0.5
    # point 4 - point 2
    side4 = ((square[3][0] - square[1][0]) ** 2) + ((square[3][1] - square[1][1]) ** 2) ** 0.5
    
    
    # Check if both pairs of sides are equal
    if not (side1 == side2 and side3 == side4):
        return False
    

    # point 1 - point 4
    diag_length1 = (((square[0][0] - square[3][0]) ** 2) + ((square[0][1] - square[3][1]) ** 2)) ** 0.5
    # point 2 - point 3
    diag_length2 = (((square[1][0] - square[2][0]) ** 2) + ((square[1][1] - square[2][1]) ** 2)) ** 0.5

    if diag_length1 != diag_length2:
        return False    

    return True

def get_all_points(board_size):
    all_points = []
    for row in range(board_size):
        for col in range(board_size):
            point = [row, col]
            all_points.append(point)
    
    return all_points
    
def get_squares(board_size, num_points = 4):
    unique_squares = []
    points = get_all_points(board_size)
    
    squares = combinations(points, num_points)
    
    for square in squares:
        if is_valid_square(square):
            unique_squares.append(square)
                    
              
    return unique_squares



# print(is_valid_square([[0, 1], [1, 7], [6, 0], [7, 6]]))
