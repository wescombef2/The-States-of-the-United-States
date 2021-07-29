"""
The States of the United States
Component 01 - Foundational GUI
Version 2.0 - Created Buttons Frame and Four Currently Non-Functioning Buttons
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
        # Define Formatting Variables
        bg_colour = "grey"

        # Main Frame
        self.frm_m = Frame(width=100, height=200, bg=bg_colour)
        self.frm_m.grid()

        # Heading (Row 0)
        self.lbl_m_heading = Label(self.frm_m,
                                   text="The States of the United States",
                                   font=("Arial", "16", "bold"),
                                   bg=bg_colour,
                                   padx=10, pady=5)
        self.lbl_m_heading.grid(row=0)

        # Button Frame (Row 1)
        self.frm_m_buttons = Frame(self.frm_m, width=100, height=100, bg=bg_colour)
        self.frm_m_buttons.grid(row=1)

        # Play Game Button (Row 1 / Row 0)
        self.btn_m_play = Button(self.frm_m_buttons,
                                 text="Play",
                                 width=20, height=10,
                                 padx=10, pady=10)
        self.btn_m_play.grid(row=0)

        # View Cartogram Button (Row 1 / Row 1)
        self.btn_m_cartogram = Button(self.frm_m_buttons,
                                      text="View Cartogram",
                                      width=20, height=10,
                                      padx=10, pady=10)
        self.btn_m_cartogram.grid(row=1)

        # Instructions Button (Row 1 / Row 2)
        self.btn_m_instructions = Button(self.frm_m_buttons,
                                         text="Instructions",
                                         width=20, height=10,
                                         padx=10, pady=10)
        self.btn_m_instructions.grid(row=2)

        # View Past Results Button (Row 1 / Row 3)
        self.btn_m_results = Button(self.frm_m_buttons,
                                    text="View Past Results",
                                    width=20, height=10,
                                    padx=10, pady=10)
        self.btn_m_results.grid(row=3)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("The Presidential Election of the United States of America")
    main_window = Menu()
    root.mainloop()
