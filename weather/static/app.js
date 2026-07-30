async function getWeather() {
    const city = document.getElementById("cityInput").value.trim();
    const weatherResult = document.getElementById("weatherResult");

    if (!city) {
        weatherResult.innerHTML = "<p>Please enter a city name.</p>";
        return;
    }

    weatherResult.innerHTML = "<p>Loading...</p>";

    try {
        const response = await fetch(`/api/weather/${encodeURIComponent(city)}`);

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail);
        }

        const data = await response.json();

        const tempUnit = data.units === "imperial" ? "°F" : "°C";
        const windUnit = data.units === "imperial" ? "mph" : "km/h";

        weatherResult.innerHTML = `
            <h2>${data.city}, ${data.country}</h2>
            <p><strong>Temperature:</strong> ${data.current.temperature_2m} ${tempUnit}</p>
            <p><strong>Feels Like:</strong> ${data.current.apparent_temperature} ${tempUnit}</p>
            <p><strong>Humidity:</strong> ${data.current.relative_humidity_2m}%</p>
            <p><strong>Wind Speed:</strong> ${data.current.wind_speed_10m} ${windUnit}</p>
            <p><strong>Coordinates:</strong> ${data.latitude}, ${data.longitude}</p>
        `;
    } catch (error) {
        weatherResult.innerHTML = `<p style="color:red;">${error.message}</p>`;
    }
}