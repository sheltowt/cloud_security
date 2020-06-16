import boto3
import json

client = boto3.client('cloudtrail')

findings = client.get_findings()

with open("../extracted_data/cloudtrail.json", "w") as outfile:
	json.dump(findings, outfile)