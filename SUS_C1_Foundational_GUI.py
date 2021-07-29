"""
The States of the United States
Component 01 - Foundational GUI
Version 1.1 - Bugfix - Changed 'light_grey' bg_colour to 'grey',
'Bold' heading font to 'bold', and added 'self.lbl_m_heading.grid(row=0)'
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
        bg_colour = "grey"

        # Create Main Frame
        self.frm_m = Frame(width=100, height=200, bg=bg_colour)
        self.frm_m.grid()

        # Create Heading (Row 0)
        self.lbl_m_heading = Label(self.frm_m,
                                   text="The States of the United States",
                                   font=("Arial", "16", "bold"),
                                   bg=bg_colour,
                                   padx=10, pady=5)
        self.lbl_m_heading.grid(row=0)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("The Presidential Election of the United States of America")
    main_window = Menu()
    root.mainloop()
