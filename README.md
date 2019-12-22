# PyExcel-Docker

PyExcel-Docker is a docker version of the popular PyExcel (https://github.com/pyexcel/pyexcel) Application. This is an implementation of PyExcel with a simple user interface. 

The objective is to convert an excel file into JSON data. 

 ## Assumptions 

These include:
1. You are proficient in Python 
2. You know what Docker is and have used it before. 
3. You have used PyExcel. 

##  How to use PyExcel-Docker


1. Go to the docker hub and pull the Docker image. 
2. Run the image in your preferred environment by using the following command. 

```docker run -d -p 5000:5000 a23labs/pyexcel-docker:latest```

## Installation and running on your local machine 

Install and activate your virtual environment 

` source venv/bin/activate ` 

## Run 🏃🏾‍♂️

` python app.py ` 

Then navigate to `http://localhost:5000/upload` and upload an excel file. 


## Running on Heroku 

This is on assumption that you have a Heroku Account and an existing application

` git push heroku master `

✌🏾 

Made in 🇺🇬
