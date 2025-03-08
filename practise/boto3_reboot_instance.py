import boto3
from botocore.exceptions import ClientError
def lambda_handler(event,context):
    ec2=boto3.client('ec2')
    action=event.get('action','').upper()
    instance_id=event.get('instance_id')
    
    if action=="ON":
         try:
           ec2.reboot_instances(InstanceIds=[instance_id],DryRun=True)
         except ClientError as e:
           if 'DryRunOperation' not in str(e):
               raise 
         resonse=ec2.reboot_instances(InstanceIds=[instance_id],DryRun=False)
    elif action=="OFF":
        print("not rebooting the instance")
    else:
        print("invalid action")
     