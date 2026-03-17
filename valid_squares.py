from itertools import combinations

def is_valid_square(square):
    """
    This function checks if a list of four points represents a valid square on an 8x8 game board.

    Args:
        points: A list containing four points, each point represented as a list of two integers (row, column).

    Returns:
        True if the points form a valid square, False otherwise.
    """

    # Check all points are unique
    if len(set(tuple(p) for p in square)) != 4:
        return False
    
    # Calculate all pairwise distances
    distances = []
    for p1, p2 in combinations(square, 2):
        dist = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
        distances.append(dist)
    
    # Sort distances
    distances.sort()
    
    # For a square: 4 sides equal, 2 diagonals equal, and diagonal > side
    if len(distances) == 6:
        side = distances[0]
        if distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5] and distances[4] > distances[0]:
            return True
    
    return False

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
                    
    print("There are " + str(len(unique_squares)) + " unique squares on a " + str(board_size) + "x" + str(board_size) + " board.")
    return unique_squares



print("testing valid square: " + str(is_valid_square([[0, 1], [1, 7], [6, 0], [7, 6]])))
