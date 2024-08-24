import json
from datetime import datetime

import requests

def get_nasa_internships():
    url = "https://stemgateway.nasa.gov/public/s/sfsites/aura?r=12&aura.ApexAction.execute=1"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    }
    body = "message=%7B%22actions%22%3A%5B%7B%22id%22%3A%22160%3Ba%22%2C%22descriptor%22%3A%22aura%3A%2F%2FApexActionController%2FACTION%24execute%22%2C%22callingDescriptor%22%3A%22UNKNOWN%22%2C%22params%22%3A%7B%22namespace%22%3A%22%22%2C%22classname%22%3A%22ostem_OpportunityResultsCardCtrl%22%2C%22method%22%3A%22getSearchResults%22%2C%22params%22%3A%7B%22filterCriteria%22%3A%22%7B%5C%22Opportunity%20Type%5C%22%3A%5B%5C%22Internships%5C%22%5D%7D%22%7D%2C%22cacheable%22%3Afalse%2C%22isContinuation%22%3Afalse%7D%7D%5D%7D&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Afalse%7D&aura.token=null"

    response = requests.post(url, headers=headers, data=body, verify=False)


    nasa_internships = json.loads(response.text)["actions"][0]["returnValue"]["returnValue"]
    highschool_internships = []

    for internship in nasa_internships:
        if not any(str(grade) in internship["AcademicLevel__c"] for grade in [9, 10, 11, 12]):
            continue

        name ="NASA: " +  internship["Name"]
        description = internship["ProjectDescription__c"]
        location = internship["Searchable_State__c"] if "In-person" in internship["ActivityType__c"] else None
        mode = []
        for mode_type in internship["ActivityType__c"].replace(" ", "").lower().split("/"):
            mode.append(mode_type)
        date_object = datetime.strptime(internship["RegistrationEndDate__c"], "%Y-%m-%d")


        season = "spring" if date_object.month in [7, 8, 9] else "summer" if date_object.month in [12, 1, 2, 3] else "fall" if date_object.month in [4, 5, 6] else None
        deadline = {"year": date_object.year, "month": date_object.month, "day": date_object.day}
        link = "https://stemgateway.nasa.gov/s/course-offering/{}".format(internship["Id"])
        opens_applications = "open"
        grade_level = [int(grade) for grade in internship["AcademicLevel__c"].split(";") if grade.isdigit()]
        price = 0

        highschool_internships.append({
            "name": name,
            "description": description,
            "location": location,
            "mode": mode,
            "season": season,
            "deadline": deadline,
            "link": link,
            "opens_applications": opens_applications,
            "grade_level": grade_level,
            "price": price,
            "active": True,
        })

    return highschool_internships


