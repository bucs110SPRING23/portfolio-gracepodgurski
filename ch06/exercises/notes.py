import json
# json is a string format, but not a file format

# Files
#  - saved program state

# def main():
#     idea = input("Enter an idea: ")
#     ideas = []
#     ideas.append(idea)
#     print(ideas)

# main()

#  When the program ends, all program data is deleted. If we want to save this, we use files

# Operating System: - manage files
# request the file from OS
#  - where (assets)
#  - name (ideas.txt)
#  - how to use it (r = read mode)(w = writes)(a = appends)
#  when open for writing, the file is deleted and restarted (if file doesnt exist, it will create it)

# - working with files is one-way

def main():
    file_pointer = open("assets/ideas.txt","r")

    ideas = file_pointer.read()
    print(ideas)


# charcater for a line break "\n"
    for i in ideas:
        file_pointer.write(i+"\n")
    file_pointer.close()


main()

