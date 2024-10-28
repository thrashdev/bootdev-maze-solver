from geometry import Point, Cell
from time import sleep
import random


class Maze():
    def __init__(self,
                 x1, y1,
                 num_rows, num_cols,
                 cell_size_x, cell_size_y,
                 win=None,
                 seed=None
                 ):
        self.__x1 = x1
        self.__y1 = y1
        self._cells = []
        self._num_rows = num_rows
        self._num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        matrix = []
        col = []
        for c in range(self._num_cols):
            col = []
            y1 = self.__y1 + self.cell_size_y * c
            for r in range(self._num_rows):
                x1 = self.__x1 + self.cell_size_x * r
                col.append(Cell(x1, y1, x1+self.cell_size_x, y1+self.cell_size_y, self.__win))

            if col != []:
                matrix.append(col) 
    
        self._cells = matrix

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self.__win is None:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        if len(self._cells) == 0:
            return

        last_row = self._num_rows-1
        last_col = self._num_cols-1

        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[last_col][last_row].has_bottom_wall = False
        self._draw_cell(last_col, last_row)

    def _break_walls_r(self, i, j):

        opp_direction = {
                        "up":"bottom",
                        "bottom":"up",
                        "left":"right",
                        "right":"left",
                         }
        self._cells[i][j].visited = True
        while True:
            adjacent = []
            if i-1 in range(1, self._num_cols):
                adjacent.append([self._cells[i-1][j], "up" , (i-1, j)]) #up
            if j-1 in range(1, self._num_rows):
                adjacent.append([self._cells[i][j-1], "left", (i, j-1)]) #left
            if i+1 in range(1, self._num_cols):
                adjacent.append([self._cells[i+1][j], "bottom", (i+1, j)]) #down
            if j+1 in range(1, self._num_rows):
                adjacent.append([self._cells[i][j+1], "right", (i, j+1)]) #right

            to_visit = list(filter(lambda x: x[0].visited != True, adjacent))
            if len(to_visit) == 0:
                self._cells[i][j].draw()
                return
            
            rand_dir = random.randrange(0, len(to_visit))
            direction = to_visit[rand_dir][1]
            self._cells[i][j].break_wall(direction)
            to_visit[rand_dir][0].break_wall(opp_direction[direction])
            self._break_walls_r(to_visit[rand_dir][2][0], to_visit[rand_dir][2][1])


    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        current = self._cells[i][j]
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True

        adjacent = []
        if i-1 in range(1, self._num_cols):
            adjacent.append([self._cells[i-1][j], "up" , (i-1, j)]) #up
        if j-1 in range(1, self._num_rows):
            adjacent.append([self._cells[i][j-1], "left", (i, j-1)]) #left
        if i+1 in range(1, self._num_cols):
            adjacent.append([self._cells[i+1][j], "bottom", (i+1, j)]) #down
        if j+1 in range(1, self._num_rows):
            adjacent.append([self._cells[i][j+1], "right", (i, j+1)]) #right
    
        not_visited = filter(lambda x: x[0].visited != True, adjacent)
        for nv in not_visited:
            match nv[1]:
                case "up":
                    if current.has_top_wall == True or nv[0].has_bottom_wall == True:
                        continue
                case "bottom":
                    if current.has_bottom_wall == True or nv[0].has_top_wall == True:
                        continue
                case "left":
                    if current.has_left_wall == True or nv[0].has_right_wall == True:
                        continue
                case "right":
                    if current.has_right_wall == True or nv[0].has_left_wall == True:
                        continue

            current.draw_move(nv[0])
            res = self._solve_r(nv[2][0], nv[2][1])

            if res:
                return True
            
            if not res:
                current.draw_move(nv[0], undo=True)

        return False
        
