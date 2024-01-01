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
image_data = '{"images":[{"registry":"Docker Hub","repository":"centos:latest","tag":"latest","digest":null,"source":null,"exists":false,"cf_app_guid":"","cf_space":"","cf_org":""}]}'
r = requests.post(f"http://{HOST_URL}:8080/api/v1/images', headers=HEADERS, json=json.loads(image_data)) 
