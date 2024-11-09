class Hourse:
    """Класс описывающий лошадь."""

    def __init__(self, x_distance = 0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    """Класс описывающий орла."""

    def __init__(self, y_distance = 0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Hourse, Eagle):
    """Наследник двух классов."""

    def __init__(self):
        Hourse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.fly(dy)
        self.run(dx)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
