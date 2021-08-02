"""
The States of the United States
Component 01 - Foundational GUI
Version 4.0 - Added Cartogram Window and Functionality Based off of Instructions.
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

        # So that Width and Height is Measured in Pixels, Create 1x1 Image
        pixel_image = PhotoImage(width=1, height=1)

        # Play Game Button (Row 1 / Row 0)
        self.btn_m_play = Button(self.frm_m_buttons,
                                 text="Play",
                                 width=15, height=2,
                                 padx=1, pady=1)
        self.btn_m_play.grid(row=0)

        # View Cartogram Button (Row 1 / Row 1)
        self.btn_m_cartogram = Button(self.frm_m_buttons,
                                      text="View Cartogram",
                                      width=15, height=2,
                                      padx=1, pady=1,
                                      command=self.fnc_get_c)
        self.btn_m_cartogram.grid(row=1)

        # Instructions Button (Row 1 / Row 2)
        self.btn_m_instructions = Button(self.frm_m_buttons,
                                         text="Instructions",
                                         width=15, height=2,
                                         padx=1, pady=1,
                                         command=self.fnc_get_i)
        self.btn_m_instructions.grid(row=2)

        # View Past Results Button (Row 1 / Row 3)
        self.btn_m_results = Button(self.frm_m_buttons,
                                    text="View Past Results",
                                    width=15, height=2,
                                    padx=1, pady=1)
        self.btn_m_results.grid(row=3)

    def fnc_get_i(self):
        i = Instructions(self)
        i.lbl_i_text.configure(text="<<< Placeholder >>>")

    def fnc_get_c(self):
        c = Cartogram(self)


# Instructions GUI Class
class Instructions:
    # Initialize Function
    def __init__(self, menu):
        # Define Formatting Variables
        bg_colour = "grey"

        # Disable Button in Menu
        menu.btn_m_instructions.configure(state=DISABLED)

        # Create Window
        self.box_i = Toplevel()
        self.box_i.protocol('WM_DELETE_WINDOW', partial(self.fnc_i_close, menu))

        # Main Frame
        self.frm_i = Frame(self.box_i, width=100, height=100, bg=bg_colour)
        self.frm_i.grid()

        # Heading (Row 0)
        self.lbl_i_heading = Label(self.frm_i,
                                   text="Instructions",
                                   font=("Arial", "16", "bold"),
                                   bg=bg_colour,
                                   padx=10, pady=5)
        self.lbl_i_heading.grid(row=0)

        # Instruction Text (Row 1)
        self.lbl_i_text = Label(self.frm_i,
                                   text="",
                                   font=("Arial", "12"),
                                   bg=bg_colour,
                                   padx=10, pady=10)
        self.lbl_i_text.grid(row=1)

        # Footer Frame (Row 2)
        self.frm_i_footer = Frame(self.frm_i, width=100, height=20, bg=bg_colour)
        self.frm_i_footer.grid(row=2)

        # So that Width and Height is Measured in Pixels, Create 1x1 Image
        pixel_image = PhotoImage(width=1, height=1)

        # Close Button (Row 2 / Row 0)
        self.btn_i_close = Button(self.frm_i_footer,
                                 text="Close",
                                 width=10, height=2,
                                 padx=1, pady=1,
                                 command=partial(self.fnc_i_close, menu))
        self.btn_i_close.grid(row=0)

    def fnc_i_close(self, menu):
        # Re-enable Help Button
        menu.btn_m_instructions.configure(state=NORMAL)
        # Close Window
        self.box_i.destroy()


# Cartogram GUI Class
class Cartogram:
    # Initialize Function
    def __init__(self, menu):
        # Define Formatting Variables
        bg_colour = "grey"

        # Disable Button in Menu
        menu.btn_m_cartogram.configure(state=DISABLED)

        # Create Window
        self.box_c = Toplevel()
        self.box_c.protocol('WM_DELETE_WINDOW', partial(self.fnc_c_close, menu))

        # Main Frame
        self.frm_c = Frame(self.box_c, width=100, height=100, bg=bg_colour)
        self.frm_c.grid()

        # Heading (Row 0)
        self.lbl_c_heading = Label(self.frm_c,
                                   text="Cartogram",
                                   font=("Arial", "16", "bold"),
                                   bg=bg_colour,
                                   padx=10, pady=5)
        self.lbl_c_heading.grid(row=0)

        # Cartogram Frame (Row 1)
        self.frm_c_cartogram = Frame(self.frm_c, width=100, height=100, bg=bg_colour)
        self.frm_c_cartogram.grid(row=2)

        # Footer Frame (Row 2)
        self.frm_c_footer = Frame(self.frm_c, width=100, height=20, bg=bg_colour)
        self.frm_c_footer.grid(row=2)

        # So that Width and Height is Measured in Pixels, Create 1x1 Image
        pixel_image = PhotoImage(width=1, height=1)

        # Close Button (Row 2 / Row 0)
        self.btn_c_close = Button(self.frm_c_footer,
                                 text="Close",
                                 width=10, height=2,
                                 padx=1, pady=1,
                                 command=partial(self.fnc_c_close, menu))
        self.btn_c_close.grid(row=0)

    def fnc_c_close(self, menu):
        # Re-enable Help Button
        menu.btn_m_cartogram.configure(state=NORMAL)
        # Close Window
        self.box_c.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("The Presidential Election of the United States of America")
    main_window = Menu()
    root.mainloop()
