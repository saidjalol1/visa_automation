import random
from playwright.async_api import async_playwright

# Sample list of cities (add more as needed)
FAKE_LOCATIONS = [
    {"name": "Berlin", "lat": 52.5200, "lon": 13.4050},
    {"name": "Tokyo", "lat": 35.6895, "lon": 139.6917},
    {"name": "New York", "lat": 40.7128, "lon": -74.0060},
    {"name": "Paris", "lat": 48.8566, "lon": 2.3522},
    {"name": "Moscow", "lat": 55.7558, "lon": 37.6173},
    {"name": "Dubai", "lat": 25.276987, "lon": 55.296249},
    {"name": "San Francisco", "lat": 37.7749, "lon": -122.4194},
    {"name": "Sydney", "lat": -33.8688, "lon": 151.2093},
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Toronto", "lat": 43.651070, "lon": -79.347015}
    # ... you can extend this list up to 100+ entries
]


    
async def create_fake_geo_context(browser, locale="en-US"):
    """Create a new context with randomized geolocation."""
    city = random.choice(FAKE_LOCATIONS)
    context = await browser.new_context(
        geolocation={"latitude": city["lat"], "longitude": city["lon"]},
        permissions=["geolocation"],
        locale=locale
    )
    print(f"[INFO] Faked geolocation set to: {city['name']} ({city['lat']}, {city['lon']})")
    return context
