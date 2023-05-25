import requests, json

class CallAPI:

    def __init__(self, api):
            parameters = {
                
            }
            self.data_get_user(api, parameters)

    def data_get_user(self, api, parameters):
        response = requests.get(f"{api}", params=parameters)
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            self.format_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")
   
    def format_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        text = json.loads(text)
        self.quote = text["quote"]
        self.author = text["author"]
        self.genre = text["genre"]
        print(text)
        # print("quote is:", quote)
