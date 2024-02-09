from dotenv import load_dotenv
load_dotenv()

import os

CMA_TOKEN = os.getenv('CMA_TOKEN')
SPACE_ID = os.getenv('SPACE_ID')
SPACE_ENVIRONMENT = os.getenv('SPACE_ENVIRONMENT')
CONTENT_MODEL = os.getenv('CONTENT_MODEL')
