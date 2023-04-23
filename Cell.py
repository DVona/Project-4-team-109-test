from sudoku_generator import SudokuGenerator

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        pass
    '''
    Setter for this cell’s value
    '''
    def set_cell_value(self, value):
        self.value = self.set_sketched_value(value)
        pass

    '''
    Setter for this cell’s sketched value
    '''
    def set_sketched_value(self, value):
        self.set_sketched_value = value

    '''
    Draws this cell, along with the value inside it.
    If this cell has a nonzero value, that value is displayed.
    Otherwise, no value is displayed in the cell.
    The cell is outlined red if it is currently selected.
    '''
    def draw(self):
        pass

class Board:
# This class represents an entire Sudoku board. A Board object has 81 Cell objects.
    def __init__(self, width, height, screen, difficulty):
        sudoku = SudokuGenerator(width, difficulty)
        sudoku.fill_values()
        sudoku.remove_cells()
        board = sudoku.get_board()
        solved_board = sudoku.solved_board

        board_cells = []
        for i in range(height):
            board_cells.append([])
            for j in range(width):
                board_cells[i].append(Cell(board[i][j], [i], [j], screen))


        '''
    Constructor for the Board class.
    screen is a window from PyGame.
    difficulty is a variable to indicate if the user chose easy, medium, or hard.
    '''

    def draw(self):
        '''
    Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
    Draws every cell on this board.
    '''

    def select(self, row, col):
        '''
    Marks the cell at (row, col) in the board as the current selected cell.
    Once a cell has been selected, the user can edit its value or sketched value.
    '''

    def click(self, x, y):
        '''
    If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
    of the cell which was clicked. Otherwise, this function returns None.
    '''

    def clear(self):
        '''
    Clears the value cell. Note that the user can only remove the cell values and sketched value that are
    filled by themselves.
    '''

    def sketch(self, value):
        '''
    Sets the sketched value of the current selected cell equal to user entered value.
    It will be displayed at the top left corner of the cell using the draw() function.
    '''
    def place_number(self, value):
        '''
    Sets the value of the current selected cell equal to user entered value.
    Called when the user presses the Enter key.
    '''
    def reset_to_original(self):
        '''
    Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
    '''

    def is_full(self):
        '''
    Returns a Boolean value indicating whether the board is full or not.
    '''
    def update_board(self):
        '''
    Updates the underlying 2D board with the values in all cells.
    '''
    def find_empty(self):
        '''
    Finds an empty cell and returns its row and col as a tuple (x, y).
    '''
    def check_board(self):
        '''
    Check whether the Sudoku board is solved correctly."""
    '''



