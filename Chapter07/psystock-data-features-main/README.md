# psytock-data-features

# Mes notes

1. Création du fichier MLproject avec ajout des étapes et  association avec les codes python
2. création de fichiers python (les maillons de la pipeline)

# Lancement de la pipeline


```sh
# run the container
docker-compose up

# run the container
#docker run -p 5000:5000 -v $(pwd):/mlflow-project -it chapter07-mlflow

# chapter07-mlflow-1 = container name
docker exec -it psystock-data-features-main-mlflow-1 /bin/bash


# note that `psystock_data_pipelines` is the name in the MLproject
mlflow run . --experiment-name=pystock_data_features
```

