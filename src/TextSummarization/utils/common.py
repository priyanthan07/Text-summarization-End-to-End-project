import os
from box.exceptions import BoxValueError
import yaml
from src.TextSummarization.logging.Logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations        # Ensure the input and return values are valid annotations
def read_yaml(file_path: Path) -> ConfigBox:
    """reads yaml file and returns contents of config
    """
    try:
        with open(file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(dir_path: list, verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in dir_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"