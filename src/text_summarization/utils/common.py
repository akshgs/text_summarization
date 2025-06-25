import os
from box.exceptions import BoxValueError
import yaml
from text_summarization.logging import logger
from ensure import ensure_annotations
from box import path
from pathlib import Path
from typing import Any 


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> cofigBox:
    """
    reads yaml file and returns

    Args:
        path_to_yaml (Path): path to yaml file
    Raises:
         ValueError: if yaml files empty
         e: empty file
    Returns:
        configBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return configBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty") 
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates list of directories
    Args:
        path_to_directories (list): list of path of directories
        ingnore_log(bool,optional): ingnore if multiple dire is to br created. defaults to False
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations

def get_size(path:Path) -> str:
    """get size in KB
    
    Args:
        path (Path): path of file
        
    Returns:
    str: size in KB
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"