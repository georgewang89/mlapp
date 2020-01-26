from fastai.vision import *
import requests
from pandas.io.json import json_normalize

data = {"url": "https://i.imgur.com/jv5ko9r.jpg"}
response = requests.post("{}/".format("http://127.0.0.1:5000"), json =data )
response_loaded = json.loads(response.content)
response_df = json_normalize(response_loaded)
print("Price of the house should be "+ response_df["class"])
