import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    ec2=boto3.client("ec2")
    response=ec2.describe_in(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    print(response)