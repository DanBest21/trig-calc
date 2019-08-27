import Tkinter as tk
import gui.Menu as menu

window = tk.Tk()
window.resizable(False, False)
window.title("Tangent/Normal Calculator")
frame = menu.Menu(window)
frame.pack()
window.mainloop()
