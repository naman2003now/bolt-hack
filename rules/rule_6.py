import re

ruleId = 6
severity = 2
description = "Weak Encryption Algorithm used"

output = {
    "ruleId": 6,
    "severity": 2,
    "description": "Weak Encryption Algorithm used",
}

def analyse(raw_text):
    match = re.findall("\sdes\s|aes|md5|rc2|rc4|sha-1|wep|ssl\s2.0|ssl\s3.0|pptp", raw_text)
    if(match):
        output["description"] = f"{match[0]} is a weak encryption algorithm. Use newer ones for better security."
        return output
    return None