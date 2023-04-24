from integrator.integrator import FunctionIntegration
from integrator.time_manager import time_count
import copy


class TrapezoidMethod(FunctionIntegration):
    __epsilon = 0.0000001

    def solve(self, function, borders, segments, epsilon=__epsilon):
        edges = sorted(copy.deepcopy(borders))[:2]
        length = edges[1] - edges[0]
        # Won't work with fewer than 3 segments
        if segments < 3:
            raise ValueError
        # Check limits for function
        if not function.pass_limits(edges[0]) and function.pass_limits(edges[1]):
            raise ValueError
        splits = function.get_splits()
        # Check if function have splits on interval
        if edges[0] < any(splits) < edges[1]:
            le = edges[0]
            mi = splits[0]
            ri = edges[1]
            # Split integral and segments into to proportional parts
            return self.solve(function, [le, mi], int(segments * (mi - le) / length)) + \
                self.solve(function, [mi, ri], int(segments * (ri - mi) / length))

        # Integration
        summ = 0
        seg_l = (edges[1] - edges[0]) / segments
        le_ind = edges[0] + seg_l
        while le_ind < edges[1] - seg_l:
            ri = le_ind + seg_l
            summ += (function.value(ri) + function.value(le_ind)) / 2 * seg_l
            le_ind += seg_l
        # After dividing splits can only be on edges, appending manually
        # Left border
        if edges[0] in splits:
            eps_left = edges[0] + epsilon
            rig_first = edges[0] + seg_l
            summ += (function.value(rig_first) + function.value(eps_left)) / 2 * seg_l
        else:
            summ += (function.value(edges[0] + seg_l) + function.value(edges[0])) / 2 * seg_l
        # Right border
        if edges[1] in splits:
            eps_right = edges[1] - epsilon
            lef_last = edges[1] - seg_l
            summ += (function.value(eps_right) + function.value(lef_last)) / 2 * seg_l
        else:
            summ += (function.value(edges[1]) + function.value(edges[1] - seg_l)) / 2 * seg_l

        return summ

    def __str__(self):
        return "Trapezoid method"
