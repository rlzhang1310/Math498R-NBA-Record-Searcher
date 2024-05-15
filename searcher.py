import pandas as pd
import numpy as np

################################################################
## Searcher file where the querying will be performed
################################################################

class Searcher:
    def __init__(self, data):
        self.data = data

    def get_most_stat_in1game_in_range(self, start, end, stats):
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        if start > end:
            print("End date less than start date")
            return
        date_range = pd.date_range(start, end)
        try:
            query_df = self.data[self.data['GAME_DATE'].isin(date_range)]
            res_df = pd.DataFrame()
            for stat in stats: # iterate each stat
                max_in_game = query_df[stat].max() # get max
                players_with_max = query_df.loc[query_df[stat] == max_in_game]
                players_with_max = players_with_max[["Season", "PLAYER_NAME", "Team", "GAME_DATE", "MATCHUP", "WL", stat]]
                res_df = pd.concat([players_with_max, res_df]) # add to final dataframe that we return

            # return players_with_max['PLAYER_NAME'].unique()
            result = res_df[["Season", "PLAYER_NAME", "Team", "GAME_DATE", "MATCHUP", "WL"]+stats]
            if len(result) == 0:
                print("Does not exist within specified parameters")
                return
            else:
                return result
        except KeyError:
            self.stat_does_not_exist_errors(stat)

    def get_num_times_stat_achieved_in_range(self, start, end, stats, numbers):
        if len(stats) != len(numbers):
            return 'ERROR: lists must be same size'
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        if start > end:
            print("End date less than start date")
            return
        Date_range = pd.date_range(start, end)
        try:
            df = self.data[self.data['GAME_DATE'].isin(Date_range)]
            cur_stat = '' # keep track of current stat being filtered
            for i in range(2): # iterably filter df
                df = df.loc[df[stats[i]] == numbers[i]]
                cur_stat = stats[i]
            if len(df) == 0:
                print("Does not exist within specified parameters")
                return      
            else:          
                print(df[["Season", "PLAYER_NAME", "Team", "GAME_DATE", "MATCHUP", "WL"]+stats])
                return len(df)        
        except KeyError:
            self.stat_does_not_exist_errors(cur_stat)
    
    def stat_does_not_exist_errors(self, stat):
        if stat == 'AST':
            print(f"AST Stat not recorded until 1946-1947 Season")
        elif stat == 'BLK':
            print(f"BLK Stat not recorded until 1973-1974 Season")
        elif stat == 'STL':
            print(f"BLK Stat not recorded until 1973-1974 Season")
        else:
            print(f"{stat} has unknown error, check your parameters again")
            
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






    # def get_num_times_fgm_achieved_in_range(self, fgm, start, end) :
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     df = self.data[self.data['GAME_DATE'].isin(range)]
    #     num = df.loc[self.data['FGM'] >= fgm]
    #     return len(num)
    
    # def get_num_times_ftm_achieved_in_range(self, ftm, start, end) :
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     df = self.data[self.data['GAME_DATE'].isin(range)]
    #     num = df[self.data['FTM'] >= ftm]
    #     return len(num)
    
    # def get_num_times_ast_achieved_in_range(self, ast, start, end):
    #     # filter out non-tracked years
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     df = self.data.loc[(self.data['GAME_DATE'] >= '1970-01-01')]
    #     df = df[df['GAME_DATE'].isin(range)]
    #     num = df.loc[df['AST'] >= ast]
    #     return len(num)
    
    # def get_num_times_blk_achieved_in_range(self, blk, start, end):
    #     # filter out non-tracked years
    #     df = self.data.loc[(self.data['GAME_DATE'] >= '1974-01-01')]
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     df = df[df['GAME_DATE'].isin(range)]
    #     num = df.loc[df['BLK'] >= blk]
    #     return len(num)
    
    # def get_num_times_reb_achieved(self, reb):
    #     # filter out non-tracked years
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     df = self.data[self.data['GAME_DATE'].isin(range)]
    #     num = df[self.data['REB'] >= reb]
    #     return len(num)
    
    # def get_num_times_stl_achieved(self, stl):
    #     # filter out non-tracked years
    #     df = self.data.loc[(self.data['GAME_DATE'] >= '1974-01-01')]
    #     start = pd.to_datetime(start)
    #     end = pd.to_datetime(end)
    #     range = pd.date_range(start, end)
    #     df = df[df['GAME_DATE'].isin(range)]
    #     num = df.loc[df['STL'] >= stl]
    #     return len(num)
