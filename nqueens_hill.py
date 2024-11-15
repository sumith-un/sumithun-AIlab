import random

def random_initial_board(n):
    """Generate a random initial configuration of queens."""
    return [random.randint(0, n - 1) for _ in range(n)]

def calculate_conflicts(board):
    """Calculate the number of conflicts on the board."""
    conflicts = 0
    n = len(board)
    
    # Check each pair of queens
    for i in range(n):
        for j in range(i + 1, n):
            # Check if queens i and j are on the same diagonal
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def generate_neighbors(board):
    """Generate all neighbors by moving each queen to a different row in its column."""
    neighbors = []
    n = len(board)
    
    for i in range(n):
        # Try moving queen i to a different row
        for row in range(n):
            if row != board[i]:
                new_board = board[:]
                new_board[i] = row  # Move the queen to a new row
                neighbors.append(new_board)
    return neighbors

def hill_climbing(n):
    """Solve the N-Queens problem using Hill Climbing."""
    # Step 1: Start with a random configuration
    current_board = random_initial_board(n)
    current_conflicts = calculate_conflicts(current_board)
    
    # Step 2: Hill climbing loop
    while current_conflicts > 0:
        # Step 2a: Generate all possible neighbors
        neighbors = generate_neighbors(current_board)
        
        # Step 2b: Find the neighbor with the least number of conflicts
        best_neighbor = None
        best_conflicts = current_conflicts
        for neighbor in neighbors:
            neighbor_conflicts = calculate_conflicts(neighbor)
            if neighbor_conflicts < best_conflicts:
                best_neighbor = neighbor
                best_conflicts = neighbor_conflicts
        
        # Step 2c: If no better neighbor is found, we're stuck in a local minimum
        if best_conflicts >= current_conflicts:
            print("Stuck in a local minimum")
            return current_board
        
        # Step 2d: Move to the best neighbor
        current_board = best_neighbor
        current_conflicts = best_conflicts
    
    # Step 3: Return the solution (no conflicts)
    print("Solution found!")
    return current_board

def print_board(board):
    """Print the board configuration."""
    n = len(board)
    for row in range(n):
        row_str = ['Q' if col == board[row] else '.' for col in range(n)]
        print(" ".join(row_str))

# Example usage:
n = 8  # 8-Queens problem
solution = hill_climbing(n)
print_board(solution)
