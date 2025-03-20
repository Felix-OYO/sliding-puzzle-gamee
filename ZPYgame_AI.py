"""  
# Sliding Puzzle Game  
  
## How to Play  
  
**Objective:**  
- Arrange the tiles in numerical order with the empty space at the bottom right to win the game.  
  
**Controls:**  
- Click on a tile to select it.  
- Use the arrow keys (Up, Down, Left, Right) to move the selected tile towards the empty space.  
- Press the spacebar to automatically win the game.  
  
**Game Features:**  
- Randomized starting grid for a unique challenge every time.  
- Visual highlight on selected tiles.  
- Automatic increase in difficulty after each win.  
  
## System Requirements  
- Python 3.x  
- Pygame library installed  
  
## Installation  
1. Ensure Python and Pygame are installed on your system.  
2. Download the game code and this README file.  
3. Run the game script using a Python interpreter.  
  
Enjoy the game! If you have any questions or feedback, feel free to reach out.  
"""  
  
import pygame    
import sys    
import random    
  
# Initialize Pygame    
pygame.init()    
  
# Set up display    
width, height = 300, 300  # Square shape for a 3x3 grid    
screen = pygame.display.set_mode((width, height))    
pygame.display.set_caption('Sliding Puzzle')    
  
# Colors    
WHITE = (255, 255, 255)    
BLACK = (0, 0, 0)    
GREEN = (0, 255, 0)    
  
# Variables    
tile_size = width // 3    
selected = None  # Track selected tile    
  
def create_grid(num_tiles):    
    # Create a list of tiles (1 to num_tiles) plus an empty space    
    grid = list(range(1, num_tiles)) + [0]    
    random.shuffle(grid)    
    return [grid[i:i + 3] for i in range(0, len(grid), 3)]    
  
def draw_grid(grid):    
    screen.fill(WHITE)    
    for row in range(3):    
        for col in range(3):    
            tile = grid[row][col]    
            if tile != 0:  # Don't draw the empty space    
                pygame.draw.rect(screen, BLACK, (col * tile_size, row * tile_size, tile_size, tile_size))    
                font = pygame.font.Font(None, 100)    
                text = font.render(str(tile), True, WHITE)    
                text_rect = text.get_rect(center=(col * tile_size + tile_size // 2, row * tile_size + tile_size // 2))    
                screen.blit(text, text_rect)    
            if selected == (row, col):    
                pygame.draw.rect(screen, GREEN, (col * tile_size, row * tile_size, tile_size, tile_size), 5)  # Highlight selected    
  
def swap_tiles(grid, r1, c1, r2, c2):    
    grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]    
  
def is_solved(grid, num_tiles):    
    correct_order = list(range(1, num_tiles)) + [0]    
    # Flatten the grid for comparison    
    flat_grid = [tile for row in grid for tile in row]    
    return flat_grid == correct_order    
  
def draw_win_message():    
    font = pygame.font.Font(None, 60)    
    text = font.render("You Win!", True, GREEN)    
    text_rect = text.get_rect(center=(width // 2, height // 2))    
    screen.blit(text, text_rect)    
    pygame.display.flip()    
    pygame.time.wait(2000)  # Wait for 2 seconds    
  
def show_instructions():  
    screen.fill(WHITE)  
    instructions = [  
        "Sliding Puzzle Game",  
        "Arrange tiles in order:",  
        "1 2 3",  
        "4 5 6",  
        "7 8 _",  
        "Click to select tiles.",  
        "Use arrow keys to move.",  
        "Press space to auto-win.",  
    ]  
    font = pygame.font.Font(None, 24)  
    for i, line in enumerate(instructions):  
        text = font.render(line, True, BLACK)  
        text_rect = text.get_rect(center=(width // 2, 30 + i * 30))  
        screen.blit(text, text_rect)  
    pygame.display.flip()  
    pygame.time.wait(4000)  # Show instructions for 4 seconds  
  
# Initialize game    
num_tiles = 9  # Start with 8 tiles and an empty space    
grid = create_grid(num_tiles)    
running = True    
  
show_instructions()  # Display instructions at the start  
  
while running:    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:    
            running = False    
        elif event.type == pygame.MOUSEBUTTONDOWN:    
            x, y = event.pos    
            selected = (y // tile_size, x // tile_size)  # Select tile    
        elif event.type == pygame.KEYDOWN and selected:    
            row, col = selected    
            if event.key == pygame.K_UP and row > 0 and grid[row-1][col] == 0:    
                swap_tiles(grid, row, col, row-1, col)    
            elif event.key == pygame.K_DOWN and row < 2 and grid[row+1][col] == 0:    
                swap_tiles(grid, row, col, row+1, col)    
            elif event.key == pygame.K_LEFT and col > 0 and grid[row][col-1] == 0:    
                swap_tiles(grid, row, col, row, col-1)    
            elif event.key == pygame.K_RIGHT and col < 2 and grid[row][col+1] == 0:    
                swap_tiles(grid, row, col, row, col+1)    
            elif event.key == pygame.K_SPACE:    
                # Automatically win the game    
                draw_win_message()    
                num_tiles += 1  # Increase the number of tiles    
                grid = create_grid(num_tiles)  # Reset the game    
  
    draw_grid(grid)    
    pygame.display.flip()    
  
    if is_solved(grid, num_tiles):    
        draw_win_message()    
        num_tiles += 1  # Increase the number of tiles    
        grid = create_grid(num_tiles)  # Reset the game    
  
pygame.quit()    
sys.exit() 

  