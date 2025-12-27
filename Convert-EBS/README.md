# Python-project
As a cloud engineer we take care of AWS environment and ensuring it is in compliance with organizational policies. 

In this project we use ``AWS cloud watch`` and ``Lambda function AWS`` to govern the resource according to the policies

For instance, we trigger a lambda when an Elastic Blob Storage
(EBS) is created, we use Cloud watch evens that allows us to monitor and respond to EBS volume that are of type GP2 and convert it to GP3

Let's say someone want to create EBS with type GP2 and your Organization want to everyone create EBS with type of GP3 because of the performance issue, then there's a new developer create EBS Volume using type of GP2 and Lambda will trigger and convert it to GP3.

# Prerequisite for this project
- Create and Configure Cloud watch -> Go to CW, Events, Rules and create a new rules. for service name choose EC2, event type (ebs volume notification), create specific event (createVolume) and choose any volume ARN.
- Create IAM policy for ec2.service -> add permission and set up action to All ec2 action if fails set to volumes for actions (List and modify) for resources (All resources)