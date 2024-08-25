def update_readme(internships):
    lines = []
    
    for internship in internships:
        description = internship["description"] if len(internship["description"]) < 100 else internship["description"][:100] + "..."
        season = internship["season"]
        season = "N/A" if season is None else (season.replace("spring", "Spring").replace("summer", "Summer").replace("fall", "Fall"))

        line = "| {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
            "[" + str(internship["name"]) + "]" + "(" + str(internship["link"]) + ")",
            description.replace("\n", "<br/>").replace("\r", "<br/>"),
            internship["location"] if internship["location"] is not None else "N/A",
            "<br/>".join(internship["mode"]).replace("in-person", "In&#8209;person").replace("virtual", "Virtual").replace("hybrid", "Hybrid"),
            season,
            "{}/{}/{}".format(internship["deadline"]["month"], internship["deadline"]["day"], internship["deadline"]["year"]),
            internship["opens_applications"].replace("open", "Open"),
            ", ".join([str(grade) for grade in internship["grade_level"]]),
            internship["price"],
        )
        lines.append(line)

    with open("TEMPLATE.md", "r") as file:
        template = file.read()

    template = template.replace("<!-- INTERNSHIPS -->", "\n".join(lines))

    with open("../README.md", "w+") as file:
        file.write(template)
