import config_analyser
import report_generator
import os

output = []

for config in os.listdir("Configs"):
    config_file_path = os.path.join("Configs", config)
    config_absolute_path = os.path.abspath(config_file_path)
    output.append(config_analyser.analyse(config_absolute_path))
    
report_generator.generate_report(output)