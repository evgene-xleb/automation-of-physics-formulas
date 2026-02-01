class PhysicsFormuls:
    def __init__(self, S=0, t=0, V=0):
        self._S = S
        self._t = t
        self._V = V


class Mechanics(PhysicsFormuls):
    def __init__(self, S=0.0, t=0.0, V=0.0):
        super().__init__(S, t, V)

    def __str__(self):
        return f"Это формулы по физике на тему Механика:\nS(расстояние) = {self._S}км\nt(время) = {self._t}ч\nV(скорость) = {self._V}км/ч"

    def speed(self):
        if 0 != self._t != 0.0:
            return self._S / self._t
        else:
            raise ZeroDivisionError("На ноль делить нельзя!")

    def get_speed(self):
        return f"V(скорость) = {self.speed()}км/ч, при данных: S(расcтояние) = {self._S}км, t(время) = {self._t}ч"

    def distance(self):
        if 0 != self._t != 0.0:
            return self._V * self._t
        else:
            raise ZeroDivisionError("На ноль делить нельзя!")

    def get_distance(self):
        return f"S(расcтояние) = {self.distance()}км, при данных: V(скорость) = {self._V}км/ч, t(время) = {self._t}ч"

    def time(self):
        if 0 != self._V != 0.0:
            return self._S / self._V
        else:
            raise ZeroDivisionError("На ноль делить нельзя!")

    def get_time(self):
        return f"t(время) = {self.time()}ч, при данных: S(расcтояние) = {self._S}км, V(скорость) = {self._V}км/ч"

    def set_time(self, new_time):
        if isinstance(new_time, (int, float)) and new_time >= 0:
            self._t = new_time
        else:
            raise TypeError("Не правильный тип данных !")

    def set_speed(self, new_speed):
        if isinstance(new_speed, (int, float)) and new_speed >= 0:
            self._V = new_speed
        else:
            raise TypeError("Не правильный тип данных !")

    def set_distance(self, new_distance):
        if isinstance(new_distance, (int, float)) and new_distance >= 0:
            self._S = new_distance
        else:
            raise TypeError("Не правильный тип данных !")


def open_file():
    with open("formulas_file.txt", "w", encoding="utf-8") as file:
        file.readlines()


S = Mechanics(t=40, V=32)

print(S)
task = S.get_distance()

print(task)
