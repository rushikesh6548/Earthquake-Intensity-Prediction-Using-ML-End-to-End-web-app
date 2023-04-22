import os
import sys

import numpy as np

from src.exception import CustomException
from src.logger import logging
from src.utils import getting_data_as_df,get_all_data_from_api
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
import requests

import geopy
from datetime import datetime


class DataPreprocessingConfig:
    def __init__(self):
        self.raw_data_path = os.path.join('raw_data_From_api', 'alldata.csv')


class DataPreprocessing:
    def __init__(self):
        data_object = DataPreprocessingConfig()
        self.raw_data_path  = data_object.raw_data_path
        self.raw_data_imputed_df = pd.DataFrame()
        self.final_ready_data_df  = pd.DataFrame()

    def initiate_data_preprocessing(self):
        raw_data_df = pd.read_csv(self.raw_data_path, header=0,encoding='utf-8',encoding_errors='ignore')

        logging.info("Got the data as dataframe and initiating Data preprocessing")

        # As from Performing EDA we know we will only keep the following features and perform feature engineering based on insights

        raw_data_df = raw_data_df[['time','latitude','longitude','gap','dmin','mag']]

        print(raw_data_df)
        # here, Knn imputer can be applied

        raw_data_df['latitude'] = raw_data_df['latitude'].astype(dtype='float64')
        raw_data_df['longitude'] = raw_data_df['longitude'].astype(dtype='float64')
        raw_data_df['gap'] = raw_data_df['gap'].astype(dtype='float64')
        raw_data_df['dmin'] = raw_data_df['dmin'].astype(dtype='float64')
        raw_data_df['mag'] = raw_data_df['mag'].astype(dtype='float64')

        temp_df = raw_data_df[['latitude','longitude','gap','dmin','mag']]

        knn = KNNImputer(n_neighbors=50)




        print(f"Temp df : \n {temp_df}")



        temp_df_imputed = knn.fit_transform(temp_df)


        print(f"Temp df imputed : {temp_df_imputed}")




        self.raw_data_imputed_df = temp_df_imputed
        self.raw_data_imputed_df = pd.DataFrame(self.raw_data_imputed_df, columns=['latitude','longitude','gap','dmin','mag'])

        self.raw_data_imputed_df.insert(0,'time',raw_data_df['time'])


        print(self.raw_data_imputed_df)







    def do_feature_engineering(self):
        # We have The time feature that we can use to get much more information !
        #
        print(self.raw_data_imputed_df.info())
        self.raw_data_imputed_df['time'] = pd.to_datetime(self.raw_data_imputed_df['time'])
        #

        #
        # # We get a column named Quarter of year from our time column!
        # # Based on research we see there is a slight affect of earthquakes based on the season!
        #
        def get_quarter_of_year(x):
             quarter = x.quarter
             return quarter
        #
        def get_month(x):
             month = x.month
             return month

        def get_day_of_month(x):
             day = x.day
             return day
        #
        self.final_ready_data_df = self.raw_data_imputed_df
        self.final_ready_data_df['quarter_of_year']  = self.raw_data_imputed_df['time'].apply(get_quarter_of_year)

        self.final_ready_data_df['month_of_year'] = self.raw_data_imputed_df['time'].apply(get_month)
        self.final_ready_data_df['day_of_month'] = self.raw_data_imputed_df['time'].apply(get_day_of_month)


        final_data_save_path = os.path.join('artifacts','final_data2.csv')
        self.final_ready_data_df.to_csv(final_data_save_path,header=True , encoding='utf-8')

        print(self.final_ready_data_df.head(100))

        logging.info(f"Saved the Final file with no missing values in final_data.csv in {final_data_save_path}")





obj = DataPreprocessing()
obj.initiate_data_preprocessing()
obj.do_feature_engineering()