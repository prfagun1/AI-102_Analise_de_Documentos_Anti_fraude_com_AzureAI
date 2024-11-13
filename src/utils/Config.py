import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("document_inteligence_endpoint")
    KEY = os.getenv("document_inteligence_key")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("storage_connection_string")
    CONTAINER_NAME = os.getenv("container_name")