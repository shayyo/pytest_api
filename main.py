from http_client import HttpClient
import api_files


client = HttpClient()

if __name__ == '__main__':

    client.http_client_post('api/v2/notification/outputs/test', 200, api_files.test_integrations)
    client.http_client_post('api/v2/notification/outputs', 201, api_files.add_integrations)

