from flask import Flask, request, jsonify, render_template
import numpy as np
import json
from utils import *

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Flask!"


@app.route("/ds-salary-prediction", methods=["GET"])
def ds_salary_prediction():
    sample_df = load_sample()
    sample_html = sample_df.to_html(index=False)

    return render_template("project.html", sample_table=sample_html)


@app.route("/predict", methods=["GET"])
def predict():
    model = load_model()
    x = load_prediction_input()

    ## Predicted value is the y-hat/prediction
    ## Ground truth/ Target is the
    ## Input data is the x

    prediction = model.predict(x)
    print(prediction)
    return prediction.tolist()


if __name__ == "__main__":
    app.run(
        debug=True
    )  # ! IMPORTANT: Remove "debug=True" before deploying to production
