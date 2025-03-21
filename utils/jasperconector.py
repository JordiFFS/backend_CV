import requests

url = "http://173.249.34.53:9096/jasper/reports"

def SendToJasper(name: str, data: list, format: str, parameters: dict, subreports=None):
    payload = {
        "name": name,
        "format": format,
        "data": data,
        "parameters": parameters,
        "subreports": subreports
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic ZXJhczpwcm95ZWN0YWVycA=="
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    if response.status_code == 201:
        jdata = response.json()
        return jdata
    else:
        print(response.text)
        raise Exception(response.text)