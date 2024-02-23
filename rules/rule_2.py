import re
import json
rule_id = 2
description = "Weak user passwords"
severity  = 1

uppercase = re.compile("[A-Z]+")
lowercase = re.compile("[a-z]+")
numbers = re.compile("[0-9]+")
special_characters = re.compile("[^a-zA-Z0-9]+")
#passsword_check = re.compile("[a-z][A-Z][0-9][^a-zA-Z0-9]+")

output = {
    "ruleId" : 2,
    "severity": 1,
    "description" : "Weak user passwords"
}

#password [0-9] (.*)

def load_password_policy(password_policy):
    with open(password_policy) as f:
        return json.load(f)

def check_weak_password(password, policy):
    if min(map(len, password)) < policy["minLength"]:
        return output
    # if(uppercase.search(password)=="None"):
    #     return False
    # if(lowercase.search(password)=="None"):
    #     return False
    # if(numbers.search(password)=="None"):
    #     return False
    # if(special_characters.search(password)=="None"):
    #     return False
    
    return None

policy = load_password_policy("password.json")


def analyse(raw_text):
    matches = re.findall("password [0-9|\s]{0,2}(.*)\\\\", raw_text)
    return check_weak_password(matches, load_password_policy("password.json"))
