from math import pi, sin, cos


class LangtonsAnt:
    _state = []
    _ant = {
        'orientation': 90,
        'current_position': None
    }

    def __init__(self, initial_state, start_position):
        self._state = initial_state
        self._ant['current_position'] = start_position

    @property
    def state(self):
        return self._state

    def next(self):

        self.turn_ant(self._state[self._ant['current_position'][0]][self._ant['current_position'][1]])

        next_position = self.get_ant_next_position(self._ant['current_position'], self._ant['orientation'])

        self.flip_cell(self._ant['current_position'][0], self._ant['current_position'][1])

        self.move_ant(next_position)

    def flip_cell(self, cell_y, cell_x):
        self._state[cell_y][cell_x] = not self._state[cell_y][cell_x]

    def turn_ant(self, cell_value):
        rotation_direction = 90 if cell_value else -90

        self._ant['orientation'] = (self._ant['orientation'] + rotation_direction) % 360

    def move_ant(self, next_position):
        self._ant['current_position'] = next_position

    def get_ant_next_position(self, current_location, orientation):

        next_y = current_location[0] - int(sin(2*pi*(orientation / 360)))
        next_y = (len(self._state) + next_y) % len(self._state)

        next_x = current_location[1] + int(cos(2*pi*(orientation / 360)))
        next_x = (len(self._state[0]) + next_x) % len(self._state[0])

        return next_y, next_x
