# WTFruit - Fruit & Vegetable Classification

A web application that classifies fruits and vegetables using TensorFlow deep learning model.

## Features

- Upload images of fruits and vegetables
- Get real-time classification predictions
- Confidence scores for each prediction
- Clean and responsive web interface

## Tech Stack

- **Backend**: FastAPI, TensorFlow
- **Frontend**: HTML, CSS, Jinja2
- **Model**: Keras neural network trained on 36 fruit/vegetable classes
- **Deployment**: Docker, Docker Compose

## Supported Classes

The model can classify 36 different fruits and vegetables including:
apple, banana, beetroot, bell pepper, cabbage, capsicum, carrot, cauliflower, chilli pepper, corn, cucumber, eggplant, garlic, ginger, grapes, jalepeno, kiwi, lemon, lettuce, mango, onion, orange, paprika, pear, peas, pineapple, pomegranate, potato, raddish, soy beans, spinach, sweetcorn, sweetpotato, tomato, turnip, watermelon

## Quick Start

### Option 1: Docker (Recommended)

1. Clone the repository
2. Run with Docker Compose:
```bash
docker-compose up --build
```
3. Open http://localhost:8000 in your browser

4. To stop the application:
```bash
docker-compose down
```

5. To rebuild and restart:
```bash
docker-compose up --build --force-recreate
```

### Option 2: Local Development

1. Create virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

4. Open http://localhost:8000 in your browser

## Usage

1. Open the web application
2. Click "Choose File" and select an image of a fruit or vegetable
3. Click "Upload & Predict"
4. View the classification result and confidence score

## Project Structure

```
WTFruit/
├── app/
│   ├── main.py          # FastAPI application
│   ├── model.py         # Model loading logic
│   ├── predictor.py     # Prediction functions
│   └── class_labels.json # Class mappings
├── templates/
│   ├── index.html       # Home page
│   └── result.html      # Results page
├── static/
│   ├── style.css        # Styles
│   └── images/          # Background images
├── uploads/             # Uploaded images
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Model Performance

- Input size: 128x128 RGB images
- Framework: TensorFlow/Keras

## Contributing

Feel free to submit issues and pull requests to improve the project.
