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

        ## Initialize root of TK and define parameter options
        self.master = Tk()
        self.master.title("NBA Record Searcher")
        self.master.geometry("800x500")
        self.master.configure(bg="lightgray")
        self.stats_options = ['PTS', 'FTM', 'FGM', 'AST', 'BLK', 'REB', 'STL']
        self.stats_type_options = ['1 Game', 'Number of Times']

        ## Split into 2 different tabs
        self.tabControl = ttk.Notebook(self.master) 
        self.one_game_tab = ttk.Frame(self.tabControl) 
        self.num_time_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.one_game_tab, text ='Single Game') 
        self.tabControl.add(self.num_time_tab, text ='Number of Times') 
        self.tabControl.pack(expand = 1, fill ="both") 




        ## Tab 1: Single Game


        ## title label
        self.title_label = Label(self.one_game_tab, text="Select Statistic")  
        self.title_label.config(font =("Courier", 14))
        self.title_label.grid(row=0, column=0, columnspan=4,pady=5)

        ## create variable for stat selected
        self.selected_stat1 = IntVar() 
        self.selected_stat1.set(2)

        ## create button for each option
        for index, stat in enumerate(self.stats_options):
            button = Radiobutton(self.one_game_tab, text=stat,
                                 variable=self.selected_stat1, value=index,
                                 height=2, width=8)
            row = 2  
            column = index
            button.grid(row=row, column=column, sticky='w')


        ## label for Start/End year
        self.year_started_label = Label(self.one_game_tab, text="Start Year")  
        self.year_started_label.config(font =("Courier", 14))
        self.year_started_label.grid(row=3, column=0, columnspan=4,pady=5, padx=5)

        self.year_ended_label = Label(self.one_game_tab, text="End Year")  
        self.year_ended_label.config(font =("Courier", 14))
        self.year_ended_label.grid(row=3, column=2, columnspan=4,pady=5, padx=5)

        ## entry for Start/End dates
        if self.stats_options[self.selected_stat1.get()] == 'AST': ## updates initial date in DateEntry on selected stat
            self.year_started1 = DateEntry(self.one_game_tab, locale='en_US', date_pattern='yyyy-mm-dd', year = 1970, month = 1, day = 1)
        elif self.stats_options[self.selected_stat1.get()] == 'BLK' or self.stats_options[self.selected_stat1.get()] == 'STL':
            self.year_started1 = DateEntry(self.one_game_tab, locale='en_US', date_pattern='yyyy-mm-dd', year = 1974, month = 1, day = 1)
        else:
            self.year_started1 = DateEntry(self.one_game_tab, locale='en_US', date_pattern='yyyy-mm-dd', year = 1946, month = 11, day = 1)
        self.year_started1.grid(row=4, column=0, columnspan=4, pady=5, padx=5)
        self.year_ended1 = DateEntry(self.one_game_tab, locale='en_US', date_pattern='yyyy-mm-dd',
                                    year = data_processor.last_update.year, month = data_processor.last_update.month, day = data_processor.last_update.day)
        self.year_ended1.grid(row=4, column=2, columnspan=4, pady=5, padx=5)

        # Search button
        self.find_button = Button(self.one_game_tab, text="Find", command=self.execute_search_tab1)
        self.find_button.grid(row=5, column=0, columnspan=1, pady=5) 



        ## Tab 2: Number of Times
        
        # Select Statistic Label
        self.title_label = Label(self.num_time_tab, text="Select Statistic")  
        self.title_label.config(font =("Courier", 14))
        self.title_label.grid(row=0, column=0, columnspan=4,pady=5)

        # selected statistic variable
        self.selected_stat2 = IntVar() 
        self.selected_stat2.set(-4)

        # buttons for each stat
        for index, stat in enumerate(self.stats_options):
            button = Radiobutton(self.num_time_tab, text=stat,
                                 variable=self.selected_stat2, value=index,
                                 height=2, width=8)
            row = 1  
            column = index
            button.grid(row=row, column=column, sticky='w')

        # label for stat cutoff
        self.title_label = Label(self.num_time_tab, text="Input Stat Cutoff")  
        self.title_label.config(font =("Courier", 14))
        self.title_label.grid(row=3, column=0, columnspan=6,pady=5)

        # entry for stat cutoff
        self.stat_cutoff = Entry(self.num_time_tab)
        self.stat_cutoff.grid(row=4, column=0, columnspan=6, pady=5)

        # labels for start/end year
        self.year_started_label = Label(self.num_time_tab, text="Start Year")  
        self.year_started_label.config(font =("Courier", 14))
        self.year_started_label.grid(row=5, column=0, columnspan=6,pady=5, padx=5)

        self.year_ended_label = Label(self.num_time_tab, text="End Year")  
        self.year_ended_label.config(font =("Courier", 14))
        self.year_ended_label.grid(row=5, column=2, columnspan=6,pady=5, padx=5)

        # entry for start/end dates
        if self.selected_stat2 == -1: ## similar to tab1
            self.year_started2 = DateEntry(self.num_time_tab, locale='en_US', date_pattern='yyyy-mm-dd', year = 1946, month = 11, day = 1)
        elif self.stats_options[self.selected_stat2.get()] == 'AST':
            self.year_started2 = DateEntry(self.num_time_tab, locale='en_US', date_pattern='yyyy-mm-dd', year = 1970, month = 1, day = 1)
        elif self.stats_options[self.selected_stat2.get()] == 'BLK' or self.stats_options[self.selected_stat2.get()] == 'STL':
            self.year_started2 = DateEntry(self.num_time_tab, locale='en_US', date_pattern='yyyy-mm-dd', year = 1974, month = 1, day = 1)
        self.year_started2.grid(row=6, column=0, columnspan=4, pady=5, padx=5)
        self.year_ended2 = DateEntry(self.num_time_tab, locale='en_US', date_pattern='yyyy-mm-dd',
                                    year = data_processor.last_update.year, month = data_processor.last_update.month, day = data_processor.last_update.day)
        self.year_ended2.grid(row=6, column=2, columnspan=4, pady=5, padx=5)

        # Search button
        self.find_button = Button(self.num_time_tab, text="Find", command=self.execute_search_tab2)
        self.find_button.grid(row=7, column=0, columnspan=1, pady=5)
        
        # Reference to the searcher object
        self.searcher = searcher
        # Run the GUI
        self.master.mainloop()

    ## search in tab1
    def execute_search_tab1(self):
        stat = self.stats_options[self.selected_stat1.get()]
        from_year = self.year_started1.get_date()
        to_year = self.year_ended1.get_date()
        if stat == -1:
            print("Please select a statistic")
        print(self.searcher.get_most_stat_in1game_in_range(from_year, to_year, stat))

    ## search in tab2
    def execute_search_tab2(self):
        try:
            cutoff = int(self.stat_cutoff.get())
        except Exception:
            self.cutoff_errors()
            return
        stat = self.stats_options[self.selected_stat2.get()]
        if stat == -1:
            print("Please select a statistic")
        try:
            from_year = self.year_started2.get_date()
            to_year = self.year_ended2.get_date()
        except OverflowError:
            print("Invalid Dates")
        try:
            print(self.searcher.get_num_times_stat_achieved_in_range(from_year, to_year, stat, cutoff))
        except Exception:
            self.cutoff_errors()
            return

    ## catch errors with invalid cutoffs
    def cutoff_errors(self):
        print("Invalid cutoff, please input a number")



