AWS Prod Example Abhishek day 7 aws https://www.youtube.com/watch?v=FZPTL_kNvXc
VPC: Creates a VPC with a customizable CIDR block.
Subnets:
2 public subnets in us-east-1a and us-east-1b, with public IP assignment enabled.
2 private subnets in us-east-1a and us-east-1b.
Internet Gateway: Creates an Internet Gateway (IGW) and attaches it to the VPC.
Route Tables:
Public Route Table: Routes traffic destined for the internet (0.0.0.0/0) to the Internet Gateway.
Private Route Table: Routes traffic destined for the internet (0.0.0.0/0) to the NAT Gateways.
NAT Gateways: Creates two NAT Gateways, each in a public subnet in separate AZs (us-east-1a and us-east-1b), allowing instances in private subnets to access the internet.
Elastic IPs: Allocates two Elastic IPs for the NAT Gateways.
To deploy this template:
Save the YAML to a file (e.g., vpc-template.yaml).
Go to the AWS CloudFormation Console and create a new stack, using this YAML file.
Monitor the stack creation process.
This template sets up a VPC with a typical architecture for a highly available environment across two AZs with private and public subnets, route tables, and NAT Gateways for internet access in private
