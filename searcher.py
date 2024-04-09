import pandas as pd
import numpy as np

################################################################
## Searcher file where the querying will be performed
################################################################

class Searcher:
    def __init__(self, data):
        self.data = data
        self.data['GAME_DATE'] = pd.to_datetime(self.data['GAME_DATE'])


    def search_max_score(self, from_year=1946, to_year=9999):
        df_filter_year = self.data.query(f"Season >= {from_year} & Season <= {to_year}")
        max_score = df_filter_year["PTS"].max()
        query_df = df_filter_year.query(f"PTS >= {max_score}")
        return query_df[["Season", "PLAYER_NAME", "Team", "GAME_DATE", "MATCHUP", "WL", "PTS"]]
    
    def get_most_ftm_in1game_in_range(self, start, end):
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        range = pd.date_range(start, end)
        self.data = self.data[self.data['GAME_DATE'].isin(range)]
        max_ftm_in_game = self.data['FTM'].max()
        players_with_max = self.data.loc[self.data['FTM'] == max_ftm_in_game]
        return players_with_max['PLAYER_NAME'].unique()
    
    def get_most_fgm_in1game_in_range(self, start, end):
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        range = pd.date_range(start, end)
        self.data = self.data[self.data['GAME_DATE'].isin(range)]
        max_ftm_in_game = self.data['FGM'].max()
        players_with_max = self.data.loc[self.data['FGM'] == max_ftm_in_game]
        return players_with_max['PLAYER_NAME'].unique()