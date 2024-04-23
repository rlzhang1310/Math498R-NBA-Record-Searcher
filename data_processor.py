import pandas as pd
from datetime import time
import nba_api
import requests
################################################################
## Add missing data with this if necessary
################################################################

class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.data['GAME_DATE'] = pd.to_datetime(self.data['GAME_DATE'])
        self.last_update = self.data['GAME_DATE'].max()
        print(self.last_update)

    def update(self):
        ## updates new data from the previous update
        return
    

    def retry(func, retries=6):
        def retry_wrapper(*args, **kwargs):
            wait = 0.05
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    print(e)
                time.sleep(wait)
                wait *= 2
                attempts += 1
        return retry_wrapper