from ec2_setup import create_instance

# AMI ID as per EC2 website
create_instance("ami-08e2d37b6a0129927", "t2.micro", "vockey")
print("New EC2 instance created.")
