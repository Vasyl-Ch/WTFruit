import json
import tensorflow as tf

MODEL_PATH = "app/fruit_classifier.keras"
CLASSES_PATH = "app/class_labels.json"


def load_model():

    model = tf.keras.models.load_model(MODEL_PATH)

    with open(CLASSES_PATH) as f:
        classes = json.load(f)

    return model, classes


model, classes = load_model()
