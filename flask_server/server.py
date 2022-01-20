from flask import Flask,render_template,url_for,request
import tensorflow as tf

app = Flask(__name__)

# new_model = tf.keras.models.load_model('/Users/oliverwandschneider/develop/PyCharmProjects/hatespeech_classifier/models/rnn_one')

# Check its architecture
# print(new_model.summary())

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=["POST"])
def process():
    rawtext = "oh no"
    if request.method == 'POST':
        choice = request.form['taskoption']
        rawtext = request.form['rawtext']
        print(choice, rawtext)

#
    return render_template("index.html", results=[rawtext], num_of_results=1)


if __name__ == '__main__':
    app.run(debug=True)
