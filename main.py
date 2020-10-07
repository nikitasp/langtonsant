from src.LangtonsAnt import LangtonsAnt


def print_game_state(state):
    state_str = ''
    for line in state:
        state_str += ''.join(['x' if c else 'o' for c in line]) + '\n'

    print(state_str)


if __name__ == '__main__':
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
        print_game_state(game.state)

    print(game.state)

