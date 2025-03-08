import boto3
def lambda_handler(event,context):
   

# AWS Configuration
    AMI_ID = "ami-05b10e08d247fb927" # Replace with your AMI ID
    INSTANCE_TYPE = "t2.micro"
    KEY_NAME = "aws_prod_example"  # Replace with your EC2 key pair name
    #SECURITY_GROUP_ID = "sg-xxxxxxxxxxxxxxxxx"  # Replace with your security group ID
    #SUBNET_ID = "subnet-xxxxxxxxxxxxxxxxx"  # Replace with your subnet ID
    INSTANCE_NAME = "MyEC2Instance"

    # Create EC2 client
    ec2 = boto3.client("ec2")

    # Launch EC2 Instance
    response = ec2.run_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
    
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [{"Key": "Name", "Value": INSTANCE_NAME}],
            }
        ],
    )

    # Extract Instance ID
    instance_id = response["Instances"][0]["InstanceId"]
    print(f"EC2 instance {instance_id} is launching...")
