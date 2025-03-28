class Rover:
    _x = 0
    _y = 0
    _direction = 0

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def forward(self, dist):
        if abs(self._direction) == 0:
            self._y += dist

        if abs(self._direction) == 90:
            self._x += dist

        if abs(self._direction) == 180:
            self._y -= dist

        if abs(self._direction) == 270:
            self._x -= dist

    def backward(self, dist):
        self.forward(-dist)

    def rotate(self, direction):
        if direction == 'r':
            self._direction += 90
            if abs(self._direction) == 360:
                self._direction = 0

        if direction == 'l':
            self._direction -= 90
            if self._direction < 0:
                self._direction = 360 - 90

    def locate(self):
        return self._x, self._y
