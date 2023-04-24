import os
import sys
import math
import numpy as np
import pandas as pd
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import  Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging

class DataTransformationConfig:
    def __init__(self):
        self.preprocessor_obj_file_path = os.path.join('artifact','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        config_obj = DataTransformationConfig()
        self.preprocessor_obj_file_path = config_obj.preprocessor_obj_file_path

    def initiate_data_transformation(self):

        train_data_path = os.path.join('artifacts','train.csv')
        test_data_path = os.path.join('artifacts','test.csv')

        train_data = pd.read_csv(train_data_path)
        test_data = pd.read_csv(test_data_path)


        train_data_input_features = train_data.drop(['mag'],axis=1)

        train_data_output_feature = train_data['mag']

        test_data_input_features = test_data.drop(['mag'],axis=1)

        test_data_output_feature = test_data['mag']

        # Making preprocessor object :
        # We standardize the numerical columns

        numerical_col_names = ['latitude','longitude','gap','dmin','quarter_of_year','month_of_year','day_of_month']


        transformation = ColumnTransformer(transformers=[
            ('st_scaler',StandardScaler(),numerical_col_names)
        ])

        trained_transformation = transformation.fit(train_data_input_features)


        # saving this transformer object :
        with open(os.path.join('artifacts','transformation.pkl'),'wb') as f:
            pickle.dump(trained_transformation,f)



        # Transforming our Input data :
        train_data_inputs_transformed = trained_transformation.transform(train_data_input_features)
        test_data_inputs_transformed = trained_transformation.transform(test_data_input_features)


        # Transforming our output target column as such :
        # Earthquake Magnitude and intensity is usually given by :
        # Low: Magnitude
        # less
        # than
        # 4.0
        # Moderate: Magnitude
        # between
        # 4.0 and 6.0
        # Strong: Magnitude
        # between
        # 6.0 and 7.0
        # Major: Magnitude
        # between
        # 7.0 and 7.9
        # Great: Magnitude
        # 8.0 or higher

        # Hence we encode them as follows :


        def get_numeric_cat(x):
            if x <= 4.0:
                return 0
            elif x >4.0 and x <= 6.0:
                return 1
            elif x > 6.0 and x <= 7.0:
                return 2
            elif x > 7.0 and x <= 7.9:
                return 3
            elif x > 7.0:
                return 4

        train_data_output_transformed = train_data_output_feature.apply(get_numeric_cat)
        test_data_output_transformed = test_data_output_feature.apply(get_numeric_cat)




        train_data_inputs_transformed = pd.DataFrame(train_data_inputs_transformed,columns=train_data_input_features.columns)
        test_data_inputs_transformed = pd.DataFrame(test_data_inputs_transformed,columns=test_data_input_features.columns)



        return (
            train_data_inputs_transformed,
            train_data_output_transformed,
            test_data_inputs_transformed,
            test_data_output_transformed

        )


transformation_object = DataTransformation()
transformation_object.initiate_data_transformation()
