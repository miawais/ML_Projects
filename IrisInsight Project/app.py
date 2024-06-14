from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Your prediction logic here
    prediction_text = "Prediction result here"
    return render_template('your_template.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
