from geometry import Line, Point
from window import Window


def main():
    win = Window(800,600)
    l1 = Line(Point(100, 100), Point(200, 200))
    l2 = Line(Point(400, 200), Point(0, 100))
    win.draw_line(l1, "red")
    win.draw_line(l2, "blue")
    win.wait_for_close()


if __name__ == '__main__':
    main()
