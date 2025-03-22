import os
import pandas
import yaml
from src.logger import get_logger
from src.custom_exception import CustomException
import pandas as pd

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File is not in the given path")
        
        with open(file_path, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Successfully read the YAML file")
            return config
        
    except Exception as e:
        logger.error("error while reading yaml file")
        raise CustomException("Failed to read yaml file",e)
    
def load_data(path):
    try:
        logger.info("Loading data")
        return pd.read_csv(path)
        
    except Exception as e:
        logger.error(f"Error loading the data {e}")
        raise CustomException("Failed to load data" , e)