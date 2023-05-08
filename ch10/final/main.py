import requests
import random

class Emoji:
    def __init__(self):
        self.url = "https://emojihub.yurace.pro/api/random"
        self.additions = "/category/animals-and-nature"

    def get(self):
        url = self.url + self.additions
        response = requests.get(url)
        print(response.status_code)
        print(response.text)
        # data = response.json()
        # return data['results']

class Poetry:
    def __init__(self):
        self.url = "https://poetrydb.org/title/"
        self.title = ""

    def get(self):
        url = self.url + self.title
        response = requests.get(url)
        data = response.json()
        return data['results']
    

def main():
    my_emoji = Emoji()
    results = requests.get("https://emojihub.yurace.pro/api/random/category/animals-and-nature")
    flora_fauna = str(results.text)
    my_plantoranimal = flora_fauna.split()

    for i in enumerate(my_plantoranimal):
        object = str(i)
        print(object)

    Poetry.self.title.append(object)
    my_poem = Poetry()
    final = requests.get("https://poetrydb.org/title/"+object)

main()

