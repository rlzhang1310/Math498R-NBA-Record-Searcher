import pandas as pd
import numpy as np
from searcher import Searcher

################################################################
## Main file to run everything in
################################################################

def main():
    data = pd.read_csv('nba_data/NBA Player Box Score Stats(1950 - 2022).csv')
    searcher = Searcher(data)
    print(searcher.search_max_score(1963))
if __name__ == "__main__":
    main()


