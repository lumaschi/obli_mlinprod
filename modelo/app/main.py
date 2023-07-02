
import tensorflow as tf
from keras.models import load_model
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi import File, UploadFile
from keras.preprocessing import image
from PIL import Image
import uvicorn
import tensorflow as tf
import gradio as gr

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
        image = tf.image.resize(image, (240, 320))
        image = tf.cast(image, dtype=tf.float32)   
        image = image / 255.0
        image = np.expand_dims(image, axis=0)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {e}")

    try:
        predictions = model.predict(image)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error making prediction: {e}")

    try:
        # Obten la clase con mayor score
        predicted_class = np.argmax(predictions[0])
        #predicted_class=predictions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interpreting prediction: {e}")

    return {"predicted_class": int(predicted_class)}
    #return {"predicted_class": str(predicted_class)}

def classify_image(image):   
    image = np.array(image)
    image = tf.cast(image, dtype=tf.float32)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    # Obtiene las etiquetas de las clases
    class_labels = ['APARTMENT', 'HOUSE']
    # Devuelve un diccionario con las etiquetas de las clases y sus probabilidades correspondientes
    return {class_labels[i]: float(prediction[0][i]) for i in range(2)}


demo = gr.Interface(
    fn=classify_image,  # la función que hace la clasificación
    inputs=gr.inputs.Image(shape=(240, 320)),  # el tipo de entrada que espera tu modelo
    outputs=gr.outputs.Label(num_top_classes=2),  # el tipo de salida que produce tu modelo
)
demo.launch(share=True)

if __name__ == "__main__":
    import uvicorn
    app = gr.mount_gradio_app(app, demo, path="/")  
    uvicorn.run(app, host="0.0.0.0", port=80)