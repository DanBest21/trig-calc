import program.Calc as super
import math


class CosCalc(super.Calc):
    def calculate_tangent(self, graph, x, amp, freq, phase):
        # Find y, which is found through the equation: "A cos(fx + theta)"
        y = amp * math.cos(math.radians((float(freq) * x) + phase))

        # Find m, the gradient, which is found through the equation: "-fA sin(fx + theta)", i.e. dy/dx
        # If m is zero, then set it to a gradient that will create a straight horizontal line.
        if (-amp * freq * math.sin(math.radians((float(freq) * x) + phase)) < 0.000001) and (
                -amp * freq * math.sin(math.radians((float(freq) * x) + phase)) > -0.000001):
            m = 0
        else:
            m = -amp * freq * math.sin(math.radians((float(freq) * x) + phase))

        return super.draw_tangent(graph, x, y, m)

    def calculate_normal(self, graph, x, amp, freq, phase):
        # Find y, which is found through the equation: "A cos(fx + theta)"
        y = amp * math.cos(math.radians((float(freq) * x) + phase))

        # Find m, the gradient, which is found through the equation: "-1/-fA sin(fx + theta)", i.e. -1 over dy/dx
        # If m is zero, then set it to a gradient that will essentially create a straight vertical line.
        if (-amp * freq * math.sin(math.radians((float(freq) * x) + phase)) < 0.000001) and (
                -amp * freq * math.sin(math.radians((float(freq) * x) + phase)) > -0.000001):
            m = -1 / 0.0001
        else:
            m = -1 / (-amp * freq * math.sin(math.radians((float(freq) * x) + phase)))

        return super.draw_normal(graph, x, y, m)