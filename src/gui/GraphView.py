import tkinter as tk
import tkinter.messagebox as message
from program.SinCalc import SinCalc
from program.CosCalc import CosCalc
from program.TanCalc import TanCalc


class GraphView(tk.Frame):
    def __init__(self, parent, func, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.configure(bg="white")

        self.xvalue_negative = False
        self.phase_negative = False

        try:
            self.configure_graph_function(func)
        except ValueError as ex:
            message.showerror("Tangent/Normal Calculator", "Error - " + str(ex))

        # Bind the validateNumber function to the self.master, so it can be associated to particular elements.
        vcmd = self.master.register(self.calc.validate_number)

        lbl_title = tk.Label(self, text="Tangent/Normal Calculator - " + func + " Graph",
                                  font="Arial 14 bold underline", bg="white")
        lbl_title.grid(row=0, column=0, columnspan=6, padx=5, pady=25)

        # Text field that allows the user to specify what point (x co-ordinate) on the graph that they want to base the tangent and normal from.
        lbl_xvalue = tk.Label(self, text="X Value:", font="Arial 12 bold", bg="white")
        lbl_xvalue.grid(row=1, column=0, padx=(25, 5), pady=(5, 0), sticky=tk.E)

        btn_neg_xvalue = tk.Button(self, text="-", font="Arial 12 bold", bg="gray30", fg="white", width=3,
                                        relief=tk.RAISED, command=lambda: self.set_negative(btn_neg_xvalue, "xvalue"))
        btn_neg_xvalue.grid(row=1, column=1, padx=(5, 0), pady=(5, 0), sticky=tk.E)

        txt_xvalue = tk.Entry(self, font="Arial 12", width=15, validate="key",
                                   validatecommand=(vcmd, "%d", "%S", "%P"))
        txt_xvalue.grid(row=1, column=2, padx=5, pady=(5, 0), sticky=tk.W)

        lbl_rads = tk.Label(self, text="units", font="Arial 12 bold", bg="white")
        lbl_rads.grid(row=1, column=3, padx=(0, 25), pady=(5, 0), sticky=tk.W)

        # Text field that allows the user to specify the phase angle of the graph.
        lbl_phase = tk.Label(self, text="Phase Angle:", font="Arial 12 bold", bg="white")
        lbl_phase.grid(row=2, column=0, padx=(25, 5), pady=(5, 0), sticky=tk.E)

        btn_neg_phase = tk.Button(self, text="-", font="Arial 12 bold", bg="gray30", fg="white", width=3,
                                       relief=tk.RAISED, command=lambda: self.set_negative(btn_neg_phase, "phase"))
        btn_neg_phase.grid(row=2, column=1, padx=(5, 0), pady=(5, 0), sticky=tk.E)

        txt_phase = tk.Entry(self, font="Arial 12", width=15, validate="key",
                                  validatecommand=(vcmd, "%d", "%S", "%P"))
        txt_phase.grid(row=2, column=2, padx=5, pady=(5, 0), sticky=tk.W)

        lbl_degrees = tk.Label(self, text="degrees", font="Arial 12 bold", bg="white")
        lbl_degrees.grid(row=2, column=3, padx=(0, 25), pady=(5, 0), sticky=tk.W)

        var_tangent = tk.IntVar()

        # Checkbox that determines whether or not the tangent line is shown.
        chk_tangent = tk.Checkbutton(self, font="Arial 12", bg="white", variable=var_tangent)
        chk_tangent.grid(row=3, column=0, padx=5, sticky=tk.E)

        lbl_tangent = tk.Label(self, text="Show Tangent", font="Arial 12 bold", bg="white")
        lbl_tangent.grid(row=3, column=1, columnspan=3, padx=5, sticky=tk.W)

        var_normal = tk.IntVar()

        # Checkbox that determines whether or not the normal line is shown.
        chk_normal = tk.Checkbutton(self, font="Arial 12", bg="white", variable=var_normal)
        chk_normal.grid(row=4, column=0, padx=5, sticky=tk.E)

        lbl_normal = tk.Label(self, text="Show Normal", font="Arial 12 bold", bg="white")
        lbl_normal.grid(row=4, column=1, columnspan=3, padx=5, sticky=tk.W)

        # Dynamic label that details the sine/cosine/tangent equation for the current graph of either of those functions being displayed.
        lbl_equation = tk.Label(self, text=func + " Graph Equation:", font="Arial 12 bold", bg="white")
        lbl_equation.grid(row=5, column=0, columnspan=2, padx=(25, 5), sticky=tk.E)

        dyn_equation = tk.Label(self, font="Arial 12 bold", bg="white")
        dyn_equation.grid(row=5, column=2, columnspan=2, padx=(5, 25), sticky=tk.W)

        # Dynamic label that details the tangent line equation, regardless of whether or not it is currently being shown.
        lbl_tangent_eq = tk.Label(self, text="Tangent Line Equation:", font="Arial 12 bold", bg="white")
        lbl_tangent_eq.grid(row=6, column=0, columnspan=2, padx=(25, 5), sticky=tk.E)

        dyn_tangent_eq = tk.Label(self, font="Arial 12 bold", bg="white")
        dyn_tangent_eq.grid(row=6, column=2, columnspan=2, padx=(5, 25), sticky=tk.W)

        # Dynamic label that details the normal line equation, regardless of whether or not it is currently being shown.
        lbl_normal_eq = tk.Label(self, text="Normal Line Equation:", font="Arial 12 bold", bg="white")
        lbl_normal_eq.grid(row=7, column=0, columnspan=2, padx=(25, 5), pady=(0, 5), sticky=tk.E)

        dyn_normal_eq = tk.Label(self, font="Arial 12 bold", bg="white")
        dyn_normal_eq.grid(row=7, column=2, padx=(5, 25), pady=(0, 5), sticky=tk.W)

        # Button that applies any changes made and updates the graph pane and dynamic labels of the equations accordingly.
        btn_apply = tk.Button(self, text="Apply Changes", font="Arial 12 bold", bg="gray30", fg="white",
                                   width=30,
                                   command=lambda: self.apply_changes(graph, func, dyn_equation, dyn_tangent_eq,
                                                                dyn_normal_eq,
                                                                var_tangent.get(), var_normal.get(), txt_xvalue.get(),
                                                                scl_amplitude.get(), scl_frequency.get(),
                                                                txt_phase.get()))
        btn_apply.grid(row=8, column=0, columnspan=4, padx=25, pady=(25, 5))

        # Button that opens the help menu by calling the "createHelpWindow()" function.
        btn_help = tk.Button(self, text="Show Help", font="Arial 12 bold", bg="gray30", fg="white", width=30,
                                  command=lambda: self.master.navigate_to_help_frame(func))
        btn_help.grid(row=9, column=0, columnspan=4, padx=25, pady=5)

        # Button that returns the user to main menu by calling the "returnToMainMenu()" function.
        btn_menu = tk.Button(self, text="Return to Main Menu", font="Arial 12 bold", bg="gray30", fg="white",
                                  width=30, command=lambda: self.master.navigate_to_menu())
        btn_menu.grid(row=10, column=0, columnspan=4, padx=25, pady=(5, 25))

        # Scales that determine the amplitude of the sine, cosine or tangent line.

        # If the graph is a sine or cosine graph, then set the amplitude range from 0 to 200, and give it a default value of 100.
        if (func == "Sine") or (func == "Cosine"):
            scl_amplitude = tk.Scale(self, font="Arial 12 bold", from_=0, to=200, orient=tk.HORIZONTAL,
                                          bg="white", length=250)
            scl_amplitude.set(100)
        # Else if the graph is a tangent graph, then set the amplitude range from 0 to 50, and give it a default value of 25.
        elif (func == "Tangent"):
            scl_amplitude = tk.Scale(self, font="Arial 12 bold", from_=0, to=100, orient=tk.HORIZONTAL,
                                          bg="white", length=250)
            scl_amplitude.set(50)

        scl_amplitude.grid(row=8, rowspan=2, column=4, padx=5, pady=(25, 0))

        lbl_amplitude = tk.Label(self, text="Amplitude", font="Arial 12 bold", bg="white")
        lbl_amplitude.grid(row=10, column=4, padx=5, pady=(0, 5), sticky=tk.N)

        # Scales that determine the frequency of the sine, cosine or tangent line.
        scl_frequency = tk.Scale(self, font="Arial 12 bold", from_=0, to=10, resolution=0.05,
                                      orient=tk.HORIZONTAL, bg="white", length=250)
        scl_frequency.set(1)
        scl_frequency.grid(row=8, rowspan=2, column=5, padx=5, pady=(25, 0))

        lbl_frequency = tk.Label(self, text="Frequency", font="Arial 12 bold", bg="white")
        lbl_frequency.grid(row=10, column=5, padx=5, pady=(0, 5), sticky=tk.N)

        # Initialises the graph pane (tk.Canvas), and the respective tangent and normal lines, are displayed to the user.
        graph = tk.Canvas(self, width=800, height=400, bg="white")
        graph.grid(row=1, rowspan=7, column=4, columnspan=2, padx=(0, 25))

        # Draw a graph based on the default options of the self.master.
        self.apply_changes(graph, func, dyn_equation, dyn_tangent_eq, dyn_normal_eq, var_tangent.get(), var_normal.get(),
                     txt_xvalue.get(), scl_amplitude.get(), scl_frequency.get(), txt_phase.get())

    def configure_graph_function(self, func):
        if (func == "Sine"):
            self.calc = SinCalc()
        elif (func == "Cosine"):
            self.calc = CosCalc()
        elif (func == "Tangent"):
            self.calc = TanCalc()
        else:
            raise ValueError("Function '" + str(func) + "' is undefined.")

    def set_negative(self, button, value):
        # If the button is toggled off, then set it to toggled and set the respective global boolean value to true.
        if (button["relief"] == tk.RAISED):
            button.config(relief=tk.SUNKEN)

            if (value == "xvalue"):
                self.xvalue_negative = True
            elif (value == "phase"):
                self.phase_negative = True
        # Else if the button is toggled on, then toggle it off and set the respective global boolean value to false.
        elif (button["relief"] == tk.SUNKEN):
            button.config(relief=tk.RAISED)

            if (value == "xvalue"):
                self.xvalue_negative = False
            elif (value == "phase"):
                self.phase_negative = False

    def apply_changes(self, graph, func, dyn, tan_dyn, nom_dyn, tan_chk, nom_chk, x, amp, freq, phase):
        # Clear the graph canvas completely.
        graph.delete(tk.ALL)

        if (self.xvalue_negative):
            x = "-" + x
        elif (self.phase_negative):
            phase = "-" + phase

        # Draw the axis.
        self.calc.draw_axis(graph)

        if (phase == ""):
            phase = 0

        # Dependent on the function, draw a sine, cosine or tangent graph.
        self.calc.draw_graph(graph, amp, freq, self.calc.convert_to_float(phase))

        # Update the dynamic equation label.
        self.calc.update_equation_label(dyn, str(amp), str(freq), str(phase))

        # If the "Show Tangent" checkbox is checked, then calculate the tangent and add in the appropriate line.
        if (x != "") and (tan_chk == True):
            tan_dyn.config(text=self.calc.calculate_tangent(graph, self.calc.convert_to_float(x), amp, freq, self.calc.convert_to_float(phase)))
        else:
            tan_dyn.config(text="")

        # If the "Show Normal" checkbox is checked, then calculate the normal and add in the appropriate line.
        if (x != "") and (nom_chk == True):
            nom_dyn.config(text=self.calc.calculate_normal(graph, self.calc.convert_to_float(x), amp, freq, self.calc.convert_to_float(phase)))
        else:
            nom_dyn.config(text="")