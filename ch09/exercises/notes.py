# Class notes - 4/24/2023

# for final project - have a assets folder, src folder - with controller, model, etc folder, main.py file & menu.py 
# GUI menus and extensions

### 4/26/2023 - Requests and APIs - Topic for final exam 

# Network Programming 
#  - Build a program that asks trivia questions 

# Server: any computer listening for incoming network connections 
# Request: incoming connection that asks for some resource from the server
# Resources can  be images, videos, music, media files, text, JSON, HTML 

# Types of requests 
    # GET - read 
        # visiting a page, downloading a file
    # PUT - write operation (requires more security)
        # login, deleting 

# Headers 
# - sent with the request and the response 
# -  tells you what's happening  -  info about the request 
        # status codes (200  =  everything went fine, 400 = resource can not be delivered, 500  = bad code on server)
        # IP  addresses
        # system info (geolocation)


## urllib 

# Request library - "Requests: HTTPs for  Humans"

# API = Application Programmers Interface
#  - Use an API to make a request to the server in the expected format
#  APIs can return data in any format, usually returned in JSON

# URL parameters: ? , &
    # binghamton.edu
    # binghamton.edu/cs
    # binghamton.edu/cs?  - ? has variables after it which can be changed
    # binghamton.edu/cs?var1=100&var2=300

# opentdb.com - open trivia base 
    # we want to use the API so we will have to look up the documentation 

    # opentdb.com/api.php?amount=1&category=18
        # this gives us one question from category 18 (comp sci)


import requests
import random

class TriviaProxyAPI:
    def __init__(self):
        self.url = "https://opentdb.com/api.php?"
        self.varstr =  "amount=2&category=18"

    def get(self):
        url = self.url + self.varstr
        response = requests.get(url)
        requests.get("https://opentdb.com/api.php?amount=1&category=18")
        data = response.json()
        return data['results']

def main():
    tp = TriviaProxyAPI()
    results = tp.get()
    # response = requests.get("https://opentdb.com/api.php?amount=1&category=18")
    # print(response.status_code)
    # # print(response.text)
    # # this returns a dictionary - we can do this automatically using method below
    # data = response.json()
    # results = data['results']

    for r in results:
        print(r['question'])
        # possibles = [r["correct_answer"],r["incorrect_answers"]]
        possibles = [r["correct_answer"]] + r["incorrect_answers"]
        random.shuffle(possibles)
        print("Make your selection:")
        for i, p in enumerate(possibles):
            print(f"{i}){p}")

        selection = int(input(":"))
        if possibles[selection] == r["correct_answer"]:
            print("You are correct")

        else:
            print(f"You need to study more. The correct answer is: {r['correct_answer']}")


main()

