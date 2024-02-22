import re

rule_id = 1
description = "Too many user accounts"
severity = 2
MAX_NUMBER_OF_USER_ACCOUNTS = 3

output = {
    "ruleId": 1,
    "severity": 2,
    "description": "Too many user accounts",
}


def analyse(raw_text):
    matches = re.findall("\n(username|user.name)", raw_text)
    if len(matches) > MAX_NUMBER_OF_USER_ACCOUNTS: 
        output["description"] = f"{len(matches)} is a little too many user accounts;"
        return output  
    return None