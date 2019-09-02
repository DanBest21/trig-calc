import tkinter as tk
import tkinter.messagebox as message


# A subclass of the tkinter.Frame class that provides assistance and information to the user about the graph view.
class HelpWindow(tk.Frame):
    def __init__(self, parent, func, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.configure(bg="white")

        # Help information
        lbl_title = tk.Label(self, text="Tangent/Normal Calculator - Help", font="Arial 14 bold underline",
                             bg="white")
        lbl_title.grid(row=0, column=0, columnspan=2, padx=10, pady=(25, 15))

        lbl_xvalue = tk.Label(self, text="X Value:", font="Arial 12 bold", bg="white")
        lbl_xvalue.grid(row=1, column=0, padx=(10, 5), pady=5, sticky=tk.W)

        txt_xvalue = tk.Label(self,
                              text="Determines the value on the x-axis from which the tangent and normal lines are "
                                   "derived from. The \"-\" button can be used to turn this value negative. As this "
                                   "value is converted into radians to align with how the graph itself is drawn, "
                                   "the \"X Value in Radians\" field outputs this value in radians to show what value "
                                   "is being used to create the tangent and normal equations. This value must be a "
                                   "number.",
                              font="Arial 12", bg="white", wraplength=800, justify=tk.LEFT)
        txt_xvalue.grid(row=1, column=1, padx=(5, 10), pady=5, sticky=tk.W)

        lbl_phase = tk.Label(self, text="Phase Angle:", font="Arial 12 bold", bg="white")
        lbl_phase.grid(row=2, column=0, padx=(10, 5), pady=5, sticky=tk.W)

        txt_phase = tk.Label(self,
                             text="Determines how much out of phase the sine/cosine/tangent function is from if it "
                                  "were in phase with an angle of 0 degrees. The \"-\" button can be used to turn "
                                  "this value negative. This value must be a number.",
                             font="Arial 12", bg="white", wraplength=800, justify=tk.LEFT)
        txt_phase.grid(row=2, column=1, padx=(5, 10), pady=5, sticky=tk.W)

        lbl_tangent = tk.Label(self, text="Show Tangent:", font="Arial 12 bold", bg="white")
        lbl_tangent.grid(row=3, column=0, padx=(10, 5), pady=5, sticky=tk.W)

        txt_tangent = tk.Label(self, text="Calculates and displays the tangent line if checked.",
                               font="Arial 12", bg="white", wraplength=800, justify=tk.LEFT)
        txt_tangent.grid(row=3, column=1, padx=(5, 10), pady=5, sticky=tk.W)

        lbl_normal = tk.Label(self, text="Show Normal:", font="Arial 12 bold", bg="white")
        lbl_normal.grid(row=4, column=0, padx=(10, 5), pady=5, sticky=tk.W)

        txt_normal = tk.Label(self, text="Calculates and displays the normal line if checked. To ensure that the line "
                                         "is displayed appropriately on the application, it is scaled by multiplying "
                                         "the derived gradient by 720 pi (the length of the x-axis). Both of these "
                                         "equations are displayed when the normal line is switched on.",
                              font="Arial 12",
                              bg="white", wraplength=800, justify=tk.LEFT)
        txt_normal.grid(row=4, column=1, padx=(5, 10), pady=5, sticky=tk.W)

        lbl_apply = tk.Label(self, text="Apply Changes:", font="Arial 12 bold", bg="white")
        lbl_apply.grid(row=5, column=0, padx=(10, 5), pady=5, sticky=tk.W)

        txt_apply = tk.Label(self,
                             text="Applies any changes that have been made to the graph and equations since the last "
                                  "time the button was pressed or the window was initialised.",
                             font="Arial 12", bg="white", wraplength=800, justify=tk.LEFT)
        txt_apply.grid(row=5, column=1, padx=(5, 10), pady=5, sticky=tk.W)

        lbl_menu = tk.Label(self, text="Return to Main Menu:", font="Arial 12 bold", bg="white")
        lbl_menu.grid(row=6, column=0, padx=(10, 5), pady=5, sticky=tk.W)

        txt_menu = tk.Label(self,
                            text="Closes the current window and re-opens the initial main menu screen from where the "
                                 "sine/cosine or tangent menu can be selected",
                            font="Arial 12", bg="white", wraplength=800, justify=tk.LEFT)
        txt_menu.grid(row=6, column=1, padx=(5, 10), pady=5, sticky=tk.W)

        lbl_amplitude = tk.Label(self, text="Amplitude:", font="Arial 12 bold", bg="white")
        lbl_amplitude.grid(row=7, column=0, padx=(10, 5), pady=5, sticky=tk.W)

        txt_amplitude = tk.Label(self,
                                 text="Determines how much the result of the sine, cosine or tangent function is "
                                      "multiplied by. Increasing this value will cause the wave to appear higher.",
                                 font="Arial 12", bg="white", wraplength=800, justify=tk.LEFT)
        txt_amplitude.grid(row=7, column=1, padx=(5, 10), pady=5, sticky=tk.W)

        lbl_frequency = tk.Label(self, text="Frequency:", font="Arial 12 bold", bg="white")
        lbl_frequency.grid(row=8, column=0, padx=(10, 5), pady=5, sticky=tk.W)

        txt_frequency = tk.Label(self,
                                 text="Determines how much the x value of each point is multiplied by within the "
                                      "sine, cosine or tangent function. Increasing this value will cause the wave to "
                                      "appear more frequently.",
                                 font="Arial 12", bg="white", wraplength=800, justify=tk.LEFT)
        txt_frequency.grid(row=8, column=1, padx=(5, 10), pady=5, sticky=tk.W)

        # Button that closes the help window.
        btn_menu = tk.Button(self, text="Close Help", font="Arial 12 bold", bg="gray30", fg="white",
                             width=30,
                             command=lambda: self.navigate_to_graph(func))
        btn_menu.grid(row=9, column=0, columnspan=2, padx=25, pady=(15, 25))

    def navigate_to_graph(self, func):
        try:
            if (func == "Sine"):
                self.master.navigate_to_sine_view()
            elif (func == "Cosine"):
                self.master.navigate_to_cosine_view()
            elif (func == "Tangent"):
                self.master.navigate_to_tangent_view()
            else:
                raise ValueError("Function '" + str(func) + "' is undefined.")
        except ValueError as ex:
            message.showerror("Tangent/Normal Calculator", "Error - " + str(ex))
