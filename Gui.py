"""
Program: Gui.py
Author: Shiqi Wang
Last date modified: 12/12/2020

The purpose of this program is to write a gui interface to play anagram
"""
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import ctypes
from Database import Database
from Anagram import Anagram, EmptyFileError
from datetime import datetime


class Gui(tk.Tk):
    """A tkinter class"""
    def __init__(self):
        """Initialize class anagram and database,
        also create all components of the gui.
        """
        super().__init__()
        self.database = Database("history_log.db")
        self.database.create_table()
        self.anagram = Anagram()
        self.filename = None
        self.dict_file = None

        file_frame = Frame(self)
        file_frame.grid(row=0, column=0)

        self.btn_open_file = Button(file_frame, width=16, text="Choose local file",
                                     command=lambda: self.open_file())
        self.btn_open_file.pack(side=LEFT, padx=10, pady=10)

        self.text_filename = Text(file_frame, height=1, state=DISABLED)
        self.text_filename.pack(side=LEFT, padx=10, pady=10)

        self.btn_submit_file = Button(file_frame, width=16, text="Submit",
                                       command=lambda: self.submit_data())
        self.btn_submit_file.pack(side=LEFT, padx=10, pady=10)

        searching_frame = Frame(self)
        searching_frame.grid(row=1, column=0)

        self.label_input = Label(searching_frame, text="Input one word: ", fg='blue', font=("Helvetica", 12))
        self.label_input.pack(side=LEFT, padx=10, pady=10)
        self.input = Entry(searching_frame)
        self.input.pack(side=LEFT, padx=10, pady=10)
        self.btn_search_anagram = Button(searching_frame, width=16, text="Searching Anagram",
                                         command=lambda: self.searching_anagram())
        self.btn_search_anagram.pack(side=LEFT, padx=10, pady=10)

        database_frame = Frame(self)
        database_frame.grid(row=2, column=0)
        self.label_database = Label(database_frame, text="Search history input word: ", fg='blue', font=("Helvetica", 12))
        self.label_database.pack(side=LEFT, padx=10, pady=10)
        self.database_input = Entry(database_frame)
        self.database_input.pack(side=LEFT, padx=10, pady=10)
        self.btn_search_database = Button(database_frame, width=28, text="Searching History Word",
                                          command=lambda: self.searching_database())
        self.btn_search_database.pack(side=LEFT, padx=10, pady=10)

        process_frame = Frame(self.master)
        process_frame.grid(row=0, column=1, rowspan=4, sticky=W + E + N + S)
        self.text_process = Text(process_frame, state=DISABLED)
        self.text_process.pack(fill=BOTH, expand=True)

    def open_file(self):
        """get filename from text_filename section
        :return: None
        """
        self.filename = filedialog.askopenfilename()
        self.text_filename.config(state=NORMAL)
        self.text_filename.insert(END, self.filename)
        self.text_filename.config(state=DISABLED)

    def submit_data(self):
        """let instance anagram read data from the file
        and handling all kinds inappropriate using
        :return: None
        """
        self.dict_file = self.filename
        try:
            self.anagram.read_file(self.dict_file)
        except (FileNotFoundError, EmptyFileError) as e:
            self.dict_file = None
            self.show_message(str(e))
        self.show_message("File submit success!")

    def searching_anagram(self):
        """Find anagram list based on user input word,
        also put the searching record into the database
        :return: None
        """
        if self.dict_file is None:
            self.show_message("Please select a file first (don't forget to press submit button)!")
            return
        try:
            word = self.anagram.preprocess_word(self.input.get())
        except ValueError as e:
            self.show_message(str(e))
            return

        res = self.anagram.find_anagram_list(word)
        if res is None:
            self.show_message(f"word '{word}' does not exist in the dictionary.")
        elif not res:
            self.show_message(f"word '{word}' anagram in the dictionary is itself.")
        else:
            self.show_message(f"word '{word}' anagram: {res}")
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = (time, word, str(res))
        self.database.create_record(record)

    def searching_database(self):
        """Searching history finding based on the user input word
        :return: None
        """
        try:
            word = self.anagram.preprocess_word(self.database_input.get())
        except ValueError as e:
            self.show_message(str(e))
            return
        rows = self.database.select_record_by_word(word)
        res = f"The history of word '{word}': \n"
        for row in rows:
            res += str(row[1:]) + '\n'

        self.show_message(res)

    def show_message(self, msg):
        """Show the message in certain format in the text field
        :param str msg: input message
        :return: None
        """
        msg = msg + '\n' + '-' * 20 + '\n'
        self.text_process.config(state=NORMAL)
        self.text_process.insert(END, msg + '\n')
        self.text_process.config(state=DISABLED)


if __name__ == '__main__':
    # get higher resolution
    if 'win' in sys.platform:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
    Gui().mainloop()

