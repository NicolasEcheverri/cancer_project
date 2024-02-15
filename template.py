import os
from pathlib import Path
import logging #librería para ...

#iniciando el log level
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep", 
    #estructura para cd/ci. en workflow es donde de realiza los jobs de cicd .gitkeep es para crear un archivo dentro para que git pueda trakear la carpeta
    f"src/{project_name}/__init__.py", #src: source folder. init.py constructure file. Para crear los paquetes locales
    f"src/{project_name}/components/__init__.py", #data ingestion, data validation, model design 
    f"src/{project_name}/utils/__init__.py", #carpeta de funciones utiles
    f"src/{project_name}/config/__init__.py", #archivos de configuración
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml", #archivo de dvc
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb", #Para experimentos
    "templates/index.html" #codigo html<


]


#logica para crear los folders
for filepath in list_of_files:
    filepath = Path(filepath) #para tratar con con las especificaciones de que para windows es \ y para linux es /    filedir, filename = os.path.split(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
