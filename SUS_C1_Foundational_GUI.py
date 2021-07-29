"""
The States of the United States
Component 01 - Foundational GUI
Version 1.0 - Created Menu GUI Window with Basic Formatting
Finn Wescombe
29/07/21
"""

# Import Tools
from tkinter import * # For GUI Display
from functools import partial # To Prevent Unwanted Windows
import csv # For External States File and Saves File

# Menu GUI Class
class Menu:
    # Initialize Function
    def __init__(self):
        # Define Background Colour
        bg_colour = "light_grey"

        # Create Main Frame
        self.frm_m = Frame(width=100, height=200, bg=bg_colour)
        self.frm_m.grid()

        # Create Heading (Row 0)
        self.lbl_m_heading = Label(self.frm_m,
                                   text="The States of the United States",
                                   font=("Arial", "16", "Bold"),
                                   bg=bg_colour,
                                   padx=10, pady=5)

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("The Presidential Election of the United States of America")
    main_window = Menu()
    root.mainloop()
