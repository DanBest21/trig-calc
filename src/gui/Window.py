from tkinter import Tk
from gui.GraphView import GraphView
from gui.HelpFrame import HelpWindow
from gui.Menu import Menu
from gui.TheoryFrame import TheoryWindow


class Window(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.resizable(False, False)
        self.title("Tangent/Normal Calculator")
        frame = Menu(self)
        frame.pack()
        self.mainloop()

    def navigate_to_menu(self):
        self.clear_window()
        frame = Menu(self)
        frame.pack()

    def navigate_to_sine_view(self):
        self.clear_window()
        frame = GraphView(self, "Sine")
        self.title("Tangent/Normal Calculator - Sine Graph")
        frame.pack()

    def navigate_to_cosine_view(self):
        self.clear_window()
        frame = GraphView(self, "Cosine")
        self.title("Tangent/Normal Calculator - Cosine Graph")
        frame.pack()

    def navigate_to_tangent_view(self):
        self.clear_window()
        frame = GraphView(self, "Tangent")
        self.title("Tangent/Normal Calculator - Tangent Graph")
        frame.pack()

    def navigate_to_theory_frame(self):
        self.clear_window()
        frame = TheoryWindow(self)
        self.title("Tangent/Normal Calculator - Theory Definitions")
        frame.pack()

    def navigate_to_help_frame(self, func):
        self.clear_window()
        frame = HelpWindow(self, func)
        self.title("Tangent/Normal Calculator - Help")
        frame.pack()

    def clear_window(self):
        for frame in self.winfo_children():
            frame.destroy()

    def close_app(self):
        self.destroy()
