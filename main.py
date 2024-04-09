import pandas as pd
import numpy as np
from searcher import Searcher

################################################################
## Main file to run everything in
################################################################

def main():
    data = pd.read_csv('data/NBA Player Box Score Stats(1950 - 2022).csv')
    searcher = Searcher(data)
    # print(searcher.search_max_score(1963))
    # print(searcher.get_most_ftm_in1game_in_range('2000', '2022'))
    print(searcher.get_most_fgm_in1game_in_range('2000', '2022'))

if __name__ == "__main__":
    main()


