import re

ruleId = 13
severity = 3
description = "Too small logging buffer configured"

output = {
    "ruleId": 13,
    "severity": 3,
    "description": "Too small logging buffer configured",
}


def analyse(raw_text):
    matches = re.findall("logging\sbuffered\s(.*)\\\\",raw_text)
    for match in matches:
        if(int(match)<=16000):
            return output
    return None
