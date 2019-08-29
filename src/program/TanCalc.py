import math
import Calc as calc


class TanCalc(calc.Calc):
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

        return super(TanCalc, self).draw_tangent(graph, x, y, m)

    def calculate_normal(self, graph, x, amp, freq, phase):
        # Find y, which is found through the equation: "A tan(fx + theta)"
        y = amp * math.tan(math.radians((float(freq) * x) + phase))

        # Find m, the gradient, which is found through the equation: "-1 * fA sec^2(fx + theta)" or "fA 1/cos^2(fx + theta)", i.e. -1 times dy/dx
        # If m is zero, then set it to a gradient that will essentially create a straight vertical line.
        if (amp * freq * (1 / (math.cos(math.radians((float(freq) * x) + phase)) ** 2)) < 0.000001) and (
                amp * freq * (1 / (math.cos(math.radians((float(freq) * x) + phase)) ** 2)) > -0.000001):
            m = -1 / 0.00000001
        else:
            m = -1 * (amp * freq * (1 / (math.cos(math.radians((float(freq) * x) + phase)) ** 2)))

        return super(TanCalc, self).draw_normal(graph, x, y, m)

    def draw_graph(self, graph, amplitude, frequency, phase):
        prev_x = 0
        prev_y = 0

        for x in range(720 + 1):
            y = amplitude * math.tan(math.radians((float(frequency) * x) + phase))

            # Check that the absolute value between y and prev_y is smaller than the frequency times the amplitude, in order to get rid of arbritrary lines between the tangent curves.
            if (abs(y - prev_y) < (frequency * amplitude)):
                super(TanCalc, self).draw_line(graph, x, y, prev_x, prev_y)

            prev_x = x
            prev_y = y

    def update_equation_label(self, dyn, amp, freq, phase):
        dyn.config(text="y = " + amp + "tan(" + freq + "x + " + phase + ")")