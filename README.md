# troy-microservice
# Microservice A – Highly Reviewed Music

## Overview
This microservice provides a list of music tracks with high review ratings (4.5 and above). It connects to a SQLite database and returns JSON data via an HTTP GET request.

## Endpoint

- **URL:** `http://127.0.0.1:5000/highly-reviewed`  
- **Method:** GET  
- **Description:** Returns a JSON array of music tracks with fields: `title`, `artist`, and `rating`.

## Request Example (Python)

```python
import requests

response = requests.get("http://127.0.0.1:5000/highly-reviewed")
data = response.json()
print(data)
## Response Format

```json
[
  {
    "title": "Blinding Lights",
    "artist": "The Weeknd",
    "rating": 4.9
  },
  ...
]
