# End to End Earthquake Intensity Prediction using Machine Learning

This is an end-to-end machine learning project for predicting the intensity of earthquakes based on historic data. A preview of our app : 
You can try the app yourself here : http://43.205.139.197:8080/
![image](https://user-images.githubusercontent.com/46419407/234553010-ec6b689c-49ff-4816-ba98-1d02ee7f4db1.png)

![image](https://user-images.githubusercontent.com/46419407/234553044-4e38ec40-ca0f-48b5-a497-97653290490a.png)


A Process flow of the complete thing : 



## Data Collection

The data used for this project was collected from the [USGS Earthquake Hazards Program API](https://www.usgs.gov/programs/earthquake-hazards). We have considered the past 15 years of earthquakes that have occurred for our analysis.

## Data Preprocessing and Feature Engineering
- Latitude
- Longitude
- NST (Number of Stations)
- Gap
- Quarter of year
- Month of year
- Day of month

The above features were selected based on domain knowledge and their potential relevance to the earthquake intensity prediction task. Exploratory Data Analysis (EDA) was performed to gain insights into the data and identify any data quality issues that needed to be addressed.
After data collection, the raw data was preprocessed by performing exploratory data analysis (EDA) and feature engineering. The main input features are latitude, longitude, NST, Gap, quarter of year, month of year, and day of month.

## Data Ingestion

The preprocessed data was read.

### Data Transformation
After the raw data was preprocessed and feature engineering was applied, a transformation object was created using `StandardScaler` to scale the input features, which were `Latitude`, `Longitude`, `NST`, `Gap`, `Quarter of year`, `Month of year`, and `day of month`. Additionally, we created categories on the magnitude of the earthquakes so that we could classify them. These transformations were saved as a pickle file named `transformation.pkl`, which was later applied to the data during model inference.

### Model Training
After the preprocessed data was ingested and transformed, classification models were evaluated on the data, and the best model was selected based on its weighted F1 score. The best model on the basis of weighted f1 score came out to be `CatBoost Regressor`. The trained model was saved in a pickle file as `model_trained.pkl`.

### App Deployment
After the model was trained, a Flask app was created with the necessary templates
Deployment Steps : 

Creating a workflow on Github Actions with Amazon EC2 , ECR . You can see the 'aws.yaml' file.

Creating a Runner so that it constanstly listens to jobs

Enabling Continuos Integration , Continuous Delivery and Continous Deployment . 

The complete flow of the process : 
![Flowchart-Earthquake](https://user-images.githubusercontent.com/46419407/234585952-e5eacbf6-ae5b-49c1-bd99-a4a8e0f0a00b.jpeg)

