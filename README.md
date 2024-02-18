# End-to-End-Chest-Cancer-Classification-using-MLflow-DVC


## Workflows
Cambiar los archivos en este orden
1. Update config.yaml. configuración del proyecto
2. Update secrets.yaml [Optional]: credenciales secretas como contraseñas a bds, aquí no se hace
3. Update params.yaml : hiperparámetros del modelo
4. Update the entity. ver notebook data_ingestion. 1.Explicación de entidades. copiar el codigo dentro de src/entity
5. Update the configuration manager in src config. 2 ver notebook data_ingestion. 2. Probando las constantes. copiar el codigo dentro de src/config 
6. Update the components: donde están definidos los data ingestion, model training, model evaluation. ver en data_ingestion 3. Componentes
7. Update the pipeline: donde se integran las funciones de entrenamiento y predicción. ver en data_ingestion 4. pipeline
8. Update the main.py: y cuando se cree la app va a cambiar el nombre a app.py
9. Update the dvc.yaml





## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtube.com/playlist?list=PLkz_y24mlSJZrqiZ4_cLUiP0CBN5wFmTb&si=zEp_C8zLHt1DzWKK)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/chest-Disease-Classification-MLflow-DVC.mlflow \
MLFLOW_TRACKING_USERNAME=entbappy \
MLFLOW_TRACKING_PASSWORD=6824692c47a4545eac5b10041d5c8edbcef0 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/chest-Disease-Classification-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9353c5b10041d5c8edbcef0

```



### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh ### descargando docker

	sudo sh get-docker.sh ### instalando docker

	sudo usermod -aG docker ubuntu
	### : usermod: A command in Linux used to modify user accounts.
-aG docker: Options for usermod. -a appends the user to the supplementary group(s), and docker specifies the group to which the user is appended.
ubuntu: The username specified here. This command adds the user "ubuntu" to the group "docker". This is necessary to allow the user to execute Docker commands without needing root privileges every time.

	newgrp docker

	newgrp: A command in Unix-like operating systems that allows a user to log in to a new group by changing the current group ID.
docker: The group name specified here. This command logs the current user into the group "docker". This is necessary to ensure that the group membership is applied to the current shell session. Without this, the user may need to log out and back in for the group membership to take effect.
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

