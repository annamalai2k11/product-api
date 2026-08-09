import os
from dotenv import load_dotenv
from fastapi import Header, HTTPException, status

load_dotenv()

API_KEY = os.getenv("API_KEY")

def verify_api_key(x_api_key: str = Header(...)):
    if API_KEY != x_api_key:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Invalid api key"
        )