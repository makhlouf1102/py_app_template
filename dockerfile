# Deriving an image of python
FROM python:3.9

# working directory
WORKDIR /scrapper

# Setting the working directory
COPY .env .
COPY ./app ./app
COPY requirements.txt .

# Installing dependencies
RUN pip install -r requirements.txt

# Run the application
CMD [ "python", "app/main.py" ]