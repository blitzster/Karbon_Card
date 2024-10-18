from flask import Flask, render_template, request, redirect, url_for
import json
from model import probe_model_5l_profit

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/submit', methods=['POST'])
def submit_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        data = json.load(file)  # Load the JSON data
        print("Uploaded data:", data)  # Debugging output

        if "data" not in data:
            return "Invalid data structure", 400  # Handle missing key

        result = probe_model_5l_profit(data["data"])  # Call your model function
        return render_template('results.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
