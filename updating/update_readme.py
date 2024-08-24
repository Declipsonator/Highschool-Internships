def update_readme(internships):
    lines = []
    
    for internship in internships:
        line = "| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
            internship["name"],
            internship["description"].replace("\n", "<br/>").replace("\r", "<br/>"),
            internship["location"],
            "/".join(internship["mode"]),
            internship["duration"],
            "{}/{}/{}".format(internship["deadline"]["month"], internship["deadline"]["day"], internship["deadline"]["year"]),
            "[Link]({})".format(internship["link"]),
            internship["opens_applications"],
            ", ".join([str(grade) for grade in internship["grade_level"]]),
            internship["price"],
        )
        lines.append(line)

    with open("TEMPLATE.md", "r") as file:
        template = file.read()

    template = template.replace("<!-- INTERNSHIPS -->", "\n".join(lines))

    with open("../README.md", "w+") as file:
        file.write(template)
