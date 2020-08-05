import requests

url_to_get = "http://checklight.pythonanywhere.com/streets"
response_data = ""
def make_requests(url):
    global response_data

    response = requests.get(url)
    response_data = response 

def check_for_success():
    if response_data.status_code == 200:
        print("Request was successful")

def json_or_content():
    try:
        response_data.json()
        data = response_data.json()
        keyz = data.keys()
        print("data type is json")
        print(keyz)

    except:
        response_data.content()
        print("data type is HTML")

def print_keys():
    data = response_data.json()
    keyz = data.keys()
    print(keyz)


make_requests(url_to_get)
check_for_success()
json_or_content()
print_keys()