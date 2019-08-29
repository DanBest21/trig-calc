import tkinter as tk


class Menu(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.configure(bg="white")
        self.master.title("Tangent/Normal Calculator")

        lbl_title = tk.Label(self, text="Tangent/Normal Calculator", font="Arial 14 bold underline", bg="white")
        lbl_title.grid(row=0, column=0, padx=5, pady=10)

        # Button that opens the sine graph dialog.
        btn_sin = tk.Button(self, text="Sine Graph", font="Arial 12 bold", bg="gray30", fg="white", width=30,
                            command=lambda: self.master.navigate_to_sine_view())
        btn_sin.grid(row=1, column=0, padx=15, pady=5)

        # Button that opens the cosine graph dialog.
        btn_cos = tk.Button(self, text="Cosine Graph", font="Arial 12 bold", bg="gray30", fg="white", width=30,
                            command=lambda: self.master.navigate_to_cosine_view())
        btn_cos.grid(row=2, column=0, padx=15, pady=5)

        # Button that opens the tangent graph dialog.
        btn_tan = tk.Button(self, text="Tangent Graph", font="Arial 12 bold", bg="gray30", fg="white", width=30,
                            command=lambda: self.master.navigate_to_tangent_view())
        btn_tan.grid(row=3, column=0, padx=15, pady=5)

        # Button that opens the theory explanation window by calling the "createTheoryWindow()" function.
        btn_theory = tk.Button(self, text="Theory Definitions", font="Arial 12 bold", bg="gray30", fg="white", width=30,
                               command=lambda: self.master.navigate_to_theory_frame())
        btn_theory.grid(row=4, column=0, padx=15, pady=5)

        # Button that closes the main menu window and therefore effectively exits the applicaiton.
        btn_exit = tk.Button(self, text="Exit Application", font="Arial 12 bold", bg="gray30", fg="white", width=30,
                             command=lambda: self.master.close_app())
        btn_exit.grid(row=5, column=0, padx=15, pady=(5, 20))