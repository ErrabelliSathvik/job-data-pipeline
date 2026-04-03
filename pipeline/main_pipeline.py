import logging
from scripts.extract import run_extract
from scripts.transform import run_transform
from scripts.load import run_load

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_pipeline():
    logging.info("Starting pipeline")

    logging.info("Extract step")
    run_extract()

    logging.info("Transform step")
    run_transform()

    logging.info("Load step")
    run_load()

    logging.info("Pipeline completed")

if __name__ == "__main__":
    run_pipeline()