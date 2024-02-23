import re


rule_id = 8
severity = 2
description = "Missing control plane policing"

output = {
    "ruleId": 8,
    "severity": 2,
    "description": "Missing control plane policing",
}

def analyse(raw_text):
    matches = re.findall("service.policy\sinput\s[a-zA-z]+",raw_text)
    if(matches):
        return None
    return output