import requests


def test_highly_reviewed():
    url = "http://127.0.0.1:5000/highly-reviewed"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises error if not 200 OK
        data = response.json()
        print("Highly Reviewed Music:")
        for item in data:
            print(f"{item['title']} by {item['artist']} — Rating: {item['rating']}")
    except requests.exceptions.RequestException as e:
        print(f"Error contacting microservice: {e}")


if __name__ == "__main__":
    test_highly_reviewed()
