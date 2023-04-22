import logging
import os
import pickle
import sys
import numpy as np
from src import logger

from src.exception import CustomException
from src.logger import logging

class PredictPipelinelaptop():
    def __init__(self,features):

        self.features = features

    def predict(self):
        # With the features we get , we have to first transform data coming in and then predict with our model

        # Loading the transformation object and the Model object  :
        transformation_object = None
        model_object = None


        print(self.features)

        with open(r"src/components/artifact/transformation.pkl","rb") as f:
            transformation_object = pickle.load(f)



        with open(r"src/components/artifact/trained_model.pkl","rb") as f:
            model_object = pickle.load(f)


        data_transformed = transformation_object.transform(self.features)

        prediction = model_object.predict(data_transformed)

        final_prediction = prediction

        return final_prediction


