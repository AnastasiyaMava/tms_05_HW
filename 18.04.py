import json

data = {
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}

with open("18.json", "w") as f:
    str_json = json.dumps(data)
    json.dump(str_json, f)


with open("18.json", "r") as f:
    data = json.load(f)

    print(data)


