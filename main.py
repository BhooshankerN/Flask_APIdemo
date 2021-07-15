

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def bmi():
    data = request.get_json()
    weight = data['weight'] # in kg
    height = data['height'] # in m
    res = round((int(weight)/(float(height)*float(height))), 2)
    if res < 20:
        return (jsonify({"bmi (you are lean)": res}))
    elif res > 25:
        return (jsonify({"bmi (you are fat) ": res}))
    else:
        return (jsonify({"bmi (you are normal) ": res}))
        
app.run()  


