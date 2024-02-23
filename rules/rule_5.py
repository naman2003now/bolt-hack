import re


rule_id = 5
description = "Insecure SNMP access"
severity = 2

grp = re.compile("[v3]\snoauth")
comm = re.compile("\s0\s")
grp_v3 = re.compile("\s[v3]\s")

output = {
    "ruleId": 5,
    "severity": 2,
    "description": "Insecure SNMP access",
}

def check_snmp(snmp_grp,snmp_comm):
    match = snmp_grp
    if(grp.search(snmp_grp)):
        return True
    if(comm.search(snmp_comm)):
        return True
    return False

def analyse(raw_text):
    matches_grp = re.findall("snmp.server\sgroup\s[a-z0-9]+\sv[1-3]",raw_text)
    matches_comm = re.findall("snmp.server\scommunity\s[a-z0-9]+",raw_text)
    if(check_snmp):
        return output
    return None