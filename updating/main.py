import nasa
import json
import update_readme

with open("../internships.json", "r") as file:
    current_internships = json.load(file)


# Update Nasa internships
nasa_internships = nasa.get_nasa_internships()

for internship in nasa_internships:
    if internship["name"] not in [internship["name"] for internship in current_internships]:
        current_internships.append(internship)


with open("../internships.json", "w") as file:
    json.dump(current_internships, file, indent=4)

update_readme.update_readme(current_internships)