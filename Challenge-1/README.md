This is a terraform template that reuses modules from the terraform registry to create a three tier application on AWS VPC and deploy a sample app to it.

Architecture Diagram for reference is attached in Challenge-1 Folder.

In the provisioner section, there is 
a. Providers file in which we initiaze the aws provider. 
b. main.tf file we create an s3 backet and dynamodb table for storing the terraform state file in backend. 
c. backend.tf, backend configuration for storing state file is defined.
d. data.tf, getting the data of ami
e. vpc.tf, creating the vpc, public and private subnets, NAT gateway
f. web-asg.tf, creating security group, launching the configuration and creating auto scaling group for front-end.
g. web-elb.tf, creating security group and elastic load balancer for front-end.
h. app-asg.tf, creating security group, launching the configuration and auto scaling group for application-end.
i. app-elb.tf, creating security group and elastic load balancer for app-end.
j. rds.tf, creating rds with postgresgl.
h. variables.tf, variables description and its type

In the variables section, terraform.tfvars is there where we can pass the values

The application (web-app) folder has been taken from the google source just to show how application has been deployed on infrastructure.

# Usage

1. Run terraform init for initializing the terraform plugins, providers and backend

2. Run terraform validate to check if there in any syntax error.

3. Run terraform plan -var-file=variables/terraform.tfvars, to cross check the changes that would later be applied to real-time environment.

4. Run terraform apply -var-file=variables/terraform.tfvars for applying the change to real time environment

