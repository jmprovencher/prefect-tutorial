import requests
from prefect import flow

@flow
def call_api(url):
    return requests.get(url).json()

api_result = call_api("http://time.jsontest.com/")
print(api_result)