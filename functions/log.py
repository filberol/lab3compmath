from functions.function import Function
import math


class LogFunc(Function):

    def value(self, x):
        return math.copysign(5 * math.log(abs(x) + 3), x)

    def get_splits(self):
        return [0]

    def pass_limits(self, x):
        return True

    def __str__(self):
        return "sign(x) * 5 * log(|x| + 3)"
