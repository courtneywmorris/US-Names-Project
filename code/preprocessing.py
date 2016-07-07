import pandas as pd

# filename = '../../StateNames.csv'
# dataframe = pd.read_csv(filename)

class InputFrame(object):
    def __init__(self,dataframe,gender):
        self.dataframe = dataframe
        self.gender = gender
        self.gender_frame = None

    def clean_data_from_frame(self):
        gender_frame = self.dataframe[self.dataframe['Gender']==self.gender].set_index(['Year','State'])
        # gender_frame = gender_frame.set_index(['Year','State'])
        gender_frame['tuple_index'] = gender_frame.index.values
        self.gender_frame = pd.pivot_table(gender_frame, values = 'Count',
        index = 'tuple_index', columns= 'Name').fillna(0)

    ###Have a method for cleaning input data?
    def clean_input_data(self):
        self.dataframe
# if __name__ == "___main___":
