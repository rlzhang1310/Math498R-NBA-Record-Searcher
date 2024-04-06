import pandas as pd
import numpy as np

################################################################
## Searcher file where the querying will be performed
################################################################

class Searcher:
    def __init__(self, data):
        self.data = data


    def search_max_score(self, from_year=1946, to_year=9999):
        df_filter_year = self.data.query(f"Season >= {from_year} & Season <= {to_year}")
        max_score = df_filter_year["PTS"].max()
        query_df = df_filter_year.query(f"PTS >= {max_score}")
        return query_df[["Season", "PLAYER_NAME", "Team", "GAME_DATE", "MATCHUP", "WL", "PTS"]]