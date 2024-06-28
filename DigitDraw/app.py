from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from PIL import Image
import io

# Load the Flask app
app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('mnist_cnn_model.h5')

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the POST request
    image = request.files['file'].read()
    image = Image.open(io.BytesIO(image)).convert('L')  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to 28x28
    image = np.array(image) / 255.0  # Normalize
    image = image.reshape(1, 28, 28, 1)  # Reshape to fit the model input
    
    # Predict the digit
    prediction = model.predict(image)
    digit = np.argmax(prediction)
    
    return jsonify({'digit': int(digit)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
