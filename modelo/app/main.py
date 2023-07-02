
import tensorflow as tf
from keras.models import load_model
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi import File, UploadFile
from keras.preprocessing import image
from PIL import Image
import uvicorn
import cv2

print('STARTING APP')

app = FastAPI()

try:
    model = load_model('conv.h5')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.get("/health")
async def health_check():
    return {"status": "OK"}


@app.post('/predict')
async def predict(image_file: UploadFile = File(...)):
    if not model:
        raise HTTPException(status_code=500, detail="Model could not be loaded")
    try:
        image = Image.open(image_file.file)    
        image = np.array(image)
        image = cv2.resize(image, (240, 320))
        image = image.astype(np.float32)
        image = image / 255.0
        image=np.expand_dims(image, axis=0)
        print(image.shape)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {e}")

    try:
        predictions = model.predict(image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error making prediction: {e}")

    try:
        # Obten la clase con mayor score
        predicted_class = np.argmax(predictions[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interpreting prediction: {e}")

    return {"predicted_class": int(predicted_class)}

if __name__ == "__main__":
    import uvicorn  
    uvicorn.run(app, host="0.0.0.0", port=80)