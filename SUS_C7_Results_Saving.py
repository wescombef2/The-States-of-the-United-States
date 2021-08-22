"""
The States of the United States
Component 07 - Results and Saving
Version 1.0 - Saved Results in a list, refreshing each game, and displayed current
tally in internal results.
12/08/21
"""

# Import Tools
from tkinter import *  # For GUI Display
from tkinter import ttk # For Combobox
from functools import partial  # To Prevent Unwanted Windows


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
        self.frm_m_widgets = Frame(self.frm_m, width=100, height=100, bg=bg_colour)
        self.frm_m_widgets.grid(row=1)

        # So that Width and Height is Measured in Pixels, Create 1x1 Image
        pixel_image = PhotoImage(width=1, height=1)

        # Play Game Button (Row 1 / Row 0)
        self.btn_m_game = Button(self.frm_m_widgets,
                                 text="Play",
                                 width=15, height=2,
                                 padx=1, pady=1,
                                 command=self.fnc_get_g)
        self.btn_m_game.grid(row=0)

        # Combo Box (Row 1 / Row 1)
        self.lst_quiz_options = ["3 (Trial)", "10 (Short)", "20 (Long)", "51 (Complete)"]
        self.ent_m_questions = ttk.Combobox(self.frm_m_widgets)
        self.ent_m_questions['values'] = self.lst_quiz_options
        self.ent_m_questions['state'] = 'readonly'  # normal
        self.ent_m_questions.grid(row=1)

        # Instructions Button (Row 1 / Row 2)
        self.btn_m_instructions = Button(self.frm_m_widgets,
                                         text="Instructions",
                                         width=15, height=2,
                                         padx=1, pady=1,
                                         command=self.fnc_get_i)
        self.btn_m_instructions.grid(row=2)

        # View Past Results Button (Row 1 / Row 3)
        self.btn_m_results = Button(self.frm_m_widgets,
                                    text="View Past Results",
                                    width=15, height=2,
                                    padx=1, pady=1,
                                    command=self.fnc_get_r)
        self.btn_m_results.grid(row=3)

    def fnc_get_g(self):
        try:
            q_count = self.ent_m_questions.get()
            g = Game(self, q_count)
        except ValueError:
            print("Value Error")


    def fnc_get_i(self):
        i = Instructions(self)
        i.lbl_i_text.configure(text="<<< Placeholder >>>")

    def fnc_get_r(self):
        r = Results(self)
        r.lbl_r_text.configure(text="<<< Placeholder >>>")


# Game GUI Class
class Game:
    # Initialize Function
    def __init__(self, menu, q_opt):
        # Define Formatting Variables
        bg_colour = "grey"
        q_opt_split = q_opt.split(" ")
        self.q_count = int(q_opt_split[0])
        self.menu = menu

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

        # Game Cartogram and Questions Frame (Row 1)
        self.frm_g_game = Frame(self.frm_g, width=100, height=100, bg=bg_colour)
        self.frm_g_game.grid(row=1)

        # Questions Frame (Row 1 / Row 0)
        self.frm_g_internal = Frame(self.frm_g_game, width=100, height=20, bg=bg_colour)
        self.frm_g_internal.grid(row=0)

        # Basic Question Label
        self.lbl_g_question = Label(self.frm_g_internal,
                                    # Format Random Name from State List into Generic Statement
                                    text="",
                                    font=("Arial", "16", "bold"),
                                    bg=bg_colour,
                                    padx=10, pady=5)
        self.lbl_g_question.grid(row=1)

        # Cartogram Frame (Row 1 / Row 1)
        self.frm_cartogram = Frame(self.frm_g_game, width=100, height=100, bg=bg_colour)
        self.frm_cartogram.grid(row=1)

        # Footer Frame (Row 2)
        self.frm_g_footer = Frame(self.frm_g, width=100, height=20, bg=bg_colour)
        self.frm_g_footer.grid(row=2)

        # So that Width and Height is Measured in Pixels, Create 1x1 Image
        pixel_image = PhotoImage(width=1, height=1)

        # View Cartogram Button (Row 2 / Row 0, Column 0)
        self.btn_g_cartogram = Button(self.frm_g_footer,
                                      text="View Cartogram",
                                      width=15, height=2,
                                      padx=1, pady=1,
                                      command=self.fnc_get_c)
        self.btn_g_cartogram.grid(row=0, column=0)

        # Close Button (Row 2 / Row 0, Column 1)
        self.btn_g_close = Button(self.frm_g_footer,
                                  text="Close",
                                  width=10, height=2,
                                  padx=1, pady=1,
                                  command=partial(self.fnc_g_close, menu))
        self.btn_g_close.grid(row=0, column=1)

        # Generate Cartogram
        self.fnc_generate_cartogram(self, True)

        # Commence Game Routine
        self.fnc_game_intialise()

    # Game Routine Function
    def fnc_game_intialise(self):
        # Create List for Storing Selected State Objects along with other Variables
        self.lst_selected_states = [""]  # Placeholder Item so that 0 is not an Index.
        self.var_selection_index = 0 # To save index of selected item
        self.var_current_question = False # Boolean to determine whether there is a current question
        self.lst_tally = [0,0] # Saves results (correct/incorrect)
        # Generate Question
        self.fnc_internal_results("Loaded", "white") # Initial placeholder display

    # Generate Cartogram Function
    def fnc_generate_cartogram(self, frame, game_function):
        # Create State List from .csv file ( [Name, [Row, Column]]
        import csv

        # Create Blank List in Which States are Stored (Only if for new game)
        if game_function:
            self.lst_state_objects = [] # Only edits list if game function, otherwise it interferes with the current game
        # 8 Rows, 11 Columns
        with open('SUS_States.csv', newline='', encoding='utf-8-sig') as csvfile: # Open .csv file
            filereader = csv.reader(csvfile, delimiter=',')
            lst_state_csv = []
            for line in filereader:
                lst_state_csv.append([line[0], [line[1], line[2]]]) # Create list of items from csv
        for i in lst_state_csv: # for each row in csv
            state = State(frame, game_function, i[0], i[1][0], i[1][1]) # Create state object
            if game_function:
                self.lst_state_objects.append(state) # only edit list if game function

    # Generate Question Function
    def fnc_generate_question(self):
        import random

        # Destroy Generate Question Button
        self.btn_g_question.destroy() # Remove new question button

        # Boolean Variable for Current Question
        self.var_current_question = True
        # Counting Variable to Record Attempts
        self.var_current_attempts = 0

        # Create Question Label (Row 1 / Row 0 / Row 1)
        self.obj_selected_state = self.lst_state_objects[random.randint(0, len(self.lst_state_objects) - 1)]
        self.lbl_g_question.configure(text="Which State is {}?".format(self.obj_selected_state.name), bg="white")
        # Add Newly Selected State to Selected List
        self.lst_selected_states.append(self.obj_selected_state)
        # Increase Current Selection Index
        self.var_selection_index += 1

        # Return All States to White and no Name, Enabled
        for obj in self.lst_state_objects:
            obj.btn_state.configure(text="", highlightbackground="white", state=NORMAL)

    # Create Internal Results Function
    def fnc_internal_results(self, result_text, lbl_colour):
        self.q_count -= 1
        # Check if Game is Over
        # Create Internal Results GUI
        # Configure Question Label
        text = result_text + " | " + "{} Correct / {} Incorrect".format(self.lst_tally[0], self.lst_tally[1])
        self.lbl_g_question.configure(text=text, bg=lbl_colour)

        # Generate Question Button (Row 2)
        self.btn_g_question = Button(self.frm_g_internal,
                                        text="New Question",
                                         width=10, height=2,
                                         padx=1, pady=1,
                                         command=self.fnc_generate_question)
        self.btn_g_question.grid(row=2)
        if self.q_count < 0:
            self.btn_g_question.configure(text="Quit", command=partial(self.fnc_g_close, self.menu), highlightbackground="green")

    # Create Cartogram Window Function
    def fnc_get_c(self):
        c = Cartogram(self)

    # Close Window Function
    def fnc_g_close(self, menu):
        # Re-enable Help Button
        menu.btn_m_game.configure(state=NORMAL)
        # Close Window
        self.box_g.destroy()


# State Class
class State:

    def __init__(self, window, game_function, name, row, column):
        # Define Format Variables
        bg_colour = "white"

        self.name = name

        # State Button
        self.btn_state = Button(window.frm_cartogram,
                                text=self.name,
                                highlightbackground=bg_colour,
                                font=("Arial", "8", "bold"),
                                width=12, height=6,
                                borderwidth=2,
                                relief="sunken",
                                state=NORMAL)
        # Add Game Functionality If Needed
        if game_function:
            # Define Game Object for Calling in Response Function
            self.obj_game = window
            # Response Function
            self.btn_state.configure(text="", command=self.fnc_send_response)

        self.btn_state.grid(row=row, column=column)

    def fnc_send_response(self):
        # Check if current question
        if self.obj_game.var_current_question:
            if self.obj_game.obj_selected_state.name == self.name:
                self.btn_state.configure(text=self.name,
                                         highlightbackground="green")
                self.obj_game.var_current_question = False
                self.obj_game.lst_tally[0] += 1  # Add one to correct tally
                self.obj_game.fnc_internal_results("Correct", "green")  # Generate Internal Results
            else:
                self.btn_state.configure(text=self.name,
                                         highlightbackground="red",
                                         state=DISABLED)
                self.obj_game.var_current_attempts += 1
                if self.obj_game.var_current_attempts >= 3:
                    self.obj_game.var_current_question = False
                    self.obj_game.lst_tally[1] += 1  # Add one to incorrect tally
                    self.obj_game.fnc_internal_results("Incorrect", "red")


# Cartogram GUI Class
class Cartogram:
    # Initialize Function
    def __init__(self, game):
        # Define Formatting Variables
        bg_colour = "grey"

        # Disable Button in Menu
        game.btn_g_cartogram.configure(state=DISABLED)

        # Create Window
        self.box_c = Toplevel()
        self.box_c.protocol('WM_DELETE_WINDOW', partial(self.fnc_c_close, game))

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
        self.frm_cartogram = Frame(self.frm_c, width=100, height=100, bg=bg_colour)
        self.frm_cartogram.grid(row=1)

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
                                  command=partial(self.fnc_c_close, game))
        self.btn_c_close.grid(row=0)

        # Generate Cartogram
        game.fnc_generate_cartogram(self, False)

    # Close Window Function
    def fnc_c_close(self, game):
        # Re-enable Help Button
        game.btn_g_cartogram.configure(state=NORMAL)
        # Close Window
        self.box_c.destroy()


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
    root.title("The States of the United States")
    main_window = Menu()
    root.mainloop()
