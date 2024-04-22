from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from fastapi.middleware.cors import CORSMiddleware
import keras

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
MODEL = keras.models.load_model("./models/2_model")
print(MODEL)
CLASS_NAMES = ["oocarpa", "psegoutrobus", "tecunumanii"]

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.get("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    image_resized = tf.image.resize(image, (256, 256))

    image_batch = np.expand_dims(image_resized, 0)


    predictions = MODEL.predict(image_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2) # np.argmax(predictions[0])    

    return {
        'class': predicted_class,
        'confidence': float(confidence),
    }

@app.get("/")
async def root():
    return {"message": "Welcome to the Pine Seeds Classifier API!"}


if __name__== "__main__":
    uvicorn.run(app, host='localhost', port=8000)
