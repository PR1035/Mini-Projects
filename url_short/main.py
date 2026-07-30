from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import secrets
from pydantic import BaseModel

app = FastAPI()

url_mapping = {}

class URLRequest(BaseModel):
    url : str

@app.post("/shorten")
def shorten_url(request: URLRequest):
    long_url = request.url
    shortcode = secrets.token_urlsafe(6)
    url_mapping[shortcode] = long_url
    return {"short_url": f"/r/{shortcode}"}

@app.get("/r/{shortcode}")
def redirect_url(shortcode: str):
    long_url = url_mapping.get(shortcode)
    if long_url:
        return RedirectResponse(long_url)
    else:
        raise HTTPException(status_code=404, detail="URL not found")
    