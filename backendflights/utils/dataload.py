import urllib.request, json 

def data_load():
    with urllib.request.urlopen("https://raw.githubusercontent.com/Skyscanner/full-stack-recruitment-test/main/public/flights.json") as url:
        data = json.loads(url.read().decode())
        return data
print(data_load())