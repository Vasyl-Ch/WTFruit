import json
import tensorflow as tf

MODEL_PATH = "app/fruit_classifier.keras"
CLASSES_PATH = "app/class_labels.json"


try:
    with open(CLASSES_PATH, "r") as f:
        data = json.load(f)

    reversed_dict = {str(v): k for k, v in data.items()}

    with open(CLASSES_PATH, "w") as f:
        json.dump(reversed_dict, f, indent=2)

    print(f"Файл {CLASSES_PATH} успешно модифицирован!")

except Exception as e:
    print(f"Ошибка при работе с файлом: {e}")


def load_model():

    model = tf.keras.models.load_model(MODEL_PATH)

    with open(CLASSES_PATH) as f:
        classes = json.load(f)

    return model, classes


model, classes = load_model()
