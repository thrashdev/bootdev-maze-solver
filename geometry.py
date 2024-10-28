from tkinter import Canvas

WALL_COLOR = "black"
WALL_NOT_EXIST_COLOR = "white"

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1:Point, p2:Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas:Canvas, fill_color:str):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Cell():
    def __init__(self, x1, y1, x2, y2, win=None) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__win = win
        self.__centre = Point((x2+x1) / 2, (y2+y1) / 2)
        self.visited = False

    def draw(self):
        if self.__win is None:
            return
        top_left = Point(self.__x1, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        top_right = Point(self.__x2, self.__y1)
        bottom_right = Point(self.__x2, self.__y2)
        top_right = Point(self.__x2, self.__y1)
        left_wall = Line(top_left, bottom_left)
        right_wall = Line(top_right, bottom_right)
        top_wall = Line(top_left, top_right)
        bottom_wall = Line(bottom_left, bottom_right)
        if self.has_left_wall:
            self.__win.draw_line(left_wall, WALL_COLOR)
        else:
            self.__win.draw_line(left_wall, WALL_NOT_EXIST_COLOR)

        if self.has_right_wall:
            self.__win.draw_line(right_wall, WALL_COLOR)
        else:
            self.__win.draw_line(right_wall, WALL_NOT_EXIST_COLOR)

        if self.has_top_wall:
            self.__win.draw_line(top_wall, WALL_COLOR)
        else:
            self.__win.draw_line(top_wall, WALL_NOT_EXIST_COLOR)

        if self.has_bottom_wall:
            self.__win.draw_line(bottom_wall, WALL_COLOR)
        else:
            self.__win.draw_line(bottom_wall, WALL_NOT_EXIST_COLOR)

    def draw_move(self, to_cell, undo=False):
        color = "gray"
        if undo:
            color = "red"
        l = Line(self.__centre, to_cell.__centre)
        self.__win.draw_line(l, color)

    def break_wall(self, direction):
        match direction:
            case "up":
                self.has_top_wall = False
            case "bottom":
                self.has_bottom_wall = False
            case "left":
                self.has_left_wall = False
            case "right":
                self.has_right_wall = False

        # self.draw()

