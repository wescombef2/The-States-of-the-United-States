"""
The States of the United States
Component 08 - Improvements
Version 1.2 – Created a header frame for the game window that is configured
appropriately for questions, internal results, and external results, for
increased efficiency for both the program and user.
25/08/21
"""

# Import Tools
from tkinter import *  # For GUI Display
from tkinter import ttk  # For Combobox
from functools import partial  # To Prevent Unwanted Windows
from PIL import Image, ImageTk


# Menu GUI Class
class Menu:

    # Initialize Function
    def __init__(self):
        # Define Formatting Variables
        bg_colour = "white"

        # Main Frame
        self.frm_m = Frame(width=100, height=200, bg=bg_colour)
        self.frm_m.grid()

        # Logo and Heading (Row 0)
        self.img_logo = Image.open("SUS_Logo.gif")  # Open Image
        self.img_logo = self.img_logo.resize((400, 230),
                                             Image.ANTIALIAS)  # Resize image
        self.img_logo = ImageTk.PhotoImage(self.img_logo)  # Make PhotoImage
        # Use Heading Label for Image
        self.lbl_m_heading = Label(self.frm_m,
                                   image=self.img_logo,
                                   bg=bg_colour,
                                   padx=10, pady=5)
        self.lbl_m_heading.grid(row=0)

        # Primary Button Frame (Row 1)
        self.frm_m_widgets = Frame(self.frm_m, width=100, height=100,
                                   bg=bg_colour)
        self.frm_m_widgets.grid(row=1)

        # Play Game Button (Row 1 / Row 0, Column 0)
        self.btn_m_game = Button(self.frm_m_widgets,
                                 text="Play",
                                 width=15, height=2,
                                 padx=1, pady=1,
                                 command=self.fnc_get_g)
        self.btn_m_game.grid(row=0, column=0)

        # Quiz Option Frame (Row 1 / Row 0, Column 1)
        self.frm_m_options = Frame(self.frm_m_widgets, width=30, height=30,
                                   bg=bg_colour)
        self.frm_m_options.grid(row=0, column=1)

        # Options Label (Row 1 / Row 0, Column 1 / Row 0)
        self.lbl_m_options = Label(self.frm_m_options,
                                   text="Select Quiz",
                                   font=("Arial", "8", "bold"),
                                   bg=bg_colour,
                                   padx=10, pady=1)
        self.lbl_m_options.grid(row=0)

        # Combo Box (Row 1 / Row 0, Column 1 / Row 1)
        self.lst_quiz_options = ["3 (Trial)", "10 (Short)", "20 (Long)",
                                 "51 (Complete)"]
        self.ent_m_questions = ttk.Combobox(self.frm_m_options)
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
        instruction_text = "The States of the United States is a memory-based\n" \
                           "quiz around the locations of the states in a box\n" \
                           "cartographic form. To begin the game, select the quiz\n" \
                           "type and press 'Play' play in the menu. The game will\n" \
                           "provide a blank cartogram and a question; to answer,\n" \
                           "you must press the correct state within three tries.\n" \
                           "When you have answered all questions, whether correct\n" \
                           "or incorrect, the game will end and you will have the\n" \
                           "chance to save your results with a username before\n" \
                           "you return to the menu. This is optional. "
        i = Message_Box("Instructions", instruction_text, "",
                        self.btn_m_instructions)
        i.lbl_mb_text.configure(height=10, anchor=N)

    def fnc_get_r(self):
        r = Results(self)


# Message Box Class
class Message_Box:
    # Initialize Function
    def __init__(self, heading, text, footer_text, partner_button):

        # For Disable/Reenable Buttons
        if partner_button:
            self.partner_button = partner_button
            self.partner_button.configure(state=DISABLED)
        else:
            self.partner_button = ""
        # Define Formatting Variables
        bg_colour = "white"

        # Create Window
        self.box_mb = Toplevel()

        self.box_mb.protocol('WM_DELETE_WINDOW', self.fnc_mb_close)

        # Main Frame
        self.frm_mb = Frame(self.box_mb, width=30, height=30, bg=bg_colour)
        self.frm_mb.grid()

        # Heading (Row 0)
        self.lbl_mb_heading = Label(self.frm_mb,
                                    text=heading,
                                    font=("Arial", "16", "bold"),
                                    bg="dark blue",
                                    fg="white",
                                    width=30,
                                    padx=10, pady=5)
        self.lbl_mb_heading.grid(row=0)

        # Text (Row 1)
        self.lbl_mb_text = Label(self.frm_mb,
                                 text=text,
                                 font=("Arial", "12"),
                                 bg="white",
                                 fg="black",
                                 width=38,
                                 padx=20, pady=10)
        self.lbl_mb_text.grid(row=1)

        # Footer Frame (Row 2)
        self.frm_mb_footer = Frame(self.frm_mb, width=30, height=20,
                                   bg=bg_colour)
        self.frm_mb_footer.grid(row=2)

        # Footer Text (Row 2 / Row 0, Column 0)
        self.lbl_mb_foottext = Label(self.frm_mb_footer,
                                     text=footer_text,
                                     font=("Arial", "16"),
                                     bg="white",
                                     fg="black",
                                     width=30,
                                     padx=10, pady=10)
        self.lbl_mb_foottext.grid(row=0)

        # Close Button (Row 2 / Row 0, Column 1)
        self.btn_mb_close = Button(self.frm_mb_footer,
                                   text="Close",
                                   width=10, height=2,
                                   padx=1, pady=1,
                                   command=self.fnc_mb_close)
        self.btn_mb_close.grid(row=0)

    def fnc_mb_close(self):
        # Re-enable Help Button
        if self.partner_button:
            self.partner_button.configure(state=NORMAL)
        # Close Window
        self.box_mb.destroy()


# Game Class
class Game:
    # Initialize Function
    def __init__(self, menu, q_opt):

        # Set Up

        # Define Formatting Variables
        bg_colour = "white"
        q_opt_split = q_opt.split(" ")
        self.q_count = int(q_opt_split[0])
        self.menu = menu
        # Disable Button in Menu
        menu.btn_m_game.configure(state=DISABLED)

        # Create GUI

        # Create Window
        self.box_g = Toplevel()
        self.box_g.protocol('WM_DELETE_WINDOW', self.fnc_g_close)

        # Main Frame
        self.frm_g = Frame(self.box_g, width=100, height=100, bg=bg_colour)
        self.frm_g.grid()

        # Header Frame, for Questions and Results (Row 1)
        self.frm_header = Frame(self.frm_g, width=100, height=40,
                                bg=bg_colour)
        self.frm_header.grid(row=1)

        # Header Label
        self.lbl_header = Label(self.frm_header, text="",
                                font=("Arial", "16", "bold"),
                                bg="dark blue", fg="white",
                                width=100, padx=30, pady=5)
        self.lbl_header.grid(row=0)

        # Header Widget Frame (for results)
        self.frm_header_widgets = Frame(self.frm_header, width=100, height=20,
                                        bg=bg_colour)
        self.frm_header_widgets.grid(row=1)

        # Header Button (Column 1 so that Username Entry can be to left)
        self.btn_header = Button(self.frm_header_widgets,
                                 text="Continue",
                                 font=("Arial", "11", "bold"),
                                 width=20, height=2,
                                 padx=1, pady=1,
                                 command=self.fnc_generate_question)
        self.btn_header.grid(row=0, column=1)

        # Cartogram Frame (Row 2)
        self.frm_cartogram = Frame(self.frm_g, width=100, height=100,
                                   bg=bg_colour)
        self.frm_cartogram.grid(row=2)

        # Footer Frame (Row 3)
        self.frm_g_footer = Frame(self.frm_g, width=100, height=20,
                                  bg=bg_colour)
        self.frm_g_footer.grid(row=3)

        # Commence Game Routine
        self.fnc_game_intialise()

    # Game Routine Function
    def fnc_game_intialise(self):
        # Generate Cartogram
        self.fnc_generate_cartogram(self, True)

        # Create List for Storing Selected State Objects along with other Variables
        self.lst_selected_states = [
            ""]  # Placeholder Item so that 0 is not an Index.
        self.var_selection_index = 0  # To save index of selected item
        self.var_current_question = False  # Boolean to determine whether there is a current question
        self.lst_tally = [0, 0]  # Saves results (correct/incorrect)

        # Generate Question
        self.fnc_generate_question()

    # Generate Cartogram Function
    def fnc_generate_cartogram(self, frame, game_function):
        # Create State List from .csv file ( [Name, [Row, Column]]
        import csv

        # Create Blank List in Which States are Stored (Only if for new game)
        if game_function:
            self.lst_state_objects = []  # Only edits list if game function, otherwise it interferes with the current game
        # 8 Rows, 11 Columns
        with open('SUS_States.csv', newline='',
                  encoding='utf-8-sig') as csvfile:  # Open .csv file
            filereader = csv.reader(csvfile, delimiter=',')
            lst_state_csv = []
            for line in filereader:
                lst_state_csv.append([line[0], [line[1], line[
                    2]]])  # Create list of items from csv
        for i in lst_state_csv:  # for each row in csv
            state = State(frame, game_function, i[0], i[1][0],
                          i[1][1])  # Create state object
            if game_function:
                self.lst_state_objects.append(
                    state)  # only edit list if game function

    # Generate Question Function
    def fnc_generate_question(self):
        import random

        # Disable Header Button
        self.btn_header.configure(state=DISABLED)

        # Boolean Variable for Current Question
        self.var_current_question = True
        # Counting Variable to Record Attempts
        self.var_current_attempts = 0

        # Create Question Label (Row 1 / Row 0 / Row 1)
        self.obj_selected_state = self.lst_state_objects[
            random.randint(0, len(self.lst_state_objects) - 1)]
        self.lbl_header.configure(
            text="Which State is {}?".format(self.obj_selected_state.name),
            bg="dark blue")
        # Add Newly Selected State to Selected List
        self.lst_selected_states.append(self.obj_selected_state)
        # Increase Current Selection Index
        self.var_selection_index += 1

        # Return All States to White and no Name, Enabled
        for obj in self.lst_state_objects:
            obj.btn_state.configure(text="", bg="white",
                                    state=NORMAL)

    # Generate Internal Results Functions
    def fnc_internal_results(self, result_text, lbl_colour):
        # Enable Header Button
        self.btn_header.configure(state=NORMAL)

        # Configure Header Label
        text = result_text + " | " + "{} Correct / {} Incorrect".format(
            self.lst_tally[0], self.lst_tally[1])
        self.lbl_header.configure(text=text, bg=lbl_colour)

        # Check if Game is Over
        if self.q_count <= 0:  # if so
            # Configure Header Button for Generating External Results
            self.btn_header.configure(text="Complete",
                                      command=self.fnc_external_results)

    # Generate External Results Functions
    def fnc_external_results(self):
        # Configure Header Label
        text = "{} Correct / {} Incorrect".format(
            self.lst_tally[0], self.lst_tally[1])
        self.lbl_header.configure(text=text, bg="dark blue")

        # Configure Continue Button for Saving
        self.btn_header.configure(text="Save Results",
                                  command=self.fnc_save_results)

        # Username Entry Frame (Row 1 / Row 0, Column 0)
        self.frm_username = Frame(self.frm_header_widgets, width=10, height=10,
                                  bg="white")
        self.frm_username.grid(row=0, column=0)

        # Username Label (Row 1 / Row 0, Column 0 / Row 0)
        self.lbl_username = Label(self.frm_username,
                                  text="To Save, Enter Your Username",
                                  font=("Arial", "8", "bold"),
                                  bg="white",
                                  padx=10, pady=1)
        self.lbl_username.grid(row=0)

        # Username Entry Box (Row 1 / Row 0, Column 0 / Row 1)
        self.ent_username = Entry(self.frm_username,
                                  width=15,
                                  font=("Arial", "14", "bold"),
                                  justify=CENTER)
        self.ent_username.grid(row=1)

    # Save Results Function
    def fnc_save_results(self):
        # Get Username
        username = self.ent_username.get()
        # Create list for storing Username and Tally
        append_row = [username, self.lst_tally[0], self.lst_tally[1]]
        # Write to a csv file
        from csv import writer
        # open the file in the append mode
        with open('SUS_Saved_Results.csv', 'a', newline='',
                  encoding='utf-8-sig') as f_object:
            # create the csv writer
            writer_object = writer(f_object)

            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(append_row)
            # Close the file object
            f_object.close()

        self.fnc_get_message()
        # Destroy game window
        self.fnc_g_close()

    # Display Save Success Message
    def fnc_get_message(self):
        mb = Message_Box("Save Successful", "", "", "")

    # Close Window Function
    def fnc_g_close(self):
        # Re-enable Help Button
        self.menu.btn_m_game.configure(state=NORMAL)
        # Close Window
        self.box_g.destroy()

# State Class
class State:

    def __init__(self, window, game_function, name, row, column):
        # Define Format Variables

        self.name = name

        # State Button
        self.btn_state = Button(window.frm_cartogram,
                                text=self.name,
                                fg="white",
                                font=("Arial", "9", "bold"),
                                width=12, height=6,
                                borderwidth=4,
                                relief="sunken",
                                state=NORMAL)
        # Add Game Functionality If Needed
        if game_function:
            # Define Game Object for Calling in Response Function
            self.obj_game = window
            # Response Function
            self.btn_state.configure(text="", command=self.fnc_evaluate_input)

        self.btn_state.grid(row=row, column=column)

    def fnc_evaluate_input(self):
        # Check if current question (otherwise nothing happens)
        if self.obj_game.var_current_question:
            # Check if Correct State for Current Question
            if self.obj_game.obj_selected_state.name == self.name:  # If correct
                # Configure State Button Accordingly
                self.btn_state.configure(text=self.name,
                                         bg="dark blue")
                # Change Game Variables Accordingly
                self.obj_game.var_current_question = False  # No current question
                self.obj_game.q_count -= 1  # Question complete, fewer remaining
                self.obj_game.lst_tally[0] += 1  # Add one to correct tally
                # Generate Internal Results
                self.obj_game.fnc_internal_results("Correct", "dark blue")

            else:  # If Incorrect
                self.btn_state.configure(bg="red",
                                         state=DISABLED)  # Make State red and disabled

                self.obj_game.var_current_attempts += 1  # Increase attempt count
                if self.obj_game.var_current_attempts >= 3:  # Check if third attempt, if so
                    # Change Game Variables Accordingly
                    self.obj_game.var_current_question = False
                    self.obj_game.lst_tally[
                        1] += 1  # Add one to incorrect tally
                    self.obj_game.q_count -= 1  # Question complete, fewer remaining
                    # Generate Internal Results
                    self.obj_game.fnc_internal_results("Incorrect", "red")


# Cartogram GUI Class
class Cartogram:
    # Initialize Function
    def __init__(self, game):
        # Define Formatting Variables
        bg_colour = "white"

        # Disable Button in Menu
        game.btn_g_cartogram.configure(state=DISABLED)

        # Create Window
        self.box_c = Toplevel()
        self.box_c.protocol('WM_DELETE_WINDOW',
                            partial(self.fnc_c_close, game))

        # Main Frame
        self.frm_c = Frame(self.box_c, width=100, height=100, bg=bg_colour)
        self.frm_c.grid()

        # Heading (Row 0)
        self.lbl_c_heading = Label(self.frm_c,
                                   text="Cartogram",
                                   font=("Arial", "16", "bold"),
                                   bg="dark blue",
                                   fg="white",
                                   width=100,
                                   padx=10, pady=5)
        self.lbl_c_heading.grid(row=0)

        # Cartogram Frame (Row 1)
        self.frm_cartogram = Frame(self.frm_c, width=100, height=100,
                                   bg=bg_colour)
        self.frm_cartogram.grid(row=1)

        # Footer Frame (Row 2)
        self.frm_c_footer = Frame(self.frm_c, width=100, height=20,
                                  bg=bg_colour)
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


# Past Results GUI Class
class Results:
    # Initialize Function
    def __init__(self, menu):
        # Define Formatting Variables
        bg_colour = "white"

        # Disable Button in Menu
        menu.btn_m_results.configure(state=DISABLED)

        # Read csv file
        import csv
        from operator import itemgetter  # For sorting

        # Create Blank List in Which Results are Stored
        self.lst_results = []

        with open('SUS_Saved_Results.csv', newline='',
                  encoding='utf-8-sig') as csvfile:  # Open .csv file
            filereader = csv.reader(csvfile, delimiter=',')
            lst_results = []
            for line in filereader:
                percentage = (int(line[1]) / (
                            int(line[1]) + int(line[2]))) * 100
                lst_results.append([line[0], int(line[1]), int(line[2]),
                                    percentage])  # Create list of items from csv
        # Sort list results by percentage
        self.lst_sorted_results = sorted(lst_results, key=itemgetter(3),
                                         reverse=True)

        # Create Window
        self.box_r = Toplevel()
        self.box_r.protocol('WM_DELETE_WINDOW',
                            partial(self.fnc_r_close, menu))

        # Main Frame
        self.frm_r = Frame(self.box_r, width=100, height=100, bg=bg_colour)
        self.frm_r.grid()

        # Heading (Row 0)
        self.lbl_r_heading = Label(self.frm_r,
                                   text="Past Results",
                                   font=("Arial", "16", "bold"),
                                   bg="dark blue",
                                   fg="white",
                                   width=50,
                                   padx=10, pady=5)
        self.lbl_r_heading.grid(row=0)

        # Searching Frame (Row 1)
        self.frm_r_search = Frame(self.frm_r, width=100, height=50,
                                  bg=bg_colour)
        self.frm_r_search.grid(row=1)

        # Entry Box (Row 1, / Row 0, Column 0)
        self.ent_r_username = Entry(self.frm_r_search,
                                    width=15,
                                    font=("Arial", "14", "bold"),
                                    justify=CENTER)
        self.ent_r_username.grid(row=0, column=0)

        # Save Results Button (Row 1 / Row 0, Column 1)
        self.btn_r_search = Button(self.frm_r_search,
                                   text="Search Results",
                                   width=15, height=2,
                                   padx=1, pady=1,
                                   command=self.fnc_r_search_results)
        self.btn_r_search.grid(row=0, column=1)

        # Results Text (Row 2)
        self.lbl_r_text = Label(self.frm_r,
                                text="",
                                font=("Arial", "12"),
                                bg="white",
                                padx=10, pady=10)
        self.lbl_r_text.grid(row=2)

        # Footer Frame (Row 3)
        self.frm_r_footer = Frame(self.frm_r, width=100, height=20,
                                  bg=bg_colour)
        self.frm_r_footer.grid(row=3)

        # Close Button (Row 3 / Row 0)
        self.btn_r_close = Button(self.frm_r_footer,
                                  text="Close",
                                  width=10, height=2,
                                  padx=1, pady=1,
                                  command=partial(self.fnc_r_close, menu))
        self.btn_r_close.grid(row=0)

        # Configure Results Text
        highest_results = ""
        for i in range(0, 5):
            highest_results += self.fnc_r_lst_to_txt(
                self.lst_sorted_results[i])
        self.lbl_r_text.configure(text=highest_results)

    def fnc_r_close(self, menu):
        # Re-enable Help Button
        menu.btn_m_results.configure(state=NORMAL)
        # Close Window
        self.box_r.destroy()

    def fnc_r_search_results(self):
        # Get search username
        var_search_username = self.ent_r_username.get()
        lst_matching_results = []
        for r in self.lst_sorted_results:
            if r[0] == var_search_username:
                lst_matching_results.append(r)

        matching_results = ""
        for r in lst_matching_results:
            matching_results += self.fnc_r_lst_to_txt(r)
        if matching_results:
            self.lbl_r_text.configure(text=matching_results)
        else:  # Display message if no results
            self.lbl_r_text.configure(
                text="There are no results with this username.")

    def fnc_r_lst_to_txt(self, input):
        txt = "{} | {:.1f}% ({} Correct / {} Incorrect)\n".format(input[0],
                                                                  input[3],
                                                                  input[1],
                                                                  input[2])
        return txt


# Main Routine

if __name__ == "__main__":
    root = Tk()
    root.title("The States of the United States")
    main_window = Menu()
    root.mainloop()
