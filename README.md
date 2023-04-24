# End to End Earthquake Intensity Prediction Web App using Machine Learning

This is an end-to-end machine learning app/project for predicting the intensity of earthquakes in future  based on historic data. You can try the app yourself by this link:


A preview of the app : 
![image](https://user-images.githubusercontent.com/46419407/234055632-1329b035-8dfd-48c6-9a33-51355152e72c.png)

![image](https://user-images.githubusercontent.com/46419407/234055924-090664ad-f3d2-4091-a778-524a067e5cfc.png)


A complete process flow of the project : 
![Flowchart-Earthquake](https://user-images.githubusercontent.com/46419407/234055769-a7dca226-a471-45a3-94a4-b57e114bbe6e.jpeg)


## Data Collection

The data used for this project was collected from the [USGS Earthquake Hazards Program API](https://www.usgs.gov/programs/earthquake-hazards). We have considered the past 15 years of earthquakes that have occurred for our analysis.

## Data Preprocessing and Feature Engineering

After data collection, the raw data was preprocessed by performing exploratory data analysis (EDA) and feature engineering. The main input features are latitude, longitude, NST, Gap, quarter of year, month of year, and day of month.

## Data Ingestion

The preprocessed data was read.

### Data Transformation
After the raw data was preprocessed and feature engineering was applied, a transformation object was created using `StandardScaler` to scale the input features, which were `Latitude`, `Longitude`, `NST`, `Gap`, `Quarter of year`, `Month of year`, and `day of month`. Additionally, we created categories on the magnitude of the earthquakes so that we could classify them. These transformations were saved as a pickle file named `transformation.pkl`, which was later applied to the data during model inference.

### Model Training
After the preprocessed data was ingested and transformed, classification models were evaluated on the data, and the best model was selected based on its weighted F1 score. The best model on the basis of weighted f1 score came out to be `CatBoost Regressor`. The trained model was saved in a pickle file as `model_trained.pkl`.

### App Deployment
After the model was trained, a Flask app was created with the necessary templates. The app was then deployed on a server so that it could be accessed by users.```

