"""
The States of the United States
Component 02 - State Map GUI
Version 2.0 - Formed Function that Creates Multiple State Objects Using Row/Column
Indexes.
Finn Wescombe
03/08/21
"""

# Import Tools
from tkinter import * # For GUI Display
from functools import partial # To Prevent Unwanted Windows
import csv # For External States File and Saves File


# Cartogram GUI Class
class Cartogram_Test_Window:
    # Initialize Function
    def __init__(self):
        # Define Formatting Variables
        bg_colour = "grey"

        # Main Frame
        self.frm_c = Frame(width=100, height=100, bg=bg_colour)
        self.frm_c.grid()

        # Cartogram Frame (Row 1)
        self.frm_c_cartogram = Frame(self.frm_c, width=100, height=100, bg=bg_colour)
        self.frm_c_cartogram.grid(row=1)

        # Footer Frame (Row 2)
        self.frm_c_footer = Frame(self.frm_c, width=100, height=20, bg=bg_colour)
        self.frm_c_footer.grid(row=2)

        # Create State List
        states = [["A", [1, 1]], ["B", [1, 2]], ["C", [1, 3]],
                  ["D", [2, 1]], ["E", [2, 2]], ["F", [2, 3]],
                  ["G", [3, 1]], ["H", [3, 2]], ["I", [3, 3]]]
        self.fnc_generate_states(states)

    # Generate States Test Function
    def fnc_generate_states(self, list):
        for i in list:
            test_state = State(self, i[0], i[1][0], i[1][1])

# State Class
class State:

    def __init__(self, frame, name, row, column):

        # Define Format Variables
        bg_colour = "red"

        # State Button
        self.btn_state = Button(frame.frm_c_cartogram,
                                text=name,
                                highlightbackground="red",
                                font=("Arial", "8", "bold"),
                                width=12, height=6,
                                borderwidth=2,
                                relief="sunken",
                                state=NORMAL)
        self.btn_state.grid(row=row, column=column)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("The States of the United States")
    main_window = Cartogram_Test_Window()
    root.mainloop()
