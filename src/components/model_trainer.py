from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from catboost import CatBoostClassifier
import pickle
import os
from src.exception import CustomException
from src.logger import logging
import numpy as np
from src.components.data_transformation import  DataTransformationConfig
from src.components.data_transformation import DataTransformation


class ModelTrainerConfig:
    def __init__(self):
        self.trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config_obj = ModelTrainerConfig()
        self.best_model_object = None

    def initiate_model_trainer(self,train_data_inputs_transformed,
            train_data_output_transformed,
            test_data_inputs_transformed,
            test_data_output_transformed):



        print(train_data_inputs_transformed.shape,
            train_data_output_transformed.shape,
            test_data_inputs_transformed.shape,
            test_data_output_transformed.shape)

        X_train, y_train, X_test, y_test = (
            train_data_inputs_transformed,
            train_data_output_transformed,
            test_data_inputs_transformed,
            test_data_output_transformed
        )

        logging.info("Defined X_train,y_train,X_test,y_Test")

        models = {
            "Decision Tree Classifier": DecisionTreeClassifier(),
            "Random Forest Classifier": RandomForestClassifier(),
            "Naive Bayes Classifier": GaussianNB(),
            "SVM Classifier": SVC(),
            "K-Nearest Neighbors Classifier": KNeighborsClassifier(),
            "Gradient Boosting Classifier": GradientBoostingClassifier(),
            "AdaBoost Classifier": AdaBoostClassifier(),
            "XGBoost Classifier": XGBClassifier(),
            "CatBoost Classifier": CatBoostClassifier()
        }

        model_report : dict = {}

        logging.info("Initiating Model Evaluation for all models ")

        def evaluate_model(X_train= X_train ,y_train = y_train , X_test = X_test,y_test = y_test,model = None ):
            model.fit(X_train,y_train)
            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test,y_pred,)
            precison = precision_score(y_test,y_pred,average='weighted')
            f1score = f1_score(y_test,y_pred,average='weighted')

            return {'accuracy':accuracy,"Precision":precison,"f1score":f1score}

        for model_name , model_object in models.items():
            report = evaluate_model(model=model_object)
            model_report[model_name] = report


        logging.info("Completed model training with data and evaluation for all models ")

        logging.info("Finding the best model ")

        # Sorting by best r2 score :
        sorted_model_report = sorted(model_report.items(), key=lambda x: x[1]['f1score'], reverse=True)
        best_model_name = sorted_model_report[0][0]

        best_model_object = None
        best_model_f1score = None

        for model_name, model_object in models.items():
            if model_name == best_model_name:
                best_model_object = model_object

        for model_name, report in model_report.items():
            if model_name == best_model_name:
                best_model_f1score = report['f1score']

        # If we dont find any model score > 70 we raise an error !
        if best_model_f1score < 0.70:
            raise CustomException("NO model found with r2 score > 0.70")

        if best_model_f1score > 0.70:
            logging.info(
                f"Best Model Found and it is :{best_model_name} with an r2 score of {best_model_f1score}")

        self.best_model_object = best_model_object



        print(model_report)

    def save_best_model(self):
        with open(os.path.join('artifacts', 'trained_model.pkl'), 'wb') as f:
            pickle.dump(self.best_model_object, f)

        print(self.best_model_object)


datatrans_obj = DataTransformation()
input_features_training , input_features_testing , target_features_training , target_features_testing = datatrans_obj.initiate_data_transformation()
model_trainer_obj = ModelTrainer()
model_trainer_obj.initiate_model_trainer(input_features_training , input_features_testing , target_features_training , target_features_testing)
model_trainer_obj.save_best_model()