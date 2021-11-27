Rain API Server
===============

An example project for RESTful API development using OpenAPI and Python.

## How to Run
* ```python -m venv env```
* ```env\Scripts\activate.bat```
* ```java -jar openapi-generator-cli-5.3.0.jar generate -i openapi/ku-place-api.yaml -o autogen -g python-flask```
* ```pip install -r requirements.txt```
* ```python app.py```
* ```http://localhost:8080/rain-api/v1/ui```
