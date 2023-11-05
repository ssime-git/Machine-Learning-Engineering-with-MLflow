# base image
FROM continuumio/miniconda3

# install make
RUN apt-get update
RUN apt-get install -y make

# install mlflow
RUN pip install mlflow>=1.18.0

# create a working directory
WORKDIR /mlflow-project

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["mlflow", "ui", "--host", "0.0.0.0"]
