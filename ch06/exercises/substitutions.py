import json

def main():
    text_fptr = open("news.txt","r").read()
    sub_fptr = open("subs.json","r")
    subs = json.load(sub_fptr)

    print(subs,type(subs))

# Use one list to modify another list
# Which list should you loop through?

    for i in text:
        text_fptr = text_fptr.replace(subs[i]["old"],subs[i]["new"])

    for k,v in subs.items():
        text = text.replace(k,v)

    fptr = open()
main()
