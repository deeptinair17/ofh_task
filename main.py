import json
from collections import Counter
from cvss import CVSS3

# Open the file and load the data
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

vulneabilities = data['vulnerabilities']

severity_data = [vulneability['severity'] for vulneability in vulneabilities]

severity_counts = Counter(severity_data)

print(f"Total number of Highs are     ->   {severity_counts['HIGH']}")
print(f"Total Number of Criticals are ->   {severity_counts['CRITICAL']}")
print("--------Risk based Prioritisation is as follows------")
for vuln in vulneabilities:
    if vuln['fix_version'] == None:
        print(f"You can ignore, CVE {vuln['id']} for now as it has no fix available")

def prioritise(severity_top_level):

    filtered_vulnerabilities = []
    for vuln in vulneabilities:
        cvss_score =  CVSS3(vuln['vector'].replace(" ", "").upper())
        id = vuln['id']
        cvss_score = cvss_score.base_score
        fix_version = vuln['fix_version']
        severity = vuln['severity']

        if(severity_top_level == severity.upper()):
            filtered_vulnerabilities.append((id, cvss_score, fix_version, severity))

    filtered_vulnerabilities.sort(key=lambda x: x[1], reverse=True)

    if(len(filtered_vulnerabilities) > 0):
        print(f"Please prioritise fixing in this order for {severity_top_level}")
        for v in filtered_vulnerabilities:
            #if vuln[2] != None:
            print(v[0])

prioritise('CRITICAL')
prioritise('HIGH')
prioritise('Medium')
prioritise('Low')