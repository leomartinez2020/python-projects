"""
Clone of 2048 game.
"""

#import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    templist = [0]*len(line) # list of zeroes same length as line
    counter = 0 # counter for tempList
    for elem in line:
        if elem != 0:
            templist[counter] = elem # only numbers different from
            counter += 1      # zero are copied
    resultlist = [0]*len(line) # list for final result
    ind, jind = 0, 0
    while ind < len(templist) - 1:
        if templist[ind] == templist[ind+1]:
            resultlist[jind] = templist[ind] + templist[ind+1] # if consecutive numbers
            ind += 2               # are equal they are
        else:                    # copied to list resultList
            resultlist[jind] = templist[ind]
            ind += 1
        jind += 1
    if templist[-1] != 0 and ind < len(line):
        resultlist[jind] = templist[-1]  # if last number is not zero and 
    return resultlist

def sumar(tup1, tup2):
    """
    adds two tuples
    """
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = []
        self.reset()
        uplist = [(0,col) for col in range(self._grid_width)]
        rightlist = [(row,self._grid_width-1) for row in range(self._grid_height)]
        downlist = [(self._grid_height-1,col) for col in range(self._grid_width)]
        leftlist = [(row, 0) for row in range(self._grid_height)]
        self._dicto = {UP:uplist, RIGHT:rightlist, DOWN:downlist, LEFT:leftlist}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        stringo = '['
        stringo += ''.join(str(self._grid[0])) + '\n'
        for elem in self._grid[1:-1]:
            linea = str(elem)
            stringo += ' ' + ''.join(linea) + '\n'
        stringo += ' ' + ''.join(str(self._grid[-1])) + ']'
        return stringo

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        control = True
        if direction == 1 or direction == 2:
            rango1 = self._grid_width
            rango2 = self._grid_height
        if direction == 3 or direction == 4:
            rango1 = self._grid_height
            rango2 = self._grid_width
        inicial = self._dicto[direction]
        inc = OFFSETS[direction]
        for item in range(rango1):
            sec = [inicial[item]]
            tupla = inicial[item]
            for elem in range(rango2-1):
                tupla = sumar(tupla,inc)
                sec.append(tupla)
            lista = []
            for valor in sec:
                lista.append(self._grid[valor[0]][valor[1]])
            copia = lista[:] 
            lista = merge(lista)
            if control:
                if lista != copia:#ojo aqui!!!
                    control = False
            counter = 0
            for elem in lista:
                self._grid[sec[counter][0]][sec[counter][1]] = elem
                counter += 1
        if control == False:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        import random
        if random.random() < 0.9:
            tile = 2
        else:
            tile = 4
        counter = 0
        while True:
            counter += 1
            row = random.randrange(0, self._grid_height)
            col = random.randrange(0, self._grid_width)
            if self._grid[row][col] == 0:
                self._grid[row][col] = tile
                break
            if counter > 500:
                break

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        if row in range(self._grid_height) and col in range(self._grid_width):
            self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
