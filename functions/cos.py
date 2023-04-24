from functions.function import Function
import math


class CosFunc(Function):

    def value(self, x):
        return 5 * math.cos(x) / x

    def get_splits(self):
        return [0]

    def pass_limits(self, x):
        return True

    def __str__(self):
        return "5 * cos(x) / x"
