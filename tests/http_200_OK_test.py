import pytest

from api_client import APIClient

# Replace 'http://example.com/api' with the actual base URL of your API
BASE_URL = 'http://yahoo.com'
api_client = APIClient(BASE_URL)

def test_get_example():
    response = api_client.send_request('GET', '/')
    print(response.status_code)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_post_example():
    data = {"key": "value"}
    response = api_client.send_request('POST', 'example', data=data)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    # You can add more assertions based on the response content if needed
    # For example, assert response.json()["result"] == "success"
