import os
import sys

import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import getting_data_as_df,get_all_data_from_api
from sklearn.model_selection import train_test_split



class DataIngestionConfig():
    def __init__(self):
        self.train_data_path : str = os.path.join('artifacts','train.csv')
        self.test_data_path : str = os.path.join('artifacts','test.csv')


class DataIngestion():

    def __init__(self):
        data_path_obj = DataIngestionConfig()
        self.train_data_path = data_path_obj.train_data_path
        self.test_data_path = data_path_obj.test_data_path


    def initiate_data_ingestion(self):


        logging.info("Entered Data Ingestion")

    # try :
    # we will read the data from api !
    # To read the data from api we have a function is utils !

    # For the first time we have to run the function : get_all_data_from_api
    # get_all_data_from_api() # This will get all the data from api and save it in a folder

    # Reading the data after getting it from api and preproecssing , feature engineering the data :

        data_path = os.path.join('artifacts','final_data.csv')

        data = pd.read_csv(data_path)

        data = data.drop(['Unnamed: 0','time'],axis = 1 )

        logging.info("Initiating Train Test Split on Data")

        train_data, test_data = train_test_split(data,test_size=0.25,random_state=2)

        train_data.to_csv(self.train_data_path, index=False, header=True)

        test_data.to_csv(self.test_data_path, index=False, header=True)

        logging.info("Train and test data split done and saved to path")


ingestion_obj = DataIngestion()
ingestion_obj.initiate_data_ingestion()
