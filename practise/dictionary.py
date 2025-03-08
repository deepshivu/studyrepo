student_details={"name":"ram","age":10,"class":11}
print(student_details["name"])
ec2_instance_details={"name":"instance1","instance_type":"t2.micro"}
print(ec2_instance_details["name"])
ec2_instance_details["instance_type"]="t2.xlarge"
print(ec2_instance_details["instance_type"])
ec2_instance_details["public_ip"]="1.2.3.4"
ec2_instance_details["private_ip"]="5.6.7.8"
print(ec2_instance_details)
del ec2_instance_details["private_ip"]
print(ec2_instance_details)
if "public_ip" in ec2_instance_details:
    print("public ip exists")
else:
    print("public ip does not exist")
for key, value in ec2_instance_details.items():
    print(key, value)