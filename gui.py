################################################################
## This file is responsible for the GUI
################################################################
from searcher import Searcher
from data_processor import DataProcessor
from tkinter import *

class GUI:
    def __init__(self, searcher):
        self.master = Tk()
        self.master.title("NBA Record Searcher")
        self.master.geometry("800x500")
        self.master.configure(bg="white")

        # Options Label
        title_var = StringVar()
        self.title_label = Label(self.master, text="Select Statistic")  
        title_var.set("Select Statistic")
        self.title_label.config(font =("Courier", 14))
        # Radio button options
        self.stats_options = ['STL', 'BLK', 'PTS', 'AST', 'REB']
        self.title_label.grid(row=0, column=0, columnspan=4,pady=5)
        self.selected_stat = IntVar() 

        for index, stat in enumerate(self.stats_options):
            button = Radiobutton(self.master, text=stat,
                                 variable=self.selected_stat, value=index,
                                 height=2, width=8)
            row = 2  
            column = index
            button.grid(row=row, column=column, sticky='w', pady=5)

        # Search button
        self.find_button = Button(self.master, text="Find", command=self.execute_search)
        self.find_button.grid(row=5, column=0, columnspan=1, pady=5)  # Span across two columns

        # Reference to the searcher object
        self.searcher = searcher
        self.master.mainloop()

    def execute_search(self):
        stat = self.selected_stat.get()
        # from_year = self.from_year_entry.get()
        # to_year = self.to_year_entry.get()
        print(stat)
        # self.searcher.find(stat, from_year, to_year)


