import requests
import sys

TOKEN = sys.argv[1]



# HEADERS = {"Accept": "application/json", "aqua-auth": f"Bearer {TOKEN}", "Authorization": f"Bearer {TOKEN}"}

# i = requests.post(f"http://{HOST_URL}:8080/api/v1/scanner/registry/Docker%20Hub/image/centos:8/scan", headers=HEADERS)
# if i.status_code == 200:
#     print("Success")
# else:
#     print("Error")
#     sys.exit(1)
