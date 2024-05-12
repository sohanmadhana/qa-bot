import os
import json
from elasticsearch import Elasticsearch
from tqdm.auto import tqdm
from dotenv import load_dotenv
from groq import groq
import logging

# Set up logging
logging.basicConfig(
    filename=os.path.join('app_logs', 'app.log'),  # log file name
    filemode='a',  # append to the log file
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO  # log level
)

logger = logging.getLogger(__name__)

# Log some info
logger.info('Starting the app')

# Log some success
try:
    # Instantiate Elastic search
    es = Elasticsearch("http://localhost:9200")
    logger.info('Successfully connected to Elasticsearch')
except Exception as e:
    # Log an error
    logger.error(f'Error connecting to Elasticsearch: {e}')

# Intialize llm object
try:
    llm_client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )
    logger.info('Successfully initialized llm')
except Exception as e:
    logger.error(f'Error connecting to Elasticsearch: {e}')
