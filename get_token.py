import requests
import sys
import json

HOST_URL = sys.argv[1]
USERNAME = sys.argv[2]
PASSWORD = sys.argv[3]

r = requests.post(f"http://{HOST_URL}:8080/api/v1/login", json={"id":f"{USERNAME}", "password":f"{PASSWORD}"})
TOKEN = r.json().get('token')

HEADERS = {"Accept": "application/json", "Authorization": f"Bearer {TOKEN}"}

# add image for scanning
image_data = '{"images":[{"registry":"Docker Hub","repository":"centos", "tag": "latest"}]}'
r = requests.post(f"http://{HOST_URL}:8080/api/v1/images", headers=HEADERS, json=json.loads(image_data))
if r.status_code != 200:
    sys.exit(1)
else:
    print("Image scan was added successfully")
