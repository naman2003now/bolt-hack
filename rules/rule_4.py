import re

rule_id = 4
description = "Insecure access protocols"
severity = 2

output = {
    "ruleId" : 4,
    "severity" : 2,
    "description" : "Insecure access protocols",
}

def analyse(raw_text):
    match = re.findall("tftp-server\s+|ip\s+ftp\s+(username|password)\s+|ip\s+http\s+server|line\s+vty\s+\d+\s+\d+", raw_text)
    if(match):
        output["description"] = "Insecure access protocols have been detected. Please use secure access protocols."
        return output
    return None