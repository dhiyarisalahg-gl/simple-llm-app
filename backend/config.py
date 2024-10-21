from dotenv import load_dotenv
import os

load_dotenv()

def get_settings():
    return {
        "openai_api_key": os.getenv("OPENAI_API_KEY")
    }
