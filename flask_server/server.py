import numpy as np
from flask import Flask, render_template, request
from tensorflow import keras

from reddit_api import RedditWrapper

app = Flask(__name__)

mul_model = keras.models.load_model(
    '/Users/oliverwandschneider/dev/PycharmProjects/hatespeech_classifier/model_saves_saves/multi_class_rnn_other')
bin_model = keras.models.load_model(
    '/Users/oliverwandschneider/dev/PycharmProjects/hatespeech_classifier/model_saves_saves/binary_class_rnn')

wrapper = RedditWrapper()
hs_classes = ['other', 'racism', 'religion', 'disability', 'sexism', 'sexual orientation']


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods = ["POST"])
def process():
    classes = ["No Hatespeech", "Hatespeech"]
    results = list()
    if request.method == 'POST':
        choice = request.form['taskoption']
        rawtext = request.form['rawtext']
        rawtext = rawtext.strip()
        if choice == 'username':
            values = wrapper.get_user_comments(user_name = rawtext)
        elif choice == 'posturl':
            values = wrapper.get_post_comments(link = rawtext)
        else:
            values = rawtext.split(sep = "\n")

        pred = bin_model.predict(np.array([val.lower() for val in values]))
        class_pred = mul_model.predict(np.array([val.lower() for val in values]))
        for inx in range(len(values)):
            hs_class = ""
            if np.argmax(pred[inx]) == 1:
                hs_class = hs_classes[np.argmax(class_pred[inx])]
            results.append([inx + 1, values[inx], classes[np.argmax(pred[inx])], hs_class])

        return render_template("index.html", results = results, num_of_results = len(results))

    # return render_template("index.html", results = [classes[np.argmax(pred)]], num_of_results = len(results))
    return render_template("index.html", results = ["Oh no!"], num_of_results = 1)


if __name__ == '__main__':
    app.run(debug = True)
