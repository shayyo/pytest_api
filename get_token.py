import requests
import sys

HOST_URL = sys.argv[1]
USERNAME = sys.argv[2]
PASSWORD = sys.argv[3]

r = requests.post(f"http://{HOST_URL}:8080/api/v1/login", json={"id":f"{USERNAME}", "password":f"{PASSWORD}"})
TOKEN = r.json().get('token')

HEADERS = {"Accept": "application/json", "aqua-auth": f"Bearer {TOKEN}", "Authorization": f"Bearer {TOKEN}"}

