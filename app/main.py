import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import shutil
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image

from app.predictor import predict

app = FastAPI()

templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict_image(request: Request, file: UploadFile = File(...)):
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    image = Image.open(filepath)
    prediction, confidence = predict(image)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "prediction": prediction,
            "confidence": f"{confidence:.2f}%",
            "image_path": f"/{filepath}",
        },
    )
