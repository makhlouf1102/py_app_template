# py_app_template
template for a python script app

## Set up the python virtual environment
Make sure you have a python virtual environment
```
python -m venv venv
```
Go into this virtual environment
```
source vene/Script/activate # Windows 
source vene/bin/activate # Linux
```
Install all the dependencies in the `requirements.txt`
```
pip install -r requirements.txt
```
## You Added a new library ?
If you added a new library, you must add this one into `requirements.txt`
```
pip3 freeze > requirements.txt  # Python3
pip freeze > requirements.txt  # Python2
```
## Run the docker file
Build the docker Image
```
docker build -t imageName .
```
Run the image
```
docker run --name containerName imageName
```




