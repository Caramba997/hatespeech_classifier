import numpy as np
from flask import Flask, render_template, request
from tensorflow import keras

app = Flask(__name__)

mul_model = keras.models.load_model(
    '/Users/oliverwandschneider/dev/PycharmProjects/hatespeech_classifier/models/multi_class_rnn')
bin_model = keras.models.load_model(
    '/Users/oliverwandschneider/dev/PycharmProjects/hatespeech_classifier/models/binary_class_rnn')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods = ["POST"])
def process():
    classes = ["No Hatespeech", "Hatespeech"]
    rawtext = ""
    pred = []
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        pred = bin_model.predict(np.array([rawtext.lower()]))
        print(pred)

    return render_template("index.html", results = [classes[np.argmax(pred)]], num_of_results = 1)


if __name__ == '__main__':
    app.run(debug = True)
