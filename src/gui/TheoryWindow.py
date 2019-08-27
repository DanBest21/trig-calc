import Tkinter as tk
import Menu as menu


class TheoryWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.configure(bg="white")

        # Theory definitions
        lbl_title = tk.Label(self, text="Tangent/Normal Calculator - Theory Definitions",
                                  font="Arial 14 bold underline", bg="white")
        lbl_title.grid(row=0, column=0, columnspan=2, padx=10, pady=(25, 15))

        lbl_difftitle = tk.Label(self, text="Differentiation", font="Arial 12 bold underline", bg="white")
        lbl_difftitle.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        lbl_diff = tk.Label(self,
                                 text="Differentiation is the method used to find the rate of change, which is known as the derivative, of a function, which is an expression, rule or law that \"defines a relationship between one variable (the independent variable) and another variable (the dependent variable)\".",
                                 font="Arial 12", bg="white", wraplength=800, justify=tk.LEFT)
        lbl_diff.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        lbl_tantitle = tk.Label(self, text="Tangent", font="Arial 12 bold underline", bg="white")
        lbl_tantitle.grid(row=3, column=0, columnspan=2, padx=10, pady=(10, 5), sticky=tk.W)

        lbl_tan_1 = tk.Label(self,
                                  text="The rate of change is denoted by y = f(x) and the most common rate of change between the variables is the gradient of a curve at a specific point, defined to be the gradient of the tangent to the curve at that point. This is something that this program will allow you to graphically represent.",
                                  font="Arial 12", bg="white", wraplength=500, justify=tk.LEFT)
        lbl_tan_1.grid(row=4, column=0, padx=(10, 5), pady=5, sticky=tk.W)

        lbl_tan_2 = tk.Label(self,
                                  text="An example of this can be seen in figure 1 below, which shows the tangent of the graph y = f(x) when x = a0, the graph has a height of f(a) and the gradient of the curve at point a, and therefore f(a) if f'(a), with f' simply being a method to denote the derived function.",
                                  font="Arial 12", bg="white", wraplength=500, justify=tk.LEFT)
        lbl_tan_2.grid(row=5, column=0, padx=(10, 5), pady=5, sticky=tk.W)

        lbl_tan_3 = tk.Label(self,
                                  text="Something to remember: the equation of a straight line that passes through a point, say x1y1 and has a gradient of m, is given by (y-y1)/(x-x1) which equals to m.",
                                  font="Arial 12", bg="white", wraplength=500, justify=tk.LEFT)
        lbl_tan_3.grid(row=6, rowspan=3, column=0, padx=(10, 5), pady=5, sticky=tk.W)

        # Create a PhotoImage object that contains a GIF file that is stored in the active directory of the application.
        figure_1 = tk.PhotoImage(file="../img/figure_1.gif")

        # Create a Label object to place the PhotoImage into.
        # This association must be explicitly made in a separate line in order to get around an issue with tk itself that causes it to not always appear otherwise.
        img_figure_1 = tk.Label(self, image=figure_1, bg="white")
        img_figure_1.image = figure_1
        img_figure_1.grid(row=4, rowspan=4, column=1, padx=(5, 10), pady=5, sticky=tk.S)

        lbl_figure_1 = tk.Label(self, text="Figure 1", font="Arial 10 italic", bg="white")
        lbl_figure_1.grid(row=8, column=1, padx=(5, 10), pady=5, sticky=tk.N)

        lbl_normtitle = tk.Label(self, text="Normal", font="Arial 12 bold underline", bg="white")
        lbl_normtitle.grid(row=9, column=0, columnspan=2, padx=10, pady=(10, 5), sticky=tk.W)

        lbl_norm = tk.Label(self,
                                 text="In mathematics, the term normal means at right angles to, in other words perpendicular to tangent. If we have a curve like the one shown in figure 1 above, then the normal will be at a right angle to the tangent of f'(a), an example of which can be seen in figure 2.",
                                 font="Arial 12", bg="white", wraplength=500, justify=tk.LEFT)
        lbl_norm.grid(row=10, rowspan=2, column=0, padx=(10, 5), pady=5, sticky=tk.NW)

        # Create a PhotoImage object that contains a GIF file that is stored in the active directory of the application.
        figure_2 = tk.PhotoImage(file="../img/figure_2.gif")

        # Create a Label object to place the PhotoImage into.
        # This association must be explicitly made in a separate line in order to get around an issue with tk itself that causes it to not always appear otherwise.
        img_figure_2 = tk.Label(self, image=figure_2, bg="white")
        img_figure_2.image = figure_2
        img_figure_2.grid(row=10, column=1, padx=(5, 10), pady=5, sticky=tk.S)

        lbl_figure_2 = tk.Label(self, text="Figure 2", font="Arial 10 italic", bg="white")
        lbl_figure_2.grid(row=11, column=1, padx=(5, 10), pady=5, sticky=tk.N)

        # Button that closes the theory window and returns to the main menu.
        btn_menu = tk.Button(self, text="Return to Main Menu", font="Arial 12 bold", bg="gray30",
                                  fg="white",
                                  width=30, command=lambda: self.return_to_menu())
        btn_menu.grid(row=12, column=0, columnspan=2, padx=25, pady=(15, 25))

    def return_to_menu(self):
        frame = menu.Menu(self.master)
        frame.pack()
        self.destroy()