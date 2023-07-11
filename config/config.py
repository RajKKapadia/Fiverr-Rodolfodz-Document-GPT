import os
import tempfile

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_TOKEN = os.getenv('TWILIO_TOKEN')
FROM = os.getenv('FROM')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENVIRONMENT = os.getenv('PINECONE_ENVIRONMENT')
PINECONE_INDEX_NAME=os.getenv('PINECONE_INDEX_NAME')

OUTPUT_DIR = os.path.join(
    tempfile.gettempdir(),
    'document-gpt',
    'output'
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

ERROR_MESSAGE = 'We are facing a technical issue at this moment.'
