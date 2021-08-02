"""
The States of the United States
Component 01 - Foundational GUI
Version 6.0 - Added Past Results Window and Button Functionality Based off of
Previous.
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
        self.btn_m_game = Button(self.frm_m_buttons,
                                 text="Play",
                                 width=15, height=2,
                                 padx=1, pady=1,
                                 command=self.fnc_get_g)
        self.btn_m_game.grid(row=0)

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
                                    padx=1, pady=1,
                                    command=self.fnc_get_r)
        self.btn_m_results.grid(row=3)

    def fnc_get_g(self):
        g = Game(self)

    def fnc_get_i(self):
        i = Instructions(self)
        i.lbl_i_text.configure(text="<<< Placeholder >>>")

    def fnc_get_c(self):
        c = Cartogram(self)

    def fnc_get_r(self):
        r = Results(self)
        r.lbl_r_text.configure(text="<<< Placeholder >>>")



# Game GUI Class
class Game:
    # Initialize Function
    def __init__(self, menu):
        # Define Formatting Variables
        bg_colour = "grey"

        # Disable Button in Menu
        menu.btn_m_game.configure(state=DISABLED)

        # Create Window
        self.box_g = Toplevel()
        self.box_g.protocol('WM_DELETE_WINDOW', partial(self.fnc_g_close, menu))

        # Main Frame
        self.frm_g = Frame(self.box_g, width=100, height=100, bg=bg_colour)
        self.frm_g.grid()

        # Heading (Row 0)
        self.lbl_g_heading = Label(self.frm_g,
                                   text="Game",
                                   font=("Arial", "16", "bold"),
                                   bg=bg_colour,
                                   padx=10, pady=5)
        self.lbl_g_heading.grid(row=0)

        # Cartogram Frame (Row 1)
        self.frm_g_cartogram = Frame(self.frm_g, width=100, height=100, bg=bg_colour)
        self.frm_g_cartogram.grid(row=2)

        # Footer Frame (Row 2)
        self.frm_g_footer = Frame(self.frm_g, width=100, height=20, bg=bg_colour)
        self.frm_g_footer.grid(row=2)

        # So that Width and Height is Measured in Pixels, Create 1x1 Image
        pixel_image = PhotoImage(width=1, height=1)

        # Close Button (Row 2 / Row 0)
        self.btn_g_close = Button(self.frm_g_footer,
                                 text="Close",
                                 width=10, height=2,
                                 padx=1, pady=1,
                                 command=partial(self.fnc_g_close, menu))
        self.btn_g_close.grid(row=0)

    def fnc_g_close(self, menu):
        # Re-enable Help Button
        menu.btn_m_game.configure(state=NORMAL)
        # Close Window
        self.box_g.destroy()


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


# Past Results GUI Class
class Results:
    # Initialize Function
    def __init__(self, menu):
        # Define Formatting Variables
        bg_colour = "grey"

        # Disable Button in Menu
        menu.btn_m_results.configure(state=DISABLED)

        # Create Window
        self.box_r = Toplevel()
        self.box_r.protocol('WM_DELETE_WINDOW', partial(self.fnc_r_close, menu))

        # Main Frame
        self.frm_r = Frame(self.box_r, width=100, height=100, bg=bg_colour)
        self.frm_r.grid()

        # Heading (Row 0)
        self.lbl_r_heading = Label(self.frm_r,
                                   text="Past Results",
                                   font=("Arial", "16", "bold"),
                                   bg=bg_colour,
                                   padx=10, pady=5)
        self.lbl_r_heading.grid(row=0)

        # Results Text (Row 1)
        self.lbl_r_text = Label(self.frm_r,
                                   text="",
                                   font=("Arial", "12"),
                                   bg=bg_colour,
                                   padx=10, pady=10)
        self.lbl_r_text.grid(row=1)

        # Footer Frame (Row 2)
        self.frm_r_footer = Frame(self.frm_r, width=100, height=20, bg=bg_colour)
        self.frm_r_footer.grid(row=2)

        # So that Width and Height is Measured in Pixels, Create 1x1 Image
        pixel_image = PhotoImage(width=1, height=1)

        # Close Button (Row 2 / Row 0)
        self.btn_r_close = Button(self.frm_r_footer,
                                 text="Close",
                                 width=10, height=2,
                                 padx=1, pady=1,
                                 command=partial(self.fnc_r_close, menu))
        self.btn_r_close.grid(row=0)

    def fnc_r_close(self, menu):
        # Re-enable Help Button
        menu.btn_m_results.configure(state=NORMAL)
        # Close Window
        self.box_r.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("The Presidential Election of the United States of America")
    main_window = Menu()
    root.mainloop()
