from functions.function import Function
import math


class SqrtFunc(Function):

    def value(self, x):
        return math.sqrt(x)

    def get_splits(self):
        return []

    def pass_limits(self, x):
        return True if x >= 0 else False

    def __str__(self):
        return "sqrt(x)"
