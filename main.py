import joblib # for loading model pickle file
import numpy as np # for array conversion
import pandas as pd # for dataframe conversion

# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI() # instance of FastAPI class

# mount static folder files to /static route
app.mount("/static",StaticFiles(directory="static"),name="static")

# loads the ML model
model_rf = joblib.load("models/Cancellation_prediction_model.pkl")
model_svc = joblib.load("models/Cancellation_prediction_svcmodel.pkl")
model_knn = joblib.load("models/Cancellation_prediction_knnmodel.pkl")
model_xgb = joblib.load("models/Cancellation_prediction_xgbmodel.pkl")
model_nb = joblib.load("models/Cancellation_prediction_nbmodel.pkl")
model_lin = joblib.load("models/Cancellation_prediction_linearmodel.pkl")


# sets the templates folder for the app
templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def home_index(request: Request):
	"""
    Function to render `index.html` at route '/' as a get request
    __Args__:
    - request (Request): request in path operation that will return a template
    __Returns__:
    - TemplateResponse: render `result.html`
    """
	return templates.TemplateResponse("base.html",{"request":request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(
	request: Request,
    lead_time: float = Form(...),
    market_segment_type: str = Form(...),
    avg_price_per_room: float = Form(...),
    no_of_special_requests: int = Form(...)):
	"""
    Function to predict heart diasease classification
    and shows the result by rendering `index.html` at route `/predict`

    __Args__:
    - __request__: request in path operation that will return a template
    - __lead_time__: Time taken to lead the customer to the room ,
    - __market_segment_type__: Market segmentation type-either online or other modes,
    - __avg_price_per_room__: Average price cost per room,
    - __no_of_special_requests__: number of special requests made by the customer ,

    __Returns:__
    - __TemplateResponse__: render `base.html`
    """

	market_segment_type = 0 if market_segment_type.lower() == "online" else 1

	# convert list to pandas dataframe

	input_list = [lead_time,market_segment_type,avg_price_per_room,no_of_special_requests]

	final_values = np.array(input_list).reshape(1,-1)

	output = [model_rf.predict(final_values),
              model_xgb.predict(final_values),
              model_nb.predict(final_values),
              model_lin.predict(final_values),
              model_knn.predict(final_values),
              model_svc.predict(final_values)] #predicts using the model

	predictions = [float(output[0]),float(output[1]),float(output[2]),float(output[3]),float(output[4]),float(output[5])]
	
	return templates.TemplateResponse("result.html",context={"request":request,"prediction":predictions})


