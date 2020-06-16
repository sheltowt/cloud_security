import boto3
import json

client = boto3.client('securityhub')

findings = client.get_findings()

with open("../extracted_data/security_hub.json", "w") as outfile:
	json.dump(findings, outfile)