import urllib.request, json 

def load_json():
    with urllib.request.urlopen("https://raw.githubusercontent.com/Skyscanner/full-stack-recruitment-test/main/public/flights.json") as url:
        data = json.loads(url.read().decode())
        return data
