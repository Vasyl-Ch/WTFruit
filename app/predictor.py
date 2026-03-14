import numpy as np

from app.model import model, classes


def preprocess(image):
    image = image.resize((128,128))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    return image


def predict(image):

    image = preprocess(image)
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions)
    confidence = np.max(predictions)
    label = None
    for fruit_name, index in classes.items():
        if index == predicted_class:
            label = fruit_name
            break
    
    if label is None:
        label = "Unknown"

    return label, round(float(confidence) * 100, 2)