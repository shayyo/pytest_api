import requests
import sys

HOST_URL = sys.argv[1]
USERNAME = sys.argv[2]
PASSWORD = sys.argv[3]

r = requests.post(f"http://{HOST_URL}:8080/api/v1/login", json={"id":f"{USERNAME}", "password":f"{PASSWORD}"})
token = r.json().get('token')
print(f"The token is: {token}")
