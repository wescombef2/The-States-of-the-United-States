"""
The States of the United States
Component 02 - State Map GUI
Version 3.0 - Created .csv File 'SUS_States.csv' and Changed Generate States
Function so that it Reads from the File Rather than Using a List
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

        # Call Generate States Function
        self.fnc_generate_states()

    # Generate States Test Function
    def fnc_generate_states(self):
        # Create State List from .csv file ( [Name, Votes, [Row, Column]]
        import csv

        # 8 Rows, 11 Columns
        with open('SUS_States.csv', newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter=',')
            lst_state_csv = []
            for line in filereader:
                lst_state_csv.append([line[0], [line[1], line[2]]])

        for i in lst_state_csv:
            state = State(self, i[0], i[1][0], i[1][1])

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
