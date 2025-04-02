from flask import Flask, request, jsonify, render_template
import plotly.express as px
import pandas as pd
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

    context = {
        "sample_table": sample_html,
        "columns": sample_df.shape[1],
        "rows": 742,
        "graph_json": graph(),
    }

    return render_template("project.html", context=context)


@app.route("/predict", methods=["GET"])
def predict():
    model = load_model()
    # x = **THE INPUT DATA FOR PREDICTION**

    # prediction = model.predict(x)
    # print(prediction)
    # return prediction.tolist()


if __name__ == "__main__":
    app.run(
        debug=True
    )  # ! IMPORTANT: Remove "debug=True" before deploying to production
