from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline


#inicializando Flask. cambio
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg" #cada que el usuario carge la imagen se va a llamar así
        self.classifier = PredictionPipeline(self.filename) 




#creando la ruta por defecto. es decir cuando se entre a la la uri que salga el index.html
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


#si se ejecuta /train va a empezar el entrenamiento
@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # os.system("dvc repro")
    return "Training done successfully!"



#si la ruta es predict 2
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename) #viene de utils. lo decodifica
    result = clApp.classifier.predict()
    return jsonify(result)


#ejecutando ClientApp cuando se ejecute este .py
if __name__ == "__main__":
    #cambio para que ejecute de nuevo github actions
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080) #for AWS

