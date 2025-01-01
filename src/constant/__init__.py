import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve credentials
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")

AWS_S3_BUCKET_NAME = "sensor-wafer-fault"
MONGO_DATABASE_NAME = "Aagam"
MONGO_COLLECTION_NAME = "waferfault"

TARGET_COLUMN = "quality"
MONGO_DB_URL = f"mongodb+srv://{username}:{password}@cluster0.mnuki.mongodb.net/?retryWrites=true&w=majority"


MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder = "artifacts"