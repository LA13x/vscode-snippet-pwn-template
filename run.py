import json

def go():
    data = {}
    content = []

    with open("settings.json", "r") as f:
        jsdata = json.load(f)

    jsonPath = jsdata["jsonPath"]
    files = jsdata["filePath"]
    names =  jsdata["snippetName"]

    for i in range(len(files)):
        with open(files[i], "r") as f:
            content = f.read().splitlines()
        data[names[i]] = {
            "prefix": names[i], 
            "body": content
        }

    with open(jsonPath, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("OK!")

if __name__ == "__main__":
    go()