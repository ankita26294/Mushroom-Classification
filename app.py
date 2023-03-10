
import pickle
from flask import Flask, request, render_template,app,jsonify,url_for
import numpy as np
import pandas as pd



app = Flask(__name__)
model = pickle.load(open('decision_tree.pkl', 'rb'))



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/webapp', methods=['GET', 'POST'])
def fill():
    return render_template('webapp.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            gillcolor = float(request.form["gill-color"])
            sporeprintcolor = float(request.form["spore-print-color"])
            population = float(request.form["population"])
            gillsize = float(request.form["gill-size"])
            stalk_root = float(request.form["stalk-root"])
            bruises = float(request.form["bruises"])
            stalkshape = float(request.form["stalk-shape"])

            x = pd.DataFrame({"gill_color": [gillcolor], "spore_print_color": [sporeprintcolor], "population": [population],
                             "gill_size": [gillsize], "stalk_root": [stalk_root], "bruises": [bruises],
                             "stalk_shape": [stalkshape]})

            ml = model.predict(x)
            m = round(ml[0],2)
            if m == 0:
                g = "poisonous"
            else:
                g = "edible"

            return render_template('webapp.html', result='Your mushroom is {}!'.format(g))
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)