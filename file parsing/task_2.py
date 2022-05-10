import json


with open("students.json", "r") as pupils_file:
    list_of_pupils = json.load(pupils_file)

# search by class and section
pupils_class = {}
for pupil in list_of_pupils:
    key = pupil['Class'] + " " + pupil['Club']
    if pupils_class.get(key) is None:
        pupils_class[key] = list()
    pupils_class[key].append(pupil)

for i, k in pupils_class.items():
    if len(k) > 1:
        print(i, [pupil_['Name'] for pupil_ in k])

# search by gender
for gender in list_of_pupils:
    if 'M' in gender['Gender']:
        print(gender)

# search by name
for pupil in list_of_pupils:
    if 'S' in (pupil['Name']):
        print(pupil)
