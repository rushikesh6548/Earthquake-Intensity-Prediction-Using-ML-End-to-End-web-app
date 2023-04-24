import pandas as pd
from flask import Flask,render_template,request,redirect,session
from src.pipeline.predict_pipeline import PredictPipeline


app = Flask(__name__)



# Route for home page :

@app.route('/')
@app.route('/predictdata',methods = ['GET','POST'])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html",title = "Home")
    else:
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        dmin = request.form.get('dmin')
        gap = request.form.get('gap')
        month_of_year = int(request.form.get('month'))
        quarter_of_year = None
        first_quarter = [1,2,3]
        second_quarter = [4,5,6]
        third_quarter = [7,8,9]
        fourth_quarter = [10,11,12]
        if month_of_year in first_quarter:
            quarter_of_year = 1
        elif month_of_year in second_quarter:
            quarter_of_year = 2
        elif month_of_year in third_quarter:
            quarter_of_year = 3
        else :
            quarter_of_year =4

        day_of_month = request.form.get('day')

        input_feats_as_df = pd.DataFrame([{
            'latitude': latitude,
            'longitude': longitude,
            'gap': gap,
            'dmin': dmin,
            'quarter_of_year': quarter_of_year,
            'month_of_year': month_of_year,
            'day_of_month': day_of_month

        }])


        pipeline_obj = PredictPipeline(input_feats_as_df)
        result = pipeline_obj.predict()
        result = result[0]

        print(result[0])

        result_str = None
        if result <= 4.0:
            result_str = "Low"
        elif result > 4.0 and result <= 6.0:
            result_str = "Moderate"
        elif result > 6.0 and result <= 7.0:
            result_str = "Strong"
        elif result > 7.0 and result <= 7.9:
            result_str = "Major"
        elif result > 7.0:
            result_str = "Severe"

        print(result_str)

        return render_template('home.html',response = result_str)


# @app.route('/predict',methods = ['GET','POST'])
# def predict():
#     pass


if __name__ == '__main__':
    app.run(host = "0.0.0.0",debug=True)