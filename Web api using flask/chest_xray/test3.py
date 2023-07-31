from keras_preprocessing import image
from keras.models import load_model
from tensorflow.keras.applications.resnet_v2 import preprocess_input
import numpy as np
def get_prediction(filename,wanteddirectory):
    model=load_model(wanteddirectory+'tuned_resnet.h5') #Loading our model
    # Load the image and preprocess it
    img_path = wanteddirectory+filename
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    # Make the prediction
    prediction = model.predict(x)
    print(f'Predictions: {prediction}')
    # Print the prediction
    if prediction[0] > 0.5: # assuming a threshold of 0.5 for binary classification
        return('Person is affected with Pneumonia.',prediction)
    else:
        return('Person is safe.',1-prediction)
