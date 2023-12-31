import requests
import sys

HOST_URL = sys.argv[1]
USERNAME = sys.argv[2]
PASSWORD = sys.argv[3]

r = requests.post(f"http://{HOST_URL}:8080/api/v1/login", json={"id":f"{USERNAME}", "password":f"{PASSWORD}"})
TOKEN = r.json().get('token')
print(f"The token is: {TOKEN}")

HEADERS = {"Accept": "application/json", "aqua-auth" : f"Bearer {TOKEN}"}

i = requests.post(f"http://{HOST_URL}:8080/api/v1/scanner/registry/Docker%20Hub/image/centos:8/scan", headers=HEADERS)
print(i)

r = requests.get(f"http://{HOST_URL}:8080/api/v2/containers?status=running&container_type=containers&page=1&pagesize=50", headers=HEADERS)
print(r)
