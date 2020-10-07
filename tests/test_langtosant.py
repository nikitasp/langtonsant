import unittest
from src.LangtonsAnt import LangtonsAnt


class MyTestCase(unittest.TestCase):
    def test_langtonsant_state(self):
        initial_state = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
        ]
        start_position = (2, 2)
        game = LangtonsAnt(initial_state, start_position)

        for _ in range(8):
            game.next()

        self.assertListEqual(game.state, [
            [False, False, False, False, False],
            [False, True,  True,  False, False],
            [False, True,  False, True,  False],
            [False, False, True,  True,  False],
            [False, False, False, False, False],
        ])


if __name__ == '__main__':
    unittest.main()
