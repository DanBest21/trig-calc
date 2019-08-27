import abc
import math


def draw_tangent(graph, x, y, m):
    # Find the constant of the tangent by taking the gradient times the x-value away from the y-value
    c = y - (m * math.radians(x))

    if (graph != ""):
        # TODO: Add graph function.
        pass

    if (c >= 0):
        return "y = " + str("{0:.2f}".format(m)) + "x + " + str("{0:.2f}".format(c))
    else:
        return "y = " + str("{0:.2f}".format(m)) + "x - " + str("{0:.2f}".format(c))[1:]

def draw_normal(graph, x, y, m):
    # Scale the line by multiplying it by 720 pi (length of the x-axis)
    m_line = m * 720 * math.pi

    # Find the constant of the tangent by taking the gradient times the x-value away from the y-value.
    c = y - (m * math.radians(x))

    # Find the constant for the graphical display of the line.
    c_line = y - (m_line * math.radians(x))

    if (graph != ""):
        # TODO: Add graph function.
        pass

    if (c >= 0):
        return "y = " + str("{0:.2f}".format(m)) + "x + " + str("{0:.2f}".format(c))
    else:
        return "y = " + str("{0:.2f}".format(m)) + "x - " + str("{0:.2f}".format(c))[1:]

class Calc():

    def __init__(self):
        pass

    @abc.abstractmethod
    def calculate_tangent(self, graph, x, amp, freq, phase):
        pass

    @abc.abstractmethod
    def calculate_normal(self, graph, x, amp, freq, phase):
        pass

