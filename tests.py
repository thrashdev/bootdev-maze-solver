import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m1._cells),
                num_cols
        )
        self.assertEqual(
                len(m1._cells),
                num_cols
        )

    def test_set_unvisited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                self.assertFalse(m1._cells[i][j].visited)



if __name__ == '__main__':
    unittest.main()
