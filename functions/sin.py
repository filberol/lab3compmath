from functions.function import Function
import math


class SinFunc(Function):

    def value(self, x):
        return 10 * math.sin(x) / x - 1.8

    def get_splits(self):
        return [0]

    def pass_limits(self, x):
        return True

    def __str__(self):
        return "10 * sin(x) / x - 1.8"
