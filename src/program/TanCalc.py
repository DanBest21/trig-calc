import program.Calc as super
import math


class TanCalc(super.Calc):
    def calculate_tangent(self, graph, x, amp, freq, phase):
        # Find y, which is found through the equation: "A tan(fx + theta)"
        y = amp * math.tan(math.radians((float(freq) * x) + phase))

        # Find m, the gradient, which is found through the equation: "fA sec^2(fx + theta)" or "fA 1/cos^2(fx + theta)", i.e. dy/dx
        # If m is zero, then set it to a gradient that will create a straight horizontal line.
        if (amp * freq * (1 / (math.cos(math.radians((float(freq) * x) + phase)) ** 2)) < 0.000001) and (
                amp * freq * (1 / (math.cos(math.radians((float(freq) * x) + phase)) ** 2)) > -0.000001):
            m = 0
        else:
            m = amp * freq * (1 / (math.cos(math.radians((float(freq) * x) + phase)) ** 2))

        return super.draw_tangent(graph, x, y, m)


    def calculate_normal(self, graph, x, amp, freq, phase):
        # Find y, which is found through the equation: "A tan(fx + theta)"
        y = amp * math.tan(math.radians((float(freq) * x) + phase))

        # Find m, the gradient, which is found through the equation: "-1/fA sec^2(fx + theta)" or "fA 1/cos^2(fx + theta)", i.e. -1 over dy/dx
        # If m is zero, then set it to a gradient that will essentially create a straight vertical line.
        if (amp * freq * (1 / (math.cos(math.radians((float(freq) * x) + phase)) ** 2)) < 0.000001) and (
                amp * freq * (1 / (math.cos(math.radians((float(freq) * x) + phase)) ** 2)) > -0.000001):
            m = -1 / 0.0001
        else:
            m = -1 / (amp * freq * (1 / (math.cos(math.radians((float(freq) * x) + phase)) ** 2)))

        return super.draw_normal(graph, x, y, m)