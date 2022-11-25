from collections.abc import Sequence


class Binary:
    def __init__(self, value=0):
        if isinstance(value, Sequence):
            if len(value) > 2 and value[0:2] == "0b":
                self._value = int(value, base=2)
            elif len(value) > 2 and value[0:2] == "0x":
                self._value = int(value, base=16)
            else:
                self._value = int("".join([str(i) for i in value]), base=2)
        else:
            try:
                self._value = int(value)
                if self._value < 0:
                    raise ValueError("Binary cannot accept negative numbers")
            except ValueError:
                raise ValueError(f"Cannot convert value {value} to Binary")

    def __int__(self):
        return self._value

    def __index__(self):
        return self.__int__()

    def __str__(self):
        return bin(self)[2:]

    def __eq__(self, other):
        return int(self) == int(other)

    def __and__(self, other):
        return Binary(self._value & Binary(other)._value)

    def __or__(self, other):
        return Binary(self._value | Binary(other)._value)

    def __xor__(self, other):
        return Binary(self._value ^ Binary(other)._value)

    def __lshift__(self, pos):
        return Binary(self._value << pos)

    def __rshift__(self, pos):
        return Binary(self._value >> pos)

    def __add__(self, other):
        return Binary(self._value + Binary(other)._value)

    def __sub__(self, other):
        return Binary(self._value - Binary(other)._value)

    def __mul__(self, other):
        return Binary(self._value * Binary(other)._value)

    def __truediv__(self, other):
        return Binary(int(self._value / Binary(other)._value))

    def __invert__(self):
        return Binary([abs(int(i) - 1) for i in str(self)])

    def __getitem__(self, item):
        return str(self)[-(item + 1)]
