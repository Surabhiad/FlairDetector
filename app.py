from flask import Flask, render_template, request
from worker import predictor
import json

app = Flask(__name__)

@app.route('/')
def make():
    return render_template('index.html')

@app.route('/automated_testing', methods=['POST'])
def predict():
    if request.method=='POST':
        x = request.files['upload_file']
        lines = x.read()
        lines = lines.decode("utf-8").split("\n")

        flair = dict()
        for l in lines:
            if "https" not in l:
                continue
            print("##### line - ", l)
            flair[str(l)]=predictor.predictFlair(str(l))
        return json.dumps(flair)
 
if __name__ == '__main__':
    app.run(debug=True, port=33507) 
