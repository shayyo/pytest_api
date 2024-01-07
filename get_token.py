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


# test webhook integration
webhook_test_data = '{"type":"webhook","use_mx":false,"name":"my_web_hook","url":"https://webhook.site/c726d66d-047f-4253-b6ca-0b30670c7a98"}'
r = requests.post(f"http://{HOST_URL}:8080/api/v2/notification/outputs/test", headers=HEADERS, json=json.loads(webhook_test_data))
if r.status_code != 200:
    sys.exit(1)
else:
    print("Webhook test was successful")


# test adding webhook integration
webhook_add_data = '{"properties":{"use_mx":false,"url":"https://webhook.site/c726d66d-047f-4253-b6ca-0b30670c7a98"},"type":"webhook","name":"my_web_hook"}'
r = requests.post(f"http://{HOST_URL}:8080/api/v2/notification/outputs", headers=HEADERS, json=json.loads(webhook_add_data))
if r.status_code != 201:
    print("ERROR: ", r.text, r.status_code)
    sys.exit(1)
else:
    print("Webhook was added successfully")
