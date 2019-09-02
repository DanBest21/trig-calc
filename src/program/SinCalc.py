import math
from program.Calc import Calc


# Implementation of the Calc class for the Sine function.
class SinCalc(Calc):
    def calculate_tangent(self, graph, x, amp, freq, phase):
        # Find y, which is found through the equation: "A sin(fx + theta)"
        y = amp * math.sin(math.radians((float(freq) * x) + phase))

        # Find m, the gradient, which is found through the equation: "fA cos(fx + theta)", i.e. dy/dx
        # If m is zero, then set it to a gradient that will create a straight horizontal line.
        if (amp * freq * math.cos(math.radians((float(freq) * x) + phase)) < 0.000001) and (
                amp * freq * math.cos(math.radians((float(freq) * x) + phase)) > -0.000001):
            m = 0
        else:
            m = amp * freq * math.cos(math.radians((float(freq) * x) + phase))

        return super(SinCalc, self).draw_tangent(graph, x, y, m)

    def calculate_normal(self, graph, x, amp, freq, phase):
        # Find y, which is found through the equation: "A sin(fx + theta)"
        y = amp * math.sin(math.radians((float(freq) * x) + phase))

        # Find m, the gradient, which is found through the equation: "-1 / fA cos(fx + theta)", i.e. -1 over dy/dx
        # If m is zero, then set it to a gradient that will essentially create a straight vertical line.
        if (amp * freq * math.cos(math.radians((float(freq) * x) + phase)) < 0.000001) and (
                amp * freq * math.cos(math.radians((float(freq) * x) + phase)) > -0.000001):
            m = -1 / 0.00000001
        else:
            m = -1 / (amp * freq * math.cos(math.radians((float(freq) * x) + phase)))

        return super(SinCalc, self).draw_normal(graph, x, y, m)

    def draw_graph(self, graph, amp, freq, phase):
        prev_x = 0
        prev_y = 0

        for x in range(720 + 1):
            y = amp * math.sin(math.radians((float(freq) * x) + phase))

            super(SinCalc, self).draw_line(graph, x, y, prev_x, prev_y)

            prev_x = x
            prev_y = y

    def update_equation_label(self, dyn, amp, freq, phase):
        dyn.config(text="y = " + amp + "sin(" + freq + "x + " + phase + ")")