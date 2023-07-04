from fastapi import APIRouter, HTTPException, status
from models import Pulsar
from models import Prediction_Input
from models import Prediction_Output
import numpy as np
import pickle

router = APIRouter()

pulsar_list = []
preds = []

# Cargar el modelo y el scaler desde los archivos pickle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


@router.get("/pulsar")
def get_all():
    return pulsar_list

@router.post('/pulsar', status_code=status.HTTP_201_CREATED)
def create_pulsar(item : Pulsar):
    pulsar_list.append(item)
    return {
        "message": "Creado satisfactoriamente",
        "": item
        }
    
@router.get("/pulsar/{pulsar_id}")
def update_pulsar(pulsar_id: int):
    for index, item in enumerate(pulsar_list):
        if item.id == pulsar_id:
            return item
    raise HTTPException(status_code=404, detail='Not found')

@router.put("/pulsar/{pulsar_id}")
def update_pulsar(pulsar_id: int, updated_pulsar: Pulsar):
    for index, pulsar in enumerate(pulsar_list):
        if pulsar.id == pulsar_id:
            # Actualizar los atributos relevantes del objeto Pulsar
            pulsar.Mean_Integrated = updated_pulsar.Mean_Integrated
            pulsar.SD = updated_pulsar.SD
            pulsar.EK = updated_pulsar.EK
            pulsar.Skewness = updated_pulsar.Skewness
            pulsar.Mean_DMSNR_Curve = updated_pulsar.Mean_DMSNR_Curve
            pulsar.SD_DMSNR_Curve = updated_pulsar.SD_DMSNR_Curve
            pulsar.EK_DMSNR_Curve = updated_pulsar.EK_DMSNR_Curve
            pulsar.Skewness_DMSNR_Curve = updated_pulsar.Skewness_DMSNR_Curve
            
            return {
                "message": "Modificado satisfactoriamente",
                "result": pulsar
            }
        
    raise HTTPException(status_code=404, detail='Not found')


@router.delete('/pulsar/{pulsar_id}')
def delete_pulsar(pulsar_id:int):
    for index, item in enumerate(pulsar_list):
        if item.id == pulsar_id:
            del pulsar_list[index]
            return {
                "message": "Borrado satisfactoriamente"
            }
        
    raise HTTPException(status_code=404, detail='Not found')

@router.post("/pulsar/predict")
def predict_pulsar_star(item: Prediction_Input):
    # Obtener los valores de las características desde el objeto item
    values = [
        float(item.Mean_Integrated),
        float(item.SD),
        float(item.EK),
        float(item.Skewness),
        float(item.Mean_DMSNR_Curve),
        float(item.SD_DMSNR_Curve),
        float(item.EK_DMSNR_Curve),
        float(item.Skewness_DMSNR_Curve)
    ]
    
    # Realizar la predicción
    prediction = predict(values)
    
    # Devolver el resultado de la predicción como respuesta
    return {
        'prediction': int(prediction[0])
    }

    
# Función para realizar predicciones
def predict(values):
    # Escalar los valores proporcionados
    scaled_values = scaler.transform([values])
    # Realizar la predicción utilizando el modelo cargado
    prediction = model.predict(scaled_values)
    return prediction