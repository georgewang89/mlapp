from fastai.vision import *
from PIL import Image
import requests
from io import BytesIO

from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
    if(request.method == 'POST'):
        data = request.get_json()
        img_url = data["url"]
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
        img.save('image.jpg')
        img = open_image('image.jpg')
        classifier = load_learner('')
        pred_class = classifier.predict(img)[0]
        string = pred_class.__str__()
        return jsonify({"class":string})
    else:
        return  jsonify({"about":"Hello World"})

if __name__ == '__main__':
    app.run(debug=True)