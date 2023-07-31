from flask import Flask, render_template, request
import os
from test3 import get_prediction

app = Flask(__name__)

# define the allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded file from the request
    file = request.files['file']
    wanteddirectory='C:\\Users\\moham\\Desktop\\'
    # Check if the file is allowed
    if not allowed_file(file.filename):
        return render_template('index.html', error1="Invalid file type. Please upload a file with a valid extension.")
    if not os.path.exists(wanteddirectory+file.filename):
        return render_template('index.html', error2=wanteddirectory)
    else:
        # Get the prediction result using the get_prediction function
        result,prediction0 = get_prediction(file.filename,wanteddirectory)

        # Return the predicted result
        return render_template('index.html', prediction1=result,percent=prediction0*100)

if __name__ == '__main__':
    app.run()
