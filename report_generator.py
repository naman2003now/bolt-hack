import os
import time
import json
from datetime import datetime


def create_html():
    with open("static\\index.html") as file:
        output_file = open("Report\\index.html", "w+")
        output_file.write(file.read())

def create_stylesheet():
    with open("static\\style.css") as file:
        output_file = open("Report\\style.css", "w+")
        output_file.write(file.read())

def create_script():
    with open("static\\app.js") as file:
        output_file = open("Report\\app.js", "w+")
        output_file.write(file.read())

def gen_report_txt(device_output):
    device_output['timestamp'] = str(datetime.utcfromtimestamp(time.time()))
    with open(os.path.join(f"Report", device_output['hostname'] + ".txt"), "w+") as file:
        output = ""
        output += f"Device name: {device_output['hostname']} \n"
        output += f"Report Generated @ {device_output['timestamp']} \n\n"
        output += f"Number of Severity 1 findings: {device_output['severities'][0]}\n" 
        output += f"Number of Severity 2 findings: {device_output['severities'][1]}\n"
        output += f"Number of Severity 3 findings: {device_output['severities'][2]}\n\n"
        output += "Report:\n\n"
        for report in device_output['report']:
            output += f"#{report['ruleId']}\n"
            output += f"Severity: {report['severity']}\n"
            output += f"Description: {report['description']}\n\n"
        file.write(output)

def gen_report_json(analyser_output):
    output = []
    for device_output in analyser_output:
        output.append({
            "hostname": device_output['hostname'],
            "risk": device_output['risk'],
            "report_url": f"{device_output['hostname']}.txt",
            "timestamp": device_output['timestamp']
        })
    json.dump(output, open(os.path.join("Report", "output.json"), "w+"))
            

def generate_report(analyser_output):
    if not os.path.exists("Report"):
        os.makedirs("Report")

    create_html()
    create_stylesheet()
    create_script()
    
    for device_output in analyser_output: gen_report_txt(device_output)
    gen_report_json(analyser_output)