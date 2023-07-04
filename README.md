## API de Estrellas Pulsar
Esta es una API desarrollada con FastAPI que proporciona operaciones CRUD (crear, leer, actualizar, eliminar) para estrellas pulsar.

### Endpoints
- **GET** /pulsar: Obtiene una lista de todas las estrellas pulsar almacenadas.
- **POST** /pulsar: Crea una nueva estrella pulsar.
- **GET** /pulsar/{pulsar_id}: Obtiene los detalles de una estrella pulsar específica según su ID.
- **PUT** /pulsar/{pulsar_id}: Actualiza los atributos de una estrella pulsar específica.
- **DELETE** /pulsar/{pulsar_id}: Elimina una estrella pulsar específica.
- **POST** /pulsar/predict: Realiza la predicción de una estrella pulsar utilizando un modelo preentrenado.

### Estructura del Proyecto
El proyecto sigue la siguiente estructura:

- main.py: Archivo principal de la aplicación FastAPI que inicia el servidor y configura los enrutadores.
- models.py: Contiene las definiciones de los modelos de datos utilizados en la API, como la clase Pulsar y Prediction_Input.
- routes.py: Contiene la configuración de las rutas (endpoints) de la API utilizando el enrutador de FastAPI.
- controllers/pulsar_controller.py: Contiene la lógica de controladores para manejar las operaciones CRUD relacionadas con las estrellas pulsar.

### Ejecución
Para ejecutar la API en el puerto 8080, sigue los siguientes pasos:

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Opcional: Si quieres crear un ambiente virtual
   
   ``
   python -m venv venv
   ``
4. Instala las dependencias ejecutando:
   
   ``
   pip install -r requirements.txt.
   ``
5. Ejecuta el siguiente comando en la raíz del proyecto:
   
   ``
   uvicorn main:app --reload --port 8080
   ``
7. Ahora con [Postman](https://www.postman.com/downloads/) podras consumir la api, como por ejemplo:

![post-pulsar](https://github.com/mvizap/pulsar-classification-fastapi/assets/26266422/da763232-ba90-467e-8eb8-be77c6b4ab59)
![get-pulsar](https://github.com/mvizap/pulsar-classification-fastapi/assets/26266422/a940bab0-6367-47e6-b22d-f5c4ad7640a0)
![put-pulsar](https://github.com/mvizap/pulsar-classification-fastapi/assets/26266422/f537cf4d-984c-431e-9707-accc18cf2b60)
![delete-pulsar](https://github.com/mvizap/pulsar-classification-fastapi/assets/26266422/ae233f58-0cc1-4b55-8dce-91d87ee54704)
![predict-pulsar](https://github.com/mvizap/pulsar-classification-fastapi/assets/26266422/5269e152-671b-4810-9775-0c4b23baf151)



   
   
