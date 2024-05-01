################################################################
## This file is responsible for the GUI
################################################################
from searcher import Searcher
from data_processor import DataProcessor
from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk 

class GUI:
    def __init__(self, searcher, data_processor):
        self.master = Tk()
        self.master.title("NBA Record Searcher")
        self.master.geometry("800x500")
        self.master.configure(bg="lightgray")
        self.stats_options = ['PTS', 'FTM', 'FGM', 'AST', 'BLK', 'REB', 'STL']
        self.stats_type_options = ['1 Game', 'Number of Times']

        self.tabControl = ttk.Notebook(self.master) 
        self.one_game_tab = ttk.Frame(self.tabControl) 
        self.num_time_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.one_game_tab, text ='Single Game') 
        self.tabControl.add(self.num_time_tab, text ='Number of Times') 
        self.tabControl.pack(expand = 1, fill ="both") 

        ## Tab 1: Single Game

        self.title_label = Label(self.one_game_tab, text="Select Statistic")  
        self.title_label.config(font =("Courier", 14))
        self.title_label.grid(row=0, column=0, columnspan=4,pady=5)

        self.selected_stat = IntVar() 
        for index, stat in enumerate(self.stats_options):
            button = Radiobutton(self.one_game_tab, text=stat,
                                 variable=self.selected_stat, value=index,
                                 height=2, width=8)
            row = 2  
            column = index
            button.grid(row=row, column=column, sticky='w')

        self.year_started_label = Label(self.one_game_tab, text="Start Year")  
        self.year_started_label.config(font =("Courier", 14))
        self.year_started_label.grid(row=3, column=0, columnspan=4,pady=5, padx=5)

        self.year_ended_label = Label(self.one_game_tab, text="End Year")  
        self.year_ended_label.config(font =("Courier", 14))
        self.year_ended_label.grid(row=3, column=2, columnspan=4,pady=5, padx=5)
        if self.stats_options[self.selected_stat.get()] == 'AST':
            self.year_started = DateEntry(self.one_game_tab, locale='en_US', date_pattern='yyyy-mm-dd', year = 1970, month = 1, day = 1)
        elif self.stats_options[self.selected_stat.get()] == 'BLK' or self.stats_options[self.selected_stat.get()] == 'STL':
            self.year_started = DateEntry(self.one_game_tab, locale='en_US', date_pattern='yyyy-mm-dd', year = 1974, month = 1, day = 1)
        else:
            self.year_started = DateEntry(self.one_game_tab, locale='en_US', date_pattern='yyyy-mm-dd', year = 1946, month = 11, day = 1)
        self.year_started.delete(0, "end")  ## Only this line needed to be added to clear the field.
        self.year_started.grid(row=4, column=0, columnspan=4, pady=5, padx=5)
        self.year_ended = DateEntry(self.one_game_tab, locale='en_US', date_pattern='yyyy-mm-dd',
                                    year = data_processor.last_update.year, month = data_processor.last_update.month, day = data_processor.last_update.day)
        self.year_ended.delete(0, "end")  ## Only this line needed to be added to clear the field.
        self.year_ended.grid(row=4, column=2, columnspan=4, pady=5, padx=5)

        # Search button
        self.find_button = Button(self.one_game_tab, text="Find", command=self.execute_search_tab1)
        self.find_button.grid(row=5, column=0, columnspan=1, pady=5)  # Span across two columns


        ## Tab 2: Number of Times
        
        self.title_label = Label(self.num_time_tab, text="Select Statistic")  
        self.title_label.config(font =("Courier", 14))
        self.title_label.grid(row=0, column=0, columnspan=4,pady=5)

        self.selected_stat = IntVar() 
        for index, stat in enumerate(self.stats_options):
            button = Radiobutton(self.num_time_tab, text=stat,
                                 variable=self.selected_stat, value=index,
                                 height=2, width=8)
            row = 2  
            column = index
            button.grid(row=row, column=column, sticky='w')
        self.title_label = Label(self.num_time_tab, text="Input Stat Cutoff")  
        self.title_label.config(font =("Courier", 14))
        self.title_label.grid(row=3, column=0, columnspan=4,pady=5)

        self.stat_cutoff = Entry(self.num_time_tab)
        self.stat_cutoff.grid(row=4, column=0, pady=5)

        self.year_started_label = Label(self.num_time_tab, text="Start Year")  
        self.year_started_label.config(font =("Courier", 14))
        self.year_started_label.grid(row=5, column=0, columnspan=4,pady=5, padx=5)

        self.year_ended_label = Label(self.num_time_tab, text="End Year")  
        self.year_ended_label.config(font =("Courier", 14))
        self.year_ended_label.grid(row=5, column=2, columnspan=4,pady=5, padx=5)
        if self.stats_options[self.selected_stat.get()] == 'AST':
            self.year_started = DateEntry(self.num_time_tab, locale='en_US', date_pattern='yyyy-mm-dd', year = 1970, month = 1, day = 1)
        elif self.stats_options[self.selected_stat.get()] == 'BLK' or self.stats_options[self.selected_stat.get()] == 'STL':
            self.year_started = DateEntry(self.num_time_tab, locale='en_US', date_pattern='yyyy-mm-dd', year = 1974, month = 1, day = 1)
        else:
            self.year_started = DateEntry(self.num_time_tab, locale='en_US', date_pattern='yyyy-mm-dd', year = 1946, month = 11, day = 1)
        self.year_started.delete(0, "end")  ## Only this line needed to be added to clear the field.
        self.year_started.grid(row=6, column=0, columnspan=4, pady=5, padx=5)
        self.year_ended = DateEntry(self.num_time_tab, locale='en_US', date_pattern='yyyy-mm-dd',
                                    year = data_processor.last_update.year, month = data_processor.last_update.month, day = data_processor.last_update.day)
        self.year_ended.delete(0, "end")  ## Only this line needed to be added to clear the field.
        self.year_ended.grid(row=6, column=2, columnspan=4, pady=5, padx=5)

        # Search button
        self.find_button = Button(self.num_time_tab, text="Find", command=self.execute_search_tab2)
        self.find_button.grid(row=7, column=0, columnspan=1, pady=5)
        # Reference to the searcher object
        self.searcher = searcher
        self.master.mainloop()

    def execute_search_tab1(self):
        stat = self.stats_options[self.selected_stat.get()]
        from_year = self.year_started.get_date()
        to_year = self.year_ended.get_date()
        print(stat)
        print(from_year)
        print(to_year)
        print(self.searcher.get_most_stat_in1game_in_range(from_year, to_year, stat))

    def execute_search_tab2(self):
        try:
            cutoff = int(self.stat_cutoff.get())
        except TypeError:
            print("Invalid cutoff, please input a number")
        stat = self.stats_options[self.selected_stat.get()]
        from_year = self.year_started.get_date()
        to_year = self.year_ended.get_date()
        print(stat)
        print(from_year)
        print(to_year)
        print(self.searcher.get_num_times_stat_achieved_in_range(from_year, to_year, stat, cutoff))


        # self.searcher.find(stat, from_year, to_year)


