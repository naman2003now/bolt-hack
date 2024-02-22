import re
from rules import rule_1,rule_2,rule_12,rule_13,rule_6

rules = [
    rule_1,
    rule_2,
    rule_12,
    rule_13,
    rule_6
]

def get_hostname(raw_config):
    match = re.findall("hostname (.*)", raw_config)
    return match[0].replace("\\", "")

def analyse(filePath):
    raw = ""
    with open(filePath, "r") as file:
        for line in file: raw += line
    
    severities = [0, 0, 0]
    report = []
    for rule in rules:
        rule_output = rule.analyse(raw)
        if rule_output: 
            report.append(rule_output)
            severities[rule_output["severity"] - 1] =+ 1
    
    hostname = get_hostname(raw)
    risk = "green"
    if severities[1] > 0:
        risk = "yellow"
    if severities[0] > 0: 
        risk = "red"
    output = {
        "hostname": hostname,
        "risk": risk,
        "report": report,
        "severities": severities
    }
    return output
