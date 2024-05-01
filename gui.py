################################################################
## This file is responsible for the GUI
################################################################
from searcher import Searcher
from data_processor import DataProcessor
from tkinter import *
from tkcalendar import DateEntry

class GUI:
    def __init__(self, searcher, data_processor):
        self.master = Tk()
        self.master.title("NBA Record Searcher")
        self.master.geometry("800x500")
        self.master.configure(bg="lightgray")
        self.stats_options = ['PTS', 'FTM', 'FGM', 'AST', 'BLK', 'REB', 'STL']
        self.stats_type_options = ['1 Game', 'Number of Times']

        self.title_label = Label(self.master, text="Select Statistic")  
        self.title_label.config(font =("Courier", 14))
        self.title_label.grid(row=0, column=0, columnspan=4,pady=5)

        self.stat_type = IntVar()
        for index, stat in enumerate(self.stats_type_options):
            button =Radiobutton(self.master, text=stat,
                                variable=self.stat_type, value=index, 
                                height=2, width=12, sticky='w')
            row=1
            column=index
            button.grid(row=row, column=column)

        self.selected_stat = IntVar() 
        for index, stat in enumerate(self.stats_options):
            button = Radiobutton(self.master, text=stat,
                                 variable=self.selected_stat, value=index,
                                 height=2, width=8)
            row = 2  
            column = index
            button.grid(row=row, column=column, sticky='w')

        self.year_started_label = Label(self.master, text="Start Year")  
        self.year_started_label.config(font =("Courier", 14))
        self.year_started_label.grid(row=3, column=0, columnspan=4,pady=5, padx=5)

        self.year_ended_label = Label(self.master, text="End Year")  
        self.year_ended_label.config(font =("Courier", 14))
        self.year_ended_label.grid(row=3, column=2, columnspan=4,pady=5, padx=5)
        if self.stats_options[self.selected_stat.get()] == 'AST':
            self.year_started = DateEntry(self.master, locale='en_US', date_pattern='yyyy-mm-dd', year = 1970, month = 1, day = 1)
        elif self.stats_options[self.selected_stat.get()] == 'BLK' or self.stats_options[self.selected_stat.get()] == 'STL':
            self.year_started = DateEntry(self.master, locale='en_US', date_pattern='yyyy-mm-dd', year = 1974, month = 1, day = 1)
        else:
            self.year_started = DateEntry(self.master, locale='en_US', date_pattern='yyyy-mm-dd', year = 1946, month = 11, day = 1)
        self.year_started.delete(0, "end")  ## Only this line needed to be added to clear the field.
        self.year_started.grid(row=4, column=0, columnspan=4, pady=5, padx=5)
        self.year_ended = DateEntry(self.master, locale='en_US', date_pattern='yyyy-mm-dd',
                                    year = data_processor.last_update.year, month = data_processor.last_update.month, day = data_processor.last_update.day)
        self.year_ended.delete(0, "end")  ## Only this line needed to be added to clear the field.
        self.year_ended.grid(row=4, column=2, columnspan=4, pady=5, padx=5)

        # Search button
        self.find_button = Button(self.master, text="Find", command=self.execute_search)
        self.find_button.grid(row=5, column=0, columnspan=1, pady=5)  # Span across two columns

        # Reference to the searcher object
        self.searcher = searcher
        self.master.mainloop()

    def execute_search(self):
        stat_type = self.stats_type_options[self.stat_type.get()]
        stat = self.stats_options[self.selected_stat.get()]
        from_year = self.year_started.get_date()
        to_year = self.year_ended.get_date()
        print(stat)
        print(from_year)
        print(to_year)
        if stat:
            print(self.searcher.get_most_stat_in1game_in_range(from_year, to_year, stat))
        else:
            print(self.searcher.)

        # self.searcher.find(stat, from_year, to_year)


