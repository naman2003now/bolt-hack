import re

ruleId = 9
severity = 2
description = "Missing Storm Control on access ports"

output = {
    "ruleId": 9,
    "severity": 2,
    "description": "Missing Storm Control on access ports",
}

def analyse(raw_text):
    matches = re.findall("storm.control\s[unciast|broadcast|multicast]+",raw_text)
    if(matches):
        return None
    return output