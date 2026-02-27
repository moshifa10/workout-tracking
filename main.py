import requests
import dotenv
import os
import pprint
import datetime as dt

dotenv.load_dotenv()
ENDPOINT = "https://app.100daysofpython.dev"

excercise = "/v1/nutrition/natural/exercise"

api_key = os.getenv(key="API_KEY")
app_id = os.getenv(key="APP_ID")
api_post = os.getenv(key="API_POST")
api_get = os.getenv(key="API_GET")
params = {
    # "Content-Type": "application/json",
    "x-app-id": app_id,
    "x-app-key": api_key
}

user = input("Tell me which excersise you did? ")

def call(body):
    response = requests.post(url=ENDPOINT+excercise, headers=params, json=body)
    response.raise_for_status()
    result = response.json()
    # print(pprint.pprint(result))


    now = dt.datetime.now()

    shetty = requests.get(url=api_get)
    shetty.raise_for_status()
    # print(shetty.text)

    data = shetty.json()
    # print(data)
    info = {
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M:%S"),
        "exercise": result["exercises"][0]["name"],
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"],
        # "id": data["workouts"][-1]["id"] +1
    }
    # data["workouts"].append(info)
    shitty_body = {
        "workout": info
    }
    # print(data)
    shitty_post  = requests.post(url=api_post, json=shitty_body)

    # print(shitty_post.text)
    shitty_post.raise_for_status()
# print(now)
if "." in user:
    for i in user.split("."):
        body = {"query":  f"{i}"}
        call(body)
else:
    body = {"query":  f"{user}"}
    call(body)
