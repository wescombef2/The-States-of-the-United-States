"""
The States of the United States
Component 08 - Improvements
Version 2.2 – Updated instructions to match the new game systems, swapped menu
instructions and result button locations, added question number/remaining
tracking in game.
25/08/21
"""

# Import Tools
from tkinter import *  # For GUI Display
from tkinter import ttk  # For Combobox
import tkinter as tk  # For GUI
from functools import partial  # To Prevent Unwanted Windows
from PIL import Image, ImageTk  # For Logo Image (to resize)


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
        self.lst_quiz_options = ["3 Questions (Random)", "10 Questions (States)", "10 Questions (Capitals)",
                                 "20 Questions (Random)"]
        self.ent_m_questions = ttk.Combobox(self.frm_m_options)
        self.ent_m_questions['values'] = self.lst_quiz_options
        self.ent_m_questions['state'] = 'readonly'  # normal
        self.ent_m_questions.grid(row=1)

        # View Past Results Button (Row 1 / Row 2)
        self.btn_m_results = Button(self.frm_m_widgets,
                                    text="View Past Results",
                                    width=15, height=2,
                                    padx=1, pady=1,
                                    command=self.fnc_get_r)
        self.btn_m_results.grid(row=2)

        # Instructions Button (Row 1 / Row 3)
        self.btn_m_instructions = Button(self.frm_m_widgets,
                                         text="Instructions",
                                         width=15, height=2,
                                         padx=1, pady=1,
                                         command=self.fnc_get_i)
        self.btn_m_instructions.grid(row=3)



    def fnc_get_g(self):
        try:
            q_opt = self.ent_m_questions.get()
            g = Game(self, q_opt)
        except ValueError:
            self.ent_m_questions.set('Required')

    def fnc_get_i(self):
        instruction_text = "The States of the United States is a memory-based\n" \
                           "quiz around the locations of states in a box cartogram,\n" \
                           "given the name of the state or, once the states have\n" \
                           "been memorized, the state's capital. You are given three\n" \
                           "guesses before failing each question. Once you have\n" \
                           "completed the quiz, you will be able to see a reference\n" \
                           "cartogram and given the option save your results with a\n" \
                           "username. You can find saved results from the menu.\n"
        i = Message_Box("Instructions", instruction_text, "",
                        self.btn_m_instructions)
        i.lbl_mb_text.configure(height=10, anchor=N)

    def fnc_get_r(self):
        r = Results(self)


# Message Box Class
class Message_Box:
    # Initialize Function
    def __init__(self, heading, text, footer_text, partner_button):

        # Define Formatting Variables
        bg_colour = "white"

        # Create Window
        self.box_mb = Toplevel()
        self.box_mb.protocol('WM_DELETE_WINDOW', self.fnc_mb_close)
        self.box_mb.iconbitmap('SUS_Logo.ico')

        # For Disable/Reenable Buttons
        if partner_button:
            self.partner_button = partner_button
            self.partner_button.configure(state=DISABLED)
        else:
            self.partner_button = ""

        # Main Frame
        self.frm_mb = Frame(self.box_mb, width=30, height=30, bg=bg_colour)
        self.frm_mb.grid()

        # Heading Frame
        self.frm_header = Frame(self.frm_mb, width=30, height=30, bg=bg_colour)
        self.frm_header.grid(row=0)

        # Logo and Heading (Row 0, Column 0)
        self.img_logo = Image.open("SUS_Logo.gif")  # Open Image
        self.img_logo = self.img_logo.resize((120, 80),
                                             Image.ANTIALIAS)  # Resize image
        self.img_logo = ImageTk.PhotoImage(self.img_logo)  # Make PhotoImage
        # Use Heading Label for Image
        self.lbl_image = Label(self.frm_header,
                                   image=self.img_logo,
                                   bg=bg_colour,
                                   padx=10, pady=5)
        self.lbl_image.grid(row=0, column=0)

        # Heading (Row 0)
        self.lbl_mb_heading = Label(self.frm_header,
                                    text=heading,
                                    font=("Arial", "16", "bold"),
                                    bg="dark blue",
                                    fg="white",
                                    width=20,
                                    padx=10, pady=5)
        self.lbl_mb_heading.grid(row=0, column=1)

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
                if line:
                    percentage = (int(line[1]) / (
                            int(line[1]) + int(line[2]))) * 100
                    lst_results.append([line[0], int(line[1]), int(line[2]),
                                        percentage, line[3]])  # Create list of items from csv
        # Sort list results by percentage
        self.lst_sorted_results = sorted(lst_results, key=itemgetter(3),
                                         reverse=True)

        # Create Window
        self.box_r = Toplevel()
        self.box_r.protocol('WM_DELETE_WINDOW',
                            partial(self.fnc_r_close, menu))
        self.box_r.iconbitmap('SUS_Logo.ico')
        # Main Frame
        self.frm_r = Frame(self.box_r, width=100, height=100, bg=bg_colour)
        self.frm_r.grid()

        # Heading Frame
        self.frm_header = Frame(self.frm_r, width=30, height=30, bg=bg_colour)
        self.frm_header.grid(row=0)

        # Logo and Heading (Row 0, Column 0)
        self.img_logo = Image.open("SUS_Logo.gif")  # Open Image
        self.img_logo = self.img_logo.resize((120, 80),
                                             Image.ANTIALIAS)  # Resize image
        self.img_logo = ImageTk.PhotoImage(self.img_logo)  # Make PhotoImage
        # Use Heading Label for Image
        self.lbl_image = Label(self.frm_header,
                                   image=self.img_logo,
                                   bg=bg_colour,
                                   padx=10, pady=5)
        self.lbl_image.grid(row=0, column=0)

        # Heading (Row 0)
        self.lbl_r_heading = Label(self.frm_header,
                                   text="Past Results",
                                   font=("Arial", "16", "bold"),
                                   bg="dark blue",
                                   fg="white",
                                   width=20,
                                   padx=10, pady=5)
        self.lbl_r_heading.grid(row=0, column=1)

        # Searching Frame (Row 1)
        self.frm_r_search = Frame(self.frm_r, width=100, height=50,
                                  bg=bg_colour)
        self.frm_r_search.grid(row=1)

        # Username Entry Frame (Row 1 / Row 0, Column 0)
        self.frm_username = Frame(self.frm_r_search, width=10, height=10,
                                  bg="white")
        self.frm_username.grid(row=0, column=0)

        # Username Label (Row 1 / Row 0, Column 0 / Row 0)
        self.lbl_username = Label(self.frm_username,
                                  text="Enter a Username to Search",
                                  font=("Arial", "8", "bold"),
                                  bg="white",
                                  padx=10, pady=1)
        self.lbl_username.grid(row=0)

        # Username Entry Box (Row 1 / Row 0, Column 0 / Row 1)
        self.ent_username = Entry(self.frm_username,
                                  width=15,
                                  font=("Arial", "12", "bold"),
                                  fg="black",
                                  justify=CENTER)
        self.ent_username.grid(row=1)

        # Search Results Button (Row 1 / Row 0, Column 1)
        self.btn_r_search = Button(self.frm_r_search,
                                   text="Search Results",
                                   width=15, height=2,
                                   padx=1, pady=1,
                                   command=self.fnc_r_search_results)
        self.btn_r_search.grid(row=0, column=1)

        # Search Results Label (Row 2)
        self.lbl_search_heading = Label(self.frm_r,
                                   text="Top Five Results",
                                   font=("Arial", "8", "bold"),
                                   bg="dark blue",
                                   fg="white",
                                   width=35,
                                   padx=10, pady=5)
        self.lbl_search_heading.grid(row=2)

        # Text Frame (Row 3)
        self.frm_username = Frame(self.frm_r, width=10, height=10,
                                  bg="white")
        self.frm_username.grid(row=3)

        # Username Text (Row 3 / Column 0)
        self.lbl_username_text = Label(self.frm_username,
                                text="",
                                font=("Arial", "12"),
                                bg="white",
                                padx=10, pady=10)
        self.lbl_username_text.grid(row=0, column=0)

        # Results Text (Row 3 / Column 1)
        self.lbl_result_text = Label(self.frm_username,
                                text="",
                                font=("Arial", "12"),
                                bg="white",
                                padx=10, pady=10)
        self.lbl_result_text.grid(row=0, column=1)

        # Date Text (Row 3 / Column 2)
        self.lbl_date_text = Label(self.frm_username,
                                text="",
                                font=("Arial", "12"),
                                bg="white",
                                padx=10, pady=10)
        self.lbl_date_text.grid(row=0, column=2)

        # Footer Frame (Row 3)
        self.frm_r_footer = Frame(self.frm_r, width=100, height=20,
                                  bg=bg_colour)
        self.frm_r_footer.grid(row=4)

        # Close Button (Row 3 / Row 0)
        self.btn_r_close = Button(self.frm_r_footer,
                                  text="Close",
                                  width=10, height=2,
                                  padx=1, pady=1,
                                  command=partial(self.fnc_r_close, menu))
        self.btn_r_close.grid(row=0)

        # Configure Results Text
        # Check if results
        usernames = ""
        results = ""
        dates = ""
        if len(self.lst_sorted_results) >= 5:
            for i in range(0, 5):
                lst = self.fnc_r_lst_to_txt(self.lst_sorted_results[i])
                usernames += lst[0]
                results += lst[1]
                dates += lst[2]
            self.fnc_r_configure_text(usernames, results, dates)
        elif len(self.lst_sorted_results) == 0:
            self.lbl_search_heading.configure(text="There are no saved results",
                                              bg="dark blue")
        else:
            for i in range(0, len(self.lst_sorted_results)):
                lst = self.fnc_r_lst_to_txt(self.lst_sorted_results[i])
                usernames += lst[0]
                results += lst[1]
                dates += lst[2]
            self.fnc_r_configure_text(usernames, results, dates)

    def fnc_r_search_results(self):
        # Get search username
        var_search_username = self.ent_username.get()

        lst_matching_results = []
        for r in self.lst_sorted_results:
            if r[0] == var_search_username:
                lst_matching_results.append(r)

        usernames = ""
        results = ""
        dates = ""
        for r in lst_matching_results:
            lst = self.fnc_r_lst_to_txt(r)
            usernames += lst[0]
            results += lst[1]
            dates += lst[2]
        if usernames:
            self.fnc_r_configure_text(usernames, results, dates)
            self.lbl_search_heading.configure(text="Search Results for '{}'".
                                              format(var_search_username),
                                              bg="dark blue")
        else:  # Display message if no results
            self.fnc_r_configure_text("", "", "")
            self.lbl_search_heading.configure(
                text="There are no results matching '{}'".
                    format(var_search_username), bg="red")

    def fnc_r_configure_text(self, usernames, results, date):
        self.lbl_username_text.configure(text=usernames)
        self.lbl_result_text.configure(text=results)
        self.lbl_date_text.configure(text=date)

    def fnc_r_lst_to_txt(self, input):
        txt_username = "{}\n".format(input[0])
        txt_result = "[ {:.1f}% ({}/{}) ]\n".format(input[3], input[1], (input[1]+input[2]))
        txt_dates = "{}\n".format(input[4])
        return txt_username, txt_result, txt_dates

    def fnc_r_close(self, menu):
        # Re-enable Help Button
        menu.btn_m_results.configure(state=NORMAL)
        # Close Window
        self.box_r.destroy()


# Game Class
class Game:
    # Initialize Function
    def __init__(self, menu, q_opt):

        # Set Up

        # Define Formatting Variables
        bg_colour = "white"

        # Get the Quiz Option
        q_opt_split = q_opt.split(" ")
        self.q_count = int(q_opt_split[0])
        self.q_remaining = self.q_count
        self.q_type = q_opt_split[2]
        self.menu = menu
        # Disable Button in Menu
        menu.btn_m_game.configure(state=DISABLED)

        # Create GUI

        # Create Window
        self.box_g = Toplevel()
        self.box_g.protocol('WM_DELETE_WINDOW', self.fnc_g_close)
        self.box_g.iconbitmap('SUS_Logo.ico')
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
                                width=65, padx=30, pady=5)
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
                lst_state_csv.append([line[0], line[3], [line[1], line[2]]])  # Create list of items from csv
        for i in lst_state_csv:  # for each row in csv
            state = State(frame, game_function, i[0], i[1], i[2][0],
                          i[2][1])  # Create state object
            if game_function:
                self.lst_state_objects.append(
                    state)  # only edit list if game function

    # Generate Question Function
    def fnc_generate_question(self):
        import random

        self.q_remaining -= 1

        # Return All States to White and no Name, Enabled
        for obj in self.lst_state_objects:
            obj.btn_state.configure(text="", bg="white",
                                    state=NORMAL)

        # Disable Header Button
        self.btn_header.configure(state=DISABLED)

        # Boolean Variable for Current Question
        self.var_current_question = True
        # Counting Variable to Record Attempts
        self.var_current_attempts = 0

        # Randomly Select a State Object
        self.obj_selected_state = self.lst_state_objects[
            random.randint(0, len(self.lst_state_objects) - 1)]

        # Check Quiz Type
        lst_q_types = ["(Random)", "(States)", "(Capitals)"]
        current_q_type = 0
        if self.q_type == lst_q_types[0]:
            # If random, select random current question type
            current_q_type = random.randint(1,2)
        if self.q_type == lst_q_types[1] or current_q_type == 1:
            self.lbl_header.configure(
            text="Question {} of {}: Which State is {}?".format(self.q_count-self.q_remaining, self.q_count, self.obj_selected_state.name),
            bg="dark blue")
        else:
            self.lbl_header.configure(
            text="{} is the Capital of which State?".format(self.obj_selected_state.capital),
            bg="dark blue")

        # Add Newly Selected State to Selected List
        self.lst_selected_states.append(self.obj_selected_state)
        # Increase Current Selection Index
        self.var_selection_index += 1

    # Generate Internal Results Functions
    def fnc_internal_results(self, result_text, lbl_colour):
        # Enable Header Button
        self.btn_header.configure(state=NORMAL)

        # Configure Header Label
        text = result_text + " | " + "{} Correct / {} Incorrect".format(
            self.lst_tally[0], self.lst_tally[1])
        self.lbl_header.configure(text=text, bg=lbl_colour)

        # Check if Game is Over
        if self.q_remaining <= 0:  # if so
            # Configure Header Button for Generating External Results
            self.btn_header.configure(text="Complete",
                                      command=self.fnc_external_results)

    # Generate External Results Functions
    def fnc_external_results(self):
        # Return All States to White and no Name, Enabled
        for obj in self.lst_state_objects:
            obj.btn_state.configure(text=obj.name, bg="white", fg="black",
                                    state=NORMAL)

        # Configure Header Label
        text = "Game Over ({} Correct / {} Incorrect)".format(
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
                                  font=("Arial", "12", "bold"),
                                  fg="black",
                                  justify=CENTER)
        self.ent_username.grid(row=1)

        # Close Button (Column 2)
        self.btn_close = Button(self.frm_header_widgets,
                                text="Quit without\n"
                                     "Saving",
                                font=("Arial", "11", "bold"),
                                width=10, height=2,
                                padx=1, pady=1,
                                command=self.fnc_g_close)
        self.btn_close.grid(row=0, column=2, sticky=E)

    # Save Results Function
    def fnc_save_results(self):
        from datetime import date
        # Get Username
        self.username = self.ent_username.get()
        # Get Today's Date
        self.today = date.today()
        # Check if Username
        if not self.username:  # If not
            self.ent_username.configure(fg="red")
            self.ent_username.insert(0, 'Required')
            self.ent_username.bind("<FocusIn>", lambda args: self.ent_username.delete('0', 'end'))  # Emphasize entry box
            return  # End Function
        # Create list for storing Username and Tally
        self.append_row = [self.username, self.lst_tally[0], self.lst_tally[1], self.today]
        # Write to a csv file
        from csv import writer
        # open the file in the append mode
        with open('SUS_Saved_Results.csv', 'a', newline='',
                  encoding='utf-8-sig') as f_object:
            # create the csv writer
            writer_object = writer(f_object)

            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(self.append_row)
            # Close the file object
            f_object.close()

        # Destroy game window
        self.fnc_g_close()

        self.fnc_get_save_message()

    # Display Save Success Message
    def fnc_get_save_message(self):
        message_text = "Results Saved: \n" \
                       "{} ({} Correct /{} Incorrect), {}". \
            format(self.username, self.lst_tally[0], self.lst_tally[1], self.today)
        mb = Message_Box("Save Successful", message_text, "", "")

    # Close Window Function
    def fnc_g_close(self):
        # Re-enable Help Button
        self.menu.btn_m_game.configure(state=NORMAL)
        # Close Window
        self.box_g.destroy()


# State Class
class State:

    def __init__(self, window, game_function, name, capital, row, column):

        # Define Variables to be accessed for questions
        self.name = name
        self.capital = capital

        # State Button
        self.btn_state = Button(window.frm_cartogram,
                                text=self.name,
                                fg="white",
                                font=("Arial", "6", "bold"),
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
                    # Generate Internal Results
                    self.obj_game.fnc_internal_results("Incorrect", "red")


# Main Routine

if __name__ == "__main__":
    root = Tk()
    root.title("The States of the United States")
    root.iconbitmap('SUS_Logo.ico')
    main_window = Menu()
    root.mainloop()
