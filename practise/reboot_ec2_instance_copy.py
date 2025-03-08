import boto3
from botocore.exceptions import ClientError
def lambda_handler(event,context):
    action=event.get("action",'').upper()
    instance_id=event.get("instance_id")
    print(action)
    print(instance_id)
    ec2=boto3.client("ec2")
    if action=="ON":
        try:
            response=ec2.reboot_instances(InstanceIds=[instance_id],DryRun=True)
        except ClientError as e:
            if "DryRunOperation" not in str[e]:
                return{"error":f"Permission error:{str(e)}"}
        try:
            response=ec2.reboot_instances(InstanceIds=[instance_id],DryRun=False)
            return{"message":f"successfully rebooted {instance_id}","response":response}
        except ClientError as e:
            return{"error":f"failed to reboot {str(e)}"}

    elif action=="OFF":
        print("not rebooting the instance")
    else:
        print("invalid action")
