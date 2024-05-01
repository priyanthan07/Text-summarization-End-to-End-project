import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format='[%(asctime)s] : %(message)s:')

projectName = "TextSummarization" 

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/utils/common.py",
    f"src/{projectName}/logging/__init__.py",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/config/configuration.py",
    f"src/{projectName}/pipeline/__init__.py",
    f"src/{projectName}/entity/__init__.py",
    f"src/{projectName}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "DockerFile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    # create the directory if it's not available
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir} for the file {file_name}")

    # create the file if it's not available
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        file_path.touch(exist_ok=True)
        logging.info(f"Created file: {file_path} for the file {file_name}")


    else:
        logging.info(f"The file {file_name} already exists")

    


    

