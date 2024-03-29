from abc import ABCMeta, abstractmethod
import math
import tkinter.messagebox as message


# Abstract class that contains both common functions for the calculator, and abstract methods that are implemented by its children classes.
class Calc:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def calculate_tangent(self, graph, x, amp, freq, phase):
        pass

    @abstractmethod
    def calculate_normal(self, graph, x, amp, freq, phase):
        pass

    @abstractmethod
    def draw_graph(self, graph, amp, freq, phase):
        pass

    @abstractmethod
    def update_equation_label(self, dyn, amp, freq, phase):
        pass

    def update_xvalue_label(self, x):
        return str("{0:.5f}".format(math.radians(x)))

    # Enhanced function for float() which handles any exceptions that may occur when converting a variable to a float
    # outputting the said error to an tkMessageBox error pop-up
    def convert_to_float(self, variable):
        try:
            return float(variable)
        except Exception as ex:
            message.showerror("Tangent/Normal Calculator", "Error - " + str(ex))

    # Supplemental function that acts as an input mask to any value in the x value or phase angle text fields to
    # ensure they are numerical and therefore valid.
    def validate_number(self, modificationType, newValue, completeValue):
        if (modificationType == "1") and (newValue in "0123456789."):
            try:
                self.convert_to_float(completeValue)
                return True
            except Exception:
                return False
        elif (modificationType != "1"):
            return True
        else:
            return False

    def draw_line(self, graph, x, y, prev_x, prev_y):
        if (x != 0):
            graph.create_line(prev_x + 40, 200 - prev_y, x + 40, 200 - y, fill="black")

    def draw_tangent(self, graph, x, y, m):
        # Find the constant of the tangent by taking the gradient times the x-value away from the y-value
        c = y - (m * math.radians(x))

        if (graph != ""):
            # Get the y values at 0 and 720 radians.
            y1 = (m * math.radians(0)) + c
            y2 = (m * math.radians(720)) + c

            graph.create_line(40, 200 - y1, 760, 200 - y2, fill="red")

        if (c >= 0):
            return "y = " + str("{0:.2f}".format(m)) + "x + " + str("{0:.2f}".format(c))
        else:
            return "y = " + str("{0:.2f}".format(m)) + "x - " + str("{0:.2f}".format(c))[1:]

    def draw_normal(self, graph, x, y, m):
        # If this isn't already a vertical line:
        if (m > -1 / 0.00000001):
            # Scale the gradient up by multiplying it by 720 pi (length of the x-axis)
            m_line = m * 720 * math.pi
        else:
            m_line = m

        # Find the constant of the tangent by taking the gradient times the x-value away from the y-value.
        c = y - (m * math.radians(x))

        # Find the constant of the tangent by taking the gradient times the x-value away from the y-value.
        c_line = y - (m_line * math.radians(x))

        if (graph != ""):
            # Get the y values at 0 and 720 radians.
            y1 = (m_line * math.radians(0)) + c_line
            y2 = (m_line * math.radians(720)) + c_line

            graph.create_line(40, 200 - y1, 760, 200 - y2, fill="blue")

        if (c >= 0) and (c_line >= 0):
            return "y = " + str("{0:.2f}".format(m)) + "x + " + str("{0:.2f}".format(c)), "y = " + str("{0:.2f}".format(m_line)) + "x + " + str("{0:.2f}".format(c_line))
        elif (c >= 0) and (c_line < 0):
            return "y = " + str("{0:.2f}".format(m)) + "x + " + str("{0:.2f}".format(c)), "y = " + str("{0:.2f}".format(m_line)) + "x - " + str("{0:.2f}".format(c_line))[1:]
        elif (c < 0) and (c_line >= 0):
            return "y = " + str("{0:.2f}".format(m)) + "x - " + str("{0:.2f}".format(c))[1:], "y = " + str("{0:.2f}".format(m_line)) + "x + " + str("{0:.2f}".format(c_line))
        else:
            return "y = " + str("{0:.2f}".format(m)) + "x - " + str("{0:.2f}".format(c))[1:], "y = " + str("{0:.2f}".format(m_line)) + "x - " + str("{0:.2f}".format(c_line))[1:]

    # Function that draws the axis of the graph.
    def draw_axis(self, graph):
        # Creates the y-axis.
        graph.create_line(40, 10, 40, 390, fill="black")

        # Creates the x-axis.
        graph.create_line(40, 200, 790, 200, fill="black")

        # Y-axis labels
        graph.create_text(20, 10, font="Arial 10 bold", text="200")
        graph.create_text(20, 100, font="Arial 10 bold", text="100")
        graph.create_text(20, 200, font="Arial 10 bold", text="0")
        graph.create_text(20, 300, font="Arial 10 bold", text="-100")
        graph.create_text(20, 390, font="Arial 10 bold", text="-200")

        # X-axis labels
        graph.create_text(90 + 40, 210, font="Arial 10 bold", text="90")
        graph.create_text(180 + 40, 210, font="Arial 10 bold", text="180")
        graph.create_text(270 + 40, 210, font="Arial 10 bold", text="270")
        graph.create_text(360 + 40, 210, font="Arial 10 bold", text="360")
        graph.create_text(450 + 40, 210, font="Arial 10 bold", text="450")
        graph.create_text(540 + 40, 210, font="Arial 10 bold", text="540")
        graph.create_text(630 + 40, 210, font="Arial 10 bold", text="630")
        graph.create_text(720 + 40, 210, font="Arial 10 bold", text="720")
