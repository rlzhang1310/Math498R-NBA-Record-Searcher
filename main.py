import pandas as pd
import numpy as np
from searcher import Searcher
from data_processor import DataProcessor
from gui import GUI
################################################################
## Main file to run everything in
################################################################

def main():
    data = pd.read_csv("/root/Math498R-NBA-Record-Searcher/data/NBA Player Box Score Stats(1950 - 2022).csv")
    data_processor = DataProcessor(data)
    searcher = Searcher(data)
    # print(searcher.get_num_times_stat_achieved_in_range('2000','2010', ['AST', 'BLK'], [10, 2]))
    print(searcher.get_most_stat_in1game_in_range('2000','2010',['AST','BLK']))
    app = GUI(searcher, data_processor)

if __name__ == "__main__":
    main()


    # data = pd.read_csv("/Users/rlzhang1310/Coding/MATH498R/Math498R-NBA-Record-Searcher/data/NBA Player Box Score Stats(1950 - 2022).csv")
    # data = pd.read_csv('/home/tristen/MATH498R/Math498R-NBA-Record-Searcher/data/NBA Player Box Score Stats(1950 - 2022).csv')
