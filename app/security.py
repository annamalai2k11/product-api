from fastapi import Header, HTTPException, status

from app.config import get_api_key

API_KEY = get_api_key()

def verify_api_key(x_api_key: str = Header(...)):
    if API_KEY != x_api_key:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Invalid api key"
        )