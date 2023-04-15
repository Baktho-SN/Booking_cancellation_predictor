# Booking Cancellation Predictor

Booking Cancellation Predictor App is used to predict whether or not a Customer would cancel the room booked in the hotel. Created using python's scikit-learn, Fastapi, numpy and joblib packages.

![python 3.11.0](https://img.shields.io/badge/Python-blue.svg)
![html](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![numpy](https://img.shields.io/badge/Numpy-777BB4?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/Scikit_learn-0078D4?logo=scikit-learn&logoColor=white)
![fastapi](https://img.shields.io/badge/Fastapi-109989?logo=FASTAPI&logoColor=white)
![jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?logo=Jupyter&logoColor=white)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)


## Dataset Description

The dataset consist of several predictor (independent) variables and one target (dependent) variable, Charges. Independent variables include the lead_time,market_segment_type,avg_price_per_room,Number of special requests

The data contains the following columns:

| Feature Name               | Feature Description                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| lead_time                  | Number of days that elapsed between the entering date of the booking and the arrival date           |
| market_segment_type        | What segment was used for the booking of the ticket(Online/Other)                                   |
| avg_price_per_room         | Average Cost of a room (currency)                                                                   |
| no_of_special_requests     | Number of special requests made (count 0- 5)                                                        |
| booking_status             | If the booking was cancelled or not (Yes/No)                                                        |

## Installation

Open Anaconda prompt and create new environment

```
conda create -n your_env_name python = (any_version_number > 3.11.0)
```

Then Activate the newly created environment

```
conda activate your_env_name
```

Clone the repository using `git`

```
git clone gh repo clone Baktho-SN/Booking_cancellation_predictor
```

Change to the cloned directory

```
cd <directory_name>
```

To install all requirement packages for the app

```
pip install -r requirements.txt
```

Then, Run the app

```
uvicorn main:app --reload
```

## 📷 Screenshots

### Website

![app interface](markdown/website.png)

### Demo

![Demo.GIF](markdown/demo.gif)
