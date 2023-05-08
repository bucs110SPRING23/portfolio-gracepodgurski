import requests

class Astrology:
    def __init__(self):
        self.url = "https://aztro.sameerkumar.website?"
        self.additions = "sign=gemini &day= today"

    def get(self):
        url = self.url
        response = requests.get(url)
        data = response.json()
        return data['results']
    

def main():
    astro = Astrology()

    # params = (('sign', 'gemini'),('day', 'today'),)

    # requests.post('https://aztro.sameerkumar.website/', params=params)

    results = astro.get()
    print(results.status_code)
    print(results.text)





main()