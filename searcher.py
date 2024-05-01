import pandas as pd
import numpy as np

################################################################
## Searcher file where the querying will be performed
################################################################

class Searcher:
    def __init__(self, data):
        self.data = data

    def get_most_stat_in1game_in_range(self, start, end, stat):
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        range = pd.date_range(start, end)
        query_df = self.data[self.data['GAME_DATE'].isin(range)]
        try:
            max_ftm_in_game = query_df[stat].max()
            players_with_max = query_df.loc[query_df[stat] == max_ftm_in_game]
            # return players_with_max['PLAYER_NAME'].unique()
            return players_with_max[["Season", "PLAYER_NAME", "Team", "GAME_DATE", "MATCHUP", "WL", stat]]
        except KeyError:
            print(f"{stat} Stat not recorded in specified timeframe")
    # def get_most_pts_in1game_in_range(self, start=1946, end=9999):
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     query_df = self.data[self.data['GAME_DATE'].isin(range)]
    #     max_ftm_in_game = query_df['PTS'].max()
    #     players_with_max = query_df.loc[query_df['PTS'] == max_ftm_in_game]
    #     # return players_with_max['PLAYER_NAME'].unique()
    #     return players_with_max[["Season", "PLAYER_NAME", "Team", "GAME_DATE", "MATCHUP", "WL", "PTS"]]
    #     # df_filter_year = self.data.query(f"Season >= {from_year} & Season <= {to_year}")
    #     # max_score = df_filter_year["PTS"].max()
    #     # query_df = df_filter_year.query(f"PTS >= {max_score}")
    #     # return query_df[["Season", "PLAYER_NAME", "Team", "GAME_DATE", "MATCHUP", "WL", "PTS"]]
    
    # def get_most_ftm_in1game_in_range(self, start, end):
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     query_df = self.data[self.data['GAME_DATE'].isin(range)]
    #     max_ftm_in_game = query_df['FTM'].max()
    #     players_with_max = query_df.loc[query_df['FTM'] == max_ftm_in_game]
    #     return players_with_max['PLAYER_NAME'].unique()
    
    # def get_most_fgm_in1game_in_range(self, start, end):
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     query_df = self.data[self.data['GAME_DATE'].isin(range)]
    #     max_fgm_in_game = query_df['FGM'].max()
    #     players_with_max = query_df.loc[query_df['FGM'] == max_fgm_in_game]
    #     return players_with_max['PLAYER_NAME'].unique()
    
    # def get_most_ast_in1game_in_range(self, start, end):
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     query_df = self.data[self.data['GAME_DATE'].isin(range)]
    #     max_ast_in_game = query_df['AST'].max()
    #     players_with_max = query_df.loc[query_df['AST'] == max_ast_in_game]
    #     return players_with_max['PLAYER_NAME'].unique()
    
    # def get_most_blk_in1game_in_range(self, start, end):
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     query_df = self.data[self.data['GAME_DATE'].isin(range)]
    #     max_blk_in_game = query_df['BLK'].max()
    #     players_with_max = query_df.loc[query_df['BLK'] == max_blk_in_game]
    #     return players_with_max['PLAYER_NAME'].unique()
    
    # def get_most_reb_in1game_in_range(self, start, end):
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     query_df = self.data[self.data['GAME_DATE'].isin(range)]
    #     max_reb_in_game = query_df['REB'].max()
    #     players_with_max = query_df.loc[query_df['REB'] == max_reb_in_game]
    #     return players_with_max['PLAYER_NAME'].unique()
    
    # def get_most_stl_in1game_in_range(self, start, end):
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     query_df = self.data[self.data['GAME_DATE'].isin(range)]
    #     max_stl_in_game = query_df['STL'].max()
    #     players_with_max = query_df.loc[query_df['STL'] == max_stl_in_game]
    #     return players_with_max['PLAYER_NAME'].unique()
    
    # how many times has a stat line been achieved?
    # assists, blocks, shots
    # might not work
    
    def get_num_times_fgm_achieved_in_range(self, fgm, start, end) :
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        range = pd.date_range(start, end)
        df = self.data[self.data['GAME_DATE'].isin(range)]
        num = df.loc[self.data['FGM'] >= fgm]
        return len(num)
    
    def get_num_times_ftm_achieved_in_range(self, ftm, start, end) :
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        range = pd.date_range(start, end)
        df = self.data[self.data['GAME_DATE'].isin(range)]
        num = df[self.data['FTM'] >= ftm]
        return len(num)
    
    def get_num_times_ast_achieved_in_range(self, ast, start, end):
        # filter out non-tracked years
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        range = pd.date_range(start, end)
        df = self.data.loc[(self.data['GAME_DATE'] >= '1970-01-01')]
        df = df[df['GAME_DATE'].isin(range)]
        num = df.loc[df['AST'] >= ast]
        return len(num)
    
    def get_num_times_blk_achieved_in_range(self, blk, start, end):
        # filter out non-tracked years
        df = self.data.loc[(self.data['GAME_DATE'] >= '1974-01-01')]
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        range = pd.date_range(start, end)
        df = df[df['GAME_DATE'].isin(range)]
        num = df.loc[df['BLK'] >= blk]
        return len(num)
    
    def get_num_times_reb_achieved(self, reb):
        # filter out non-tracked years
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        range = pd.date_range(start, end)
        df = self.data[self.data['GAME_DATE'].isin(range)]
        num = df[self.data['REB'] >= reb]
        return len(num)
    
    def get_num_times_stl_achieved(self, stl):
        # filter out non-tracked years
        df = self.data.loc[(self.data['GAME_DATE'] >= '1974-01-01')]
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        range = pd.date_range(start, end)
        df = df[df['GAME_DATE'].isin(range)]
        num = df.loc[df['STL'] >= stl]
        return len(num)
