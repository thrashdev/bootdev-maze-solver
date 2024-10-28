from geometry import Cell, Line, Point
from window import Window
from maze import Maze



def main():
    screen_x = 800
    screen_y = 600
    margin = 50
    num_rows = 12
    num_cols = 16
    cell_size_x = (screen_x - 2*margin) / num_cols
    cell_size_y = (screen_y - 2*margin) / num_rows
    win = Window(screen_x, screen_y)
    maze = Maze(margin,margin,num_rows,num_cols,cell_size_x,cell_size_y,win, seed=0)   
    maze.solve()
    win.wait_for_close()


if __name__ == '__main__':
    main()
