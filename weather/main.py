from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse, FileResponse
import httpx
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")



@app.get("/api/weather/{city}")
async def get_weather(city: str, units: str | None = Query(default="metric")):
    normalized_units = "imperial" if units == "imperial" else "metric"
    
    async with httpx.AsyncClient() as client:
        try:
            geo_response = await client.get(
                "https://geocoding-api.open-meteo.com/v1/search",
                params={
                    "name": city,
                    "count": 1,
                    "language": "en",
                    "format": "json"
                }
            )
            geo_response.raise_for_status()
            geo_data = geo_response.json()
            
            if not geo_data.get("results"):
                raise HTTPException(status_code=404, detail=f"City '{city}' not found")
            
            location = geo_data["results"][0]
            name = location["name"]
            country = location["country"]
            latitude = location["latitude"]
            longitude = location["longitude"]
            
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Geocoding API error: {str(e)}")
        
        try:
            weather_params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m",
                "timezone": "auto"
            }
            
            if units == "imperial":
                weather_params["temperature_unit"] = "fahrenheit"
                weather_params["wind_speed_unit"] = "mph"
            
            weather_response = await client.get(
                "https://api.open-meteo.com/v1/forecast",
                params=weather_params
            )
            weather_response.raise_for_status()
            weather_data = weather_response.json()
            
            # Return structured weather data
            return {
                "city": name,
                "country": country,
                "latitude": latitude,
                "longitude": longitude,
                "units": normalized_units,
                "current": weather_data["current"]
            }
            
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Weather API error: {str(e)}")