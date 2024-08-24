import datetime

import nasa
import json
import update_readme

with open("../internships.json", "r") as file:
    current_internships = json.load(file)


# Update Nasa internships
nasa_internships = nasa.get_nasa_internships()

for internship in nasa_internships:
    if internship["name"] not in [intern["name"] for intern in current_internships]:
        current_internships.append(internship)

print("{} NASA internships found".format(len(nasa_internships)))


# Remove outdated internships
outdated_internships = [internship for internship in current_internships
                        if datetime.datetime(internship["deadline"]["year"], internship["deadline"]["month"],
                                             internship["deadline"]["day"]) < datetime.datetime.now()]

current_internships = [internship for internship in current_internships if internship not in outdated_internships]



with open("../old_internships.json", "w") as file:
    json.dump(outdated_internships, file, indent=4)

with open("../internships.json", "w") as file:
    json.dump(current_internships, file, indent=4)

update_readme.update_readme(current_internships)