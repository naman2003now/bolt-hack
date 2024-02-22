import re

ruleId = 12
severity = 3
description = "No Syslog report/information"

output = {
    "ruleId": 12,
    "severity": 3,
    "description": "No Syslog report/information",
}

def analyse(raw_text):
    matches = re.findall("(logging\shost\s[0-9]{1}[.][0-9]{1}[.][0-9]{1}[.][0-9]{1})",raw_text)
    if(matches):
        return None
    return output

