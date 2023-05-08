import requests

class Astrology:
    def __init__(self):
        self.url = "https://aztro.sameerkumar.website"

    def get(self):
        url = self.url
        response = requests.get(url)
        data = response.json()
        return data['results']
    

def main():
    astro = Astrology()
    results = astro.get()
    print(results.status_code)
    print(results.text)


main()