import re

rule_id = 1
description = "Too many user accounts"
severity = 2
MAX_NUMBER_OF_USER_ACCOUNTS = 3

output = {
    "ruleId": 3,
    "severity": 1,
    "description": "Too many user accounts",
}


def analyse(raw_text):
    matches = re.findall("(password 0|password (.*))", raw_text)
    if len(matches) > 0: 
        output["description"] = f"You have unsafe passwords!"
        return output  
    return None