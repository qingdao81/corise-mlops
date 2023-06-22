import requests

FILE="/workspace/corise-mlops/week3/project/data/requests.json"
#URL="https://80-qingdao81-corisemlops-9egvogk6p9y.ws-eu100.gitpod.io/predict"
URL="http://0.0.0.0/predict"

def test_requests():
    file = open(FILE, "r")
    for line in file:
        response = requests.post(URL, data = line, headers = {"accept": "application/json", "Content-Type": "application/json"})
        assert response.status_code == 200