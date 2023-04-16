import pygame
import numpy as np
# Initialize Pygame
pygame.init()
# Set the dimensions of the game window
WIDTH, HEIGHT = 540, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")
# Set the font style
FONT = pygame.font.SysFont("comicsansms", 32)
# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Set the Sudoku board dimensions
ROWS, COLS = 9, 9
# Create a Sudoku board
board = np.array(
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
])
# Create a copy of the board
board_copy = np.copy(board)
# Set the current cell position
current_pos = None
# Set the game loop flag
running = True
# Define functions
def draw_board():
    """
    Draws the Sudoku board.
    """
    # Clear the window
    WINDOW.fill(WHITE)
    # Draw the cells
    for row in range(ROWS):
        for col in range(COLS):           # Set the cell position and dimensions

            x, y = col * 60, row * 60 + 60

            cell_width, cell_height = 60, 60

            # Draw the cell

            pygame.draw.rect(WINDOW, BLACK, (x, y, cell_width, cell_height), 2)

            # Draw the cell value

            value = board[row][col]

            if value != 0:

                text = FONT.render(str(value), True, BLACK)

                text_rect = text.get_rect(center=(x + cell_width // 2, y + cell_height // 2))

                WINDOW.blit(text, text_rect)

            # Highlight the current cell

            if current_pos == (row, col):

                pygame.draw.rect(WINDOW, GREEN, (x, y, cell_width, cell_height), 2)

def draw_buttons():

    """

    Draws the game buttons.

    """

    # Set the button dimensions

    button_width, button_height = 80, 40

    # Draw the solve button

    solve_button = pygame.draw.rect(WINDOW, GRAY, (WIDTH // 2 -
button_width // 2, HEIGHT - 100, button_width, button_height))

solve_text = FONT.render("Solve", True, WHITE)

solve_text_rect = solve_text.get_rect(center=solve_button.center)

WINDOW.blit(solve_text, solve_text_rect)
# Draw the reset button

reset_button = pygame.draw.rect(WINDOW, GRAY, (WIDTH // 2 - button_width // 2 - 100, HEIGHT - 100, button_width, button_height))

reset_text = FONT.render("Reset", True, WHITE)

reset_text_rect = reset_text.get_rect(center=reset_button.center)

WINDOW.blit(reset_text, reset_text_rect)

# Draw the clear button

clear_button = pygame.draw.rect(WINDOW, GRAY, (WIDTH // 2 - button_width // 2 + 100, HEIGHT - 100, button_width, button_height))

clear_text = FONT.render("Clear", True, WHITE)

clear_text_rect = clear_text.get_rect(center=clear_button.center)

WINDOW.blit(clear_text, clear_text_rect)

# Draw the reset button

reset_button = pygame.draw.rect(WINDOW, GRAY, (WIDTH // 2 - button_width // 2 - 100, HEIGHT - 100, button_width, button_height))

reset_text = FONT.render("Reset", True, WHITE)

reset_text_rect = reset_text.get_rect(center=reset_button.center)

WINDOW.blit(reset_text, reset_text_rect)

# Draw the clear button

clear_button = pygame.draw.rect(WINDOW, GRAY, (WIDTH // 2 - button_width // 2 + 100, HEIGHT - 100, button_width, button_height))

clear_text = FONT.render("Clear", True, WHITE)

clear_text_rect = clear_text.get_rect(center=clear_button.center)

WINDOW.blit(clear_text, clear_text_rect)

def select_cell(pos):
"""
Selects the current cell based on the given position.
"""
global current_pos
# Set the current cell position based on the given position

row, col = pos[1] // 60 - 1, pos[0] // 60

if 0 <= row < ROWS and 0 <= col < COLS:

    current_pos = (row, col)

else:

    current_pos = None

# Set the current cell position based on the given position

row, col = pos[1] // 60 - 1, pos[0] // 60

if 0 <= row < ROWS and 0 <= col < COLS:

    current_pos = (row, col)

else:

    current_pos = None

def solve():

"""

Solves the Sudoku board.

"""

# Solve the board using backtracking

def solve_board(board):

# Find an empty cell

empty_cell = find_empty_cell(board)
    # If there are no more empty cells, the board is solved

    if empty_cell is None:

        return True

    # Try each number from 1 to 9

    for num in range(1, 10):

        # If the number is valid in the current cell, add it to the board and recursively solve the board
        if is_valid(board, empty_cell, num)
            row, col = empty_cell
            board[row][col] = num
            if solve_board(board):
                return True
            board[row][col] in0
    return False
# Find an empty cell
def find_empty_cell(board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                return row, col
    return None
# Check if the given number is valid in the given cell
def is_valid(board, cell, num):
    row, col = cell
    # Check row
    if num in board[row, :]:
        return False
    # Check column
    if num in board[:, col]:
        return False
    # Check subgrid
    subgrid_row, subgrid_col = row // 3 * 3, col // 3 * 3
    subgrid = board[subgrid_row:subgrid_row + 3, subgrid_col:subgrid_col + 3]
    if num in subgrid:
        return False
    return True
# Solve the board
solve_board(board)
def reset():
"""
Resets the Sudoku board to the initial state.
"""
global board, current_pos
board = np.copy(board_copy)
current_pos = None
def clear():
"""
Clears the current cell.
"""
global boar
if current_pos is not None:
row, col = current_pos
board[row][col] = 0
board[row][col] = 0
def main():
global board, board_copy, current_pos
# Initialize the game
pygame.init()
pygame.display.set_caption("Sudoku Solver")
WINDOW.fill(WHITE)
# Create the board
board = np.zeros((9, 9), dtype=int)
board_copy = np.copy(board)
# Draw the board
draw_board(board)
# Main game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Select the current cell
            pos = pygame.mouse.get_pos()
           select_cell(pos)
        elif event.type == pygame.KEYDOWN:
            # If a number key is pressed, add the number to the board
            if event.unicode.isdigit() and current_pos is not None:
                row, col = current_pos
                board[row][col] = int(event.unicode)
    # Draw the board
    draw_board(board)
    # Draw the solve, reset, and clear buttons
    draw_buttons()
    # Check if the solve button is clicked
    if pygame.mouse.get_pressed()[0] and solve_button.collidepoint(pygame.mouse.get_pos()):
        solve()
    # Check if the reset button is clicked
    if pygame.mouse.get_pressed()[0] and reset_button.collidepoint(pygame.mouse.get_pos()):
        reset()
    # Check if the clear button is clicked
    if pygame.mouse.get_pressed()[0] and clear_button.collidepoint(pygame.mouse.get_pos()):
        clear()
    # Update the display
    pygame.display.update()
if __name__ == "__main__":
    main()


