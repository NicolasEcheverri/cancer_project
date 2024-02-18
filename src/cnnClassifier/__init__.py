import os
import sys
import logging
#1. este notebook es para crear el logger y que vaya guardando las ejecucione
#modulo: carpeta de donde se está ejecutando. 
#message es el mensaje que se le pasa  logger.info("welcome to cnnClassifier") 
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
#ejemplo de salida: [2024-02-14 22:13:45,905: INFO: main: welcome to cnnClassifier]
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
#creando la carpeta llamada log_dir
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) #imprime el log 
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
