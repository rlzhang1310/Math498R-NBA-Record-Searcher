import pandas as pd

################################################################
## Add missing data with this if necessary
################################################################

class Data_Processor:
    def __init__(self, data):
        self.data = data


    def update(self, last_update, cur_time):
        ## updates new data from the previous update
        return